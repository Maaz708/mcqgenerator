import os
import json
import pandas as pd
import traceback
from src.mcqgenerator.utils import read_file, get_quiz_table
from src.mcqgenerator.logger import logging

from langchain_groq import ChatGroq
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_community.callbacks.manager import get_openai_callback
import PyPDF2
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
openai_key=os.getenv("OPENAI_API")
groq_api_key=os.getenv("GROQ_KEY")


# llm2=ChatOpenAI(
#     model="gpt-3.5-turbo",
#     api_key=openai_key
# )

# llm3 = ChatOllama(
#     model ="llama3.1:latest",
#     temperature=1
# )
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key = groq_api_key
)

Response_json = {
    "1":{
        "mcq":"multiple choice question",
        "options":{
            "a":"choice here",
            "b":"choice here",
            "c":"choice here",
            "d":"choice here"
        },
        "correct":"correct answer"
    },
    "2":{
        "mcq":"multiple choice question",
        "options":{
            "a":"choice here",
            "b":"choice here",
            "c":"choice here",
            "d":"choice here"
        },
        "correct":"correct answer"
    },
    "3":{
        "mcq":"multiple choice question",
        "options":{
            "a":"choice here",
            "b":"choice here",
            "c":"choice here",
            "d":"choice here"
        },
        "correct":"correct answer"
    }
}


template = """
Text:{text}
You are an expert MCQ maker. Given the above text, it is your job to \
create quiz of {number} multiple choice for {subject} students in {tone} tone.
Make sure the questions are not repeated and check all the questions to be conforming the text as well.
Ensure to make {number} MCQs
### Response_json
{response_json}

"""


quiz_prompt = PromptTemplate(
    input_variables=["text","number","subject","tone","response_json"],
    template=template
)

quizreview_chain = quiz_prompt | llm | StrOutputParser()

template2 = """
You are an expert in english grammar and writer.

Given a Multiple Choice Quiz for {subject} students.

You need to:
1. Evaluate quiz complexity.
2. Give complexity analysis in max 50 words.
3. Update questions if needed.
4. Return ONLY valid JSON.

Quiz_mcq:
{quiz}

Return output in this format:

{{
    "complexity_analysis":"...",
    "quiz": {response_json}
}}
"""

quiz_eval_prompt = PromptTemplate(
    input_variables=["subject","quiz","response_json"],
    template=template2
)

final_chain = ({  "quiz": quizreview_chain, "subject" : lambda x: x["subject"], "response_json": lambda x: json.dumps(Response_json) }
                | quiz_eval_prompt 
                | llm 
                | JsonOutputParser())

