# PromptSpark

A minimal Python CLI app for interacting with OpenAI's API.

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

Run the CLI:
```bash
python main.py
```

## Project Structure

- `main.py` - Entry point and CLI orchestration
- `prompts.py` - Prompt templates and building logic
- `api.py` - OpenAI API client and request handling
- `.env` - Environment variables (secrets)
- `requirements.txt` - Python dependencies
