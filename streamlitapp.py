import os
import json
import pandas as pd
import traceback
from dotenv import load_dotenv 
from src.mcqgenerator.utils import read_file, get_quiz_table
import streamlit as st
from src.mcqgenerator.mcqgenerator import final_chain
from src.mcqgenerator.logger import logging


file_path=r"C:\Users\maaz7\mcqgenerator\response.json"

with open(file_path,"r") as file:
    response_json = json.load(file)

st.title("MCQ Application generator with langchain")

with st.form("user_inputs"):
    uploaded_file = st.file_uploader("Upload a pdf or txt file")

    mcq_count = st.number_input("No. of Mcqs", min_value=3, max_value=50)

    subject = st.text_input("Input subject", max_chars=20)

    tone= st.text_input("Complexity Level of question", max_chars=20, placeholder="simple")

    button= st.form_submit_button("Create MCQS")

    if button and uploaded_file is not None and mcq_count and subject and tone:
        with st.spinner("loading...."):
            try:
                text = read_file(uploaded_file)

                response = final_chain.invoke({
                    "text": text,
                    "number": mcq_count,
                    "subject": subject,
                    "tone": tone,
                    "response_json": json.dumps(response_json)
               } )
            except Exception as e:
                traceback.print_exception(type(e),e,e.__traceback__)
                st.error("Error")
            else:
                if isinstance(response, dict):
                    quiz=response.get("quiz",None)
                    if quiz is not None:
                        table_data = get_quiz_table(quiz)
                        if table_data is not None:
                            df = pd.DataFrame(table_data)
                            df.index=df.index+1
                            st.table(df)

                            st.text_area(label="Review", value = response["complexity_analysis"])
                        else:
                            st.error("Error in the table data")
                    else:
                        st.write(response)