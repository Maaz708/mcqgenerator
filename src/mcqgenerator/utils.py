import os 
from PyPDF2 import PdfReader
import json
import traceback

def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            pdf_reader=PdfReader(file)
            text=""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text
        except Exception as e:
            raise Exception("error reading the Pdf file", {e})
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    
    else:
        raise Exception("Unsupported file format only pdf and text file supported")
    
def get_quiz_table(quiz_dict):
    try:
         quiz_table = []

         for key, value in quiz_dict.items():
             mcq=value["mcq"]
             options = " || ".join([
                 f"{option} -> {option_value}" for option, option_value in value["options"].items()
             ])
             correct=value["correct"]
             quiz_table.append({"MCQ":mcq, "choices": options, "correct":correct})
         return quiz_table
    except Exception as e:
        traceback.print_exception(type(e), e,e.__traceback__)
        return False