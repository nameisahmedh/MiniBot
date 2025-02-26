# MiniBot

MiniBot is a simple chatbot application built using Python, Google Generative AI (Gemini), and the Shiny framework. It provides an interactive interface for users to enter a prompt and receive AI-generated responses.

## Features
- Uses **Google Generative AI (Gemini)** for text-based responses.
- Built with **Shiny for Python** to create a web-based interface.
- Accepts user input through a text area and generates AI-based responses.
- Styled using an external CSS file.
- Utilizes `multiprocessing` to handle concurrent requests efficiently.

## Requirements
Ensure you have the following installed before running the project:

- Python 3.8+
- Required Python libraries:
  - `os`
  - `shiny`
  - `google-generativeai`
  - `multiprocessing`
  - `python-dotenv`

You can install the required dependencies using:
```sh
pip install shiny google-generativeai python-dotenv
```

## Project Structure
```
miniBot/
│── miniBot.py      # Main script to run the chatbot
│── .env            # Stores API key (GEMINI_API_KEY)
│── style.css       # CSS file for styling
│── README.md       # Documentation file
```

## Setup & Usage
1. **Obtain a Gemini API Key**:
   - Sign up for Google Generative AI and get an API key.
   - Create a `.env` file and store the key as follows:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```

2. **Run the Application**:
   - Open a terminal and navigate to the project directory.
   - Run the script:
     ```sh
     python miniBot.py
     ```
   - The chatbot will start, and you can access it through your web browser.

## Explanation of Key Components
- **`server()`**: Handles user input and generates responses using the Gemini API.
- **`app_ui()`**: Defines the UI layout with a text input field, a submit button, and an output area.
- **`freeze_support()`**: Ensures multiprocessing works correctly on Windows.
- **`Process(target=run_app(...))`**: Runs the Shiny app in a separate process.

## Troubleshooting
- If you encounter issues with missing dependencies, ensure you have installed all required libraries.
- If the API key is incorrect or missing, the app may fail to fetch responses from Gemini AI.
- Check for syntax errors or indentation issues if the script does not run properly.

## Future Improvements
- Implement better error handling for API failures.
- Improve the UI with additional styling and interactive elements.
- Add support for more AI models and functionalities.

## License
This project is open-source and available under the MIT License.

