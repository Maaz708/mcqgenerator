# MCQ Generator using LangChain

## Overview

MCQ Generator is an AI-powered application that automatically generates Multiple Choice Questions (MCQs) from user-provided text or documents.

Built using **LangChain** and **Large Language Models (LLMs)**, the application helps educators, students, trainers, and content creators quickly create quizzes and assessments from any learning material.

---

## Features

* Generate MCQs from uploaded text documents
* AI-powered question generation using LangChain
* Adjustable number of questions
* Automatic answer generation
* Interactive Streamlit-based user interface
* Supports educational and training content

---

## Tech Stack

* Python
* LangChain
* Streamlit
* Groq / OpenAI / Ollama
* Pandas
* JSON
* python-dotenv

---

## Project Structure

```text
mcqgenerator/
│
├── src/
│   ├── mcqgenerator/
│   │   ├── MCQGenerator.py
│   │   ├── logger.py
│   │   ├── utils.py
│   │   └── prompt.py
│
├── Response.json
├── streamlitapp.py
├── setup.py
├── requirements.txt
├── .env
├── README.md
└── data/
```


##Screenshot
```
<img width="412" height="566" alt="Screenshot 2026-06-13 044008" src="https://github.com/user-attachments/assets/8055991e-0ea4-4b66-8c70-41c77d6e16a8" />

```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Maaz708/mcqgenerator.git
cd mcqgenerator
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_api_key
OPENAI_API_KEY=your_api_key
```

---

## Running the Application

Start the Streamlit application:

```bash
streamlit run streamlitapp.py
```

Open your browser and navigate to:

```text
http://localhost:8501
```

---

## How It Works

1. User uploads a document or provides text.
2. LangChain processes the content.
3. The LLM analyzes the text and extracts key concepts.
4. Multiple-choice questions are generated.
5. Answers and complexity analysis are returned in structured JSON format.
6. Results are displayed through the Streamlit interface.

---

## Use Cases

* Educational assessments
* Online learning platforms
* Corporate training programs
* Exam preparation
* Content summarization and evaluation
* Automated quiz generation

---

## Future Enhancements

* PDF, DOCX, and PPT support
* Export MCQs to Excel and PDF
* Difficulty-level selection
* Multi-language support
* Question quality evaluation
* Question bank management

---

## Author

**Mohd Maaz**

* GitHub: https://github.com/Maaz708
* LinkedIn: www.linkedin.com/in/mohd-maaz-1277121b1

---

## License

This project is licensed under the MIT License.



