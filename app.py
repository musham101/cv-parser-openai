from flask import Flask, jsonify, request
from cv_parser_openai import CV_PARSER

app = Flask(__name__)

@app.route('/parser', methods=['POST'])
def get_data():
    try:
        # Get the URL of the external API from the request JSON data
        request_data = request.get_json()
        if '.pdf' in request_data['file_name']:
            if request_data['file_type'] == 'text':
                response = CV_PARSER.make_request_openai(request_data['resume_body'])
                return response
            elif request_data['file_type'] == 'base64':
                CV_PARSER.base64_to_pdf(request_data['resume_body'])
                text = CV_PARSER.pdf_to_text('resume\last_parsed_cv.pdf')
                response = CV_PARSER.make_request_openai(text)
                return response
        elif '.doc' in request_data['file_name']:
            if request_data['file_type'] == 'text':
                response = CV_PARSER.make_request_openai(request_data['resume_body'])
                return response
            elif request_data['file_type'] == 'base64':
                CV_PARSER.base64_to_pdf(request_data['resume_body'])
                text = CV_PARSER.word_to_text('resume\last_parsed_cv.docx')
                response = CV_PARSER.make_request_openai(text)
                return response
    except Exception as e:
        return jsonify({'error': 'An error occurred: {}'.format(str(e))}), 500

if __name__ == '__main__':
    app.run(debug=True)
