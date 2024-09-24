import click
import os
from openai import OpenAI
from os import getenv

# Initialize OpenAI client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=getenv("OPENROUTER_API_KEY"),
)

SYSTEM_PROMPT = """You always return the full original text unchanged. You either append in-context comments (as comment lines AFTER the sentence) or as document level comment ([comment]
--
A document comment block.

Notice it's a delimited block.
--). The document level block gets appended to the end of the file."""

@click.command()
@click.option('--folder', '-f', type=click.Path(exists=True), required=True, help="Path to the folder containing .adoc files")
@click.option('--prompts-file', '-p', type=click.Path(exists=True), required=True, help="Path to the file containing prompts")
def process_files(folder, prompts_file):
    # Read prompts from file
    with open(prompts_file, 'r') as f:
        prompts = f.read().splitlines()

    # Get all .adoc files in the folder
    adoc_files = [f for f in os.listdir(folder) if f.endswith('.adoc')]

    for prompt in prompts:
        for file in adoc_files:
            file_path = os.path.join(folder, file)
            
            # Read the content of the file
            with open(file_path, 'r') as f:
                content = f.read()

            # Create the messages for the API call
            messages = [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"{prompt}\n\n{content}"}
            ]

            # Make the API call
            completion = client.chat.completions.create(
                extra_headers={
                    "X-Title": "asciidox",  # Replace with your app name
                },
                model="google/gemini-flash-1.5-exp",
                temperature=0.3,
                messages=messages,
            )

            # Get the response
            response = completion.choices[0].message.content

            # Write the response back to the file
            with open(file_path, 'w') as f:
                f.write(response)

            print(f"Processed {file} with prompt: {prompt}")

if __name__ == '__main__':
    process_files()
