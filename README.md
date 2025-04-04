# 🧠 AI Agent Code Generator

This project is an intelligent code assistant that leverages **LlamaIndex**, **Ollama**, and a local language model like `llama2` to analyze documents and respond to prompts intelligently. It supports tasks such as reading API documentation from PDF files and inspecting local code files interactively via terminal input.

---

## 🚀 Features

- 🔎 Intelligent prompt understanding and reasoning
- 📄 Parses and indexes documentation (e.g., PDFs)
- 🧠 Uses local LLM (via [Ollama](https://ollama.com)) for language reasoning
- 📂 Reads and returns content of local code files
- 🤖 Interactive loop with agent responses

---

## 📁 Project Structure

### Folder & File Explanation

- **`ai/`**  
  Virtual environment directory (created with `python -m venv ai`).  
  Not necessary to track with Git – usually added to `.gitignore`.

- **`data/`**  
  Contains all the **input documents** you want the agent to analyze.  
  Supports `.pdf` files (API docs) and `.py` files (source code).

- **`.env`**  
  Optional environment variables. Example:
  ```env
  LLAMA_CLOUD_API_KEY=your_key_here


---

## ⚙️ Requirements

Make sure you have the following installed:

- [Python 3.10+](https://www.python.org/downloads/)
- [Ollama](https://ollama.com) (running locally with models pulled like `llama2`, `codellama`)
- Git
- Optional (for PDF parsing): LlamaParse API key

---

## 🧱 Setup Instructions
### 1. Clone the repository

### 2.Create and activate a virtual environment
python -m venv ai

- Activate on Windows:
ai\Scripts\activate

- Or activate on Unix/Mac:
source ai/bin/activate

### 3.Install Python dependencies
- pip install -r requirements.txt

### 4. Pull Ollama models (if not already installed)
- ollama pull llama2
- ollama pull codellama



## 🧪 Running the App
python Main.py

### Example prompt:
+ read the content of test.py and explain what it does
+ analyze the API documentation in readme.pdf
+ send a post request to make a new item using api in python


##  🔐.env Example (Optional):
LLAMA_CLOUD_API_KEY=your_api_key_here 
(You can get your API key from: https://cloud.llamaindex.ai)


## 📦 Dependencies
The most important packages in requirements.txt:
- llama-index
- llama-parse
- ollama
- python-dotenv

You can generate the file automatically with:
- pip freeze > requirements.txt



# ✨ Credits
- Powered by LlamaIndex + Ollama
