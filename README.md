# Grammar Tool Face-Off

This program allows you to compare different grammar checking tools by analyzing the same piece of text across multiple platforms.

## Features

- LanguageTool integration (free and open-source)
- Placeholder support for Grammarly (requires API key)
- Placeholder support for Hemingway Editor (requires API key)
- Detailed analysis of grammar issues and suggestions
- Easy-to-read comparison of results

## Installation

1. Clone this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the program:
   ```bash
   python grammar_faceoff.py
   ```

2. Enter the text you want to analyze. You can type multiple lines.
3. Press Ctrl+D (Unix) or Ctrl+Z (Windows) followed by Enter when you're done entering text.
4. The program will analyze the text using available grammar checkers and display the results.

## API Keys

To use Grammarly or Hemingway Editor, you'll need to:

1. Create a `.env` file in the project root
2. Add your API keys:
   ```
   GRAMMARLY_API_KEY=your_grammarly_api_key
   HEMINGWAY_API_KEY=your_hemingway_api_key
   ```

Note: Currently, only LanguageTool is fully implemented. Grammarly and Hemingway Editor integrations are placeholders as they require paid API access.

## Example Text

Here's a sample text with intentional grammar issues you can use for testing:

```
The student's was late to class yesterday. They didnt bring there homework neither. The teacher, who's been teaching for 20 years, was very disappointed. The student should of been more responsible and brought they're materials to class.
```

## Learning Outcomes

- Compare different grammar checking tools
- Understand strengths and weaknesses of each tool
- Learn about common grammar issues
- Improve writing and editing skills 