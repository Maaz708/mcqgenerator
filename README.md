**MCQ Generator using LangChain
**
Overview

MCQ Generator is an AI-powered application that automatically generates Multiple Choice Questions (MCQs) from user-provided text or documents. Built using LangChain and Large Language Models (LLMs), the application helps educators, students, trainers, and content creators quickly create quizzes and assessments from any learning material.

Features:

Generate MCQs from uploaded text documents
AI-powered question generation using LangChain
Adjustable number of questions
Automatic answer generation
Interactive Streamlit-based user interface
Supports educational and training content

Tech Stack:

Python
LangChain
Streamlit
Groq/OpenAI/Ollama LLMs
Pandas
JSON
dotenv

Project Structure:

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

Installation:

1. Clone the Repository
git clone https://github.com/Maaz708/mcqgenerator
cd mcqgenerator
2. Create Virtual Environment
python -m venv venv
3. Activate Virtual Environment

Windows

venv\Scripts\activate

Linux/Mac

source venv/bin/activate

4. Install Dependencies
pip install -r requirements.txt
5. Configure Environment Variables

Create a .env file in the project root:

GROQ_API_KEY=your_api_key
OPENAI_API_KEY=your_api_key
Running the Application

Start the Streamlit application:

streamlit run streamlitapp.py

Open your browser and navigate to:

http://localhost:8501
How It Works
User uploads a document or provides text.
LangChain processes the content.
The LLM analyzes the text and extracts key concepts.
Multiple-choice questions are generated.
Answers and complexity analysis are returned in structured JSON format.
Results are displayed through the Streamlit interface.

Use Cases:

Educational assessments
Online learning platforms
Corporate training programs
Exam preparation
Content summarization and evaluation
Automated quiz generation
Future Enhancements:

PDF, DOCX, and PPT support
Export MCQs to Excel and PDF
Difficulty-level selection
Multi-language support
Question quality evaluation
Question bank management

Author

Mohd Maaz


License

This project is licensed under the MIT License.
