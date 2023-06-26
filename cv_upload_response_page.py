import streamlit as st
import base64
import requests
import fitz, json, time
from globals import API_KEY

api_key = API_KEY


q_one_liner = "get me the name, email, phone, city, educations, experiences and skills in json format from the given text"

def is_valid_json(json_data):
    try:
        json.loads(json_data)
        return True
    except TypeError:
        return False

def pdf_to_base64(pdf):
    with open(pdf, 'rb') as file:
        pdf_data = file.read()
    pdf_base64 = base64.b64encode(pdf_data).decode('utf-8')
    data = {'cv_file': pdf_base64}
    return data

def pdf_to_text(resume):
    doc = fitz.open(resume)
    text = " "
    for page in doc:
        text = text + str(page.get_text())
    text = text.strip()
    text = " ".join(text.split())
    return text

def convert_string_to_json(json_string):
    try:
        json_object = json.loads(json_string)
        return json_object
    except ValueError as e:
        print("Invalid JSON format:", e)
        return None

def make_request(text):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + api_key,
    }
    json_data = {
        'model': 'gpt-3.5-turbo',
        'messages': [
            {
                'role': 'user',
                'content': f'{text}\n {q_one_liner}',
            },
        ],
    }
    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=json_data)
    json_response = json.loads(response.text)
    answers = json_response["choices"][0]["message"]["content"]
    resp = convert_string_to_json(answers)
    return resp


st.title("CV Parser | ChatGPT")
st.subheader("Upload your CV")
# Create a file uploader component in Streamlit
pdf_file = st.file_uploader("Upload PDF", type=["pdf", "doc"])
start_time = time.time()



# Check if a PDF file was uploaded
if pdf_file is not None:
    file_contents = pdf_file.getbuffer()
    with open("cv.pdf", "wb") as f:
        f.write(file_contents)
    
    params = pdf_to_text("cv.pdf")
    api_response = make_request(params)
    end_time = time.time()
    elapsed_time = end_time - start_time

    variable_string = str(api_response)
    
    st.write("Response Time: " + str(elapsed_time) + " Seconds")

    st.subheader("ChatGPT Response:")
    st.write(api_response)






