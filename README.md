# Chatbot DeepSeek

A simple Flask-based web application for interacting with a chatbot. This project uses HTML and CSS for the frontend and Flask for the backend.

## Features

- User-friendly interface for interacting with the chatbot.
- Responsive design using HTML and CSS.
- Flask backend for handling requests and responses.

## Prerequisites

Before running the application, ensure you have the following installed:
- Python (preferably version 3.7 or higher)
- Flask (for creating the web server)
- Ollama (for running DeepSeek locally)
- DeepSeek Model (deepseek-r1:1.5b)
- Text Editor/IDE (like VSCode, PyCharm, or Sublime Text)

## Installation

1. **Download Ollama**

   **For Windows:**
   Visit the official Ollama website https://ollama.com/download. Download the Windows installer.

   After installation, verify it by running the following command in PowerShell:
   
   ![image](https://github.com/user-attachments/assets/31d258fd-1292-471f-9553-c9b858a4cd71)

2. **Pulling and Running the DeepSeek-r1:1.5b Model**

   With Ollama installed, it's time to pull the DeepSeek-r1:1.5b model and run it locally.
   How to Pull the DeepSeek Model
   - Open your terminal or command prompt.
   - Type the following command to pull the model: </br>
   ```
   ollama pull deepseek-r1:1.5b
   ```
   This command will download the model, which may take some time depending on your internet speed and system resources.
3. **Checking Available Models Using ollama list**
   ```
   ollama list
   ```
   This will display all the models you have pulled and installed, including their version numbers. You can use this to verify that DeepSeek-r1:1.5b is available and ready to be used.

4. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/chatbot_deepseek_flask_app.git
   cd chatbot_deepseek_flask_app
   
5. **Set up a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
6. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```
7. **Run the Flask application:**
   ```
   flask run
   ```
8. **Access the application:**

   Open your browser and go to
   ```
   http://127.0.0.1:5000.
   ```

## Result

![image](https://github.com/user-attachments/assets/ff7ac66d-574b-4c77-aa67-beb45bdd3a3e)

