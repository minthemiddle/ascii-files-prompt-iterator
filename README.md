# Asciidox Processor

## Overview

This application processes `.adoc` files in a specified folder using OpenAI's API. It reads prompts from a given file and applies them to each `.adoc` file, updating the content based on the API response.

## Prerequisites

- Python 3.x
- An API key from OpenAI (stored in the environment variable `OPENROUTER_API_KEY`)
- `click` and `openai` Python packages installed

## Installation

1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required packages:
   ```sh
   pip install click openai
   ```

3. Set your OpenAI API key:
   ```sh
   export OPENROUTER_API_KEY=<your-api-key>
   ```

## Usage

Run the script with the following command:
```sh
python main.py <folder-path> <prompts-file-path>
```

### Arguments

- `folder-path`: The path to the folder containing `.adoc` files.
- `prompts-file-path`: The path to the file containing prompts, one per line.

## Example

Suppose you have a folder `docs` containing `.adoc` files and a file `prompts.txt` with the following content:
```
Add a comment at the end of each file.
```

You would run:
```sh
python main.py docs prompts.txt
```

This will process each `.adoc` file in the `docs` folder, appending the specified comment to the end of each file.

## Notes

- The application uses the `google/gemini-flash-1.5-exp` model with a temperature of 0.3.
- The API response is written back to the original `.adoc` file.
