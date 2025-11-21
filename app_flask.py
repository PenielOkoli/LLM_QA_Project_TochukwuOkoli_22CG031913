from flask import Flask, render_template, request
import string
import os
import google.generativeai as genai

app = Flask(__name__)

def preprocess_question(question):
    """
    Apply basic preprocessing to the input question
    """
    # Lowercase
    question_lower = question.lower()
    
    # Remove punctuation
    question_no_punct = question_lower.translate(str.maketrans('', '', string.punctuation))
    
    # Tokenization
    tokens = question_no_punct.split()
    processed = ' '.join(tokens)
    
    return processed, tokens

def query_llm(question, api_key):
    """
    Send question to Google Gemini LLM API and return the response
    """
    try:
        genai.configure(api_key=api_key)
        
        prompt = f"Answer the following question concisely and accurately: {question}"
        
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        
        answer = response.text
        return answer
        
    except Exception as e:
        return f"Error querying LLM: {str(e)}"

@app.route('/', methods=['GET', 'POST'])
def index():
    # Initialize variables
    error = None
    warning = None
    success = None
    question = None
    api_key = None
    processed_question = None
    tokens = None
    answer = None
    
    if request.method == 'POST':
        # Get form data
        api_key = request.form.get('api_key', '').strip()
        question = request.form.get('question', '').strip()
        
        # Validation
        if not api_key:
            error = "Please enter your Google Gemini API key!"
        elif not question:
            warning = "Please enter a question!"
        else:
            # Preprocess the question
            try:
                processed_question, token_list = preprocess_question(question)
                tokens = str(token_list)
                success = "Question processed successfully!"
                
                # Query the LLM
                answer = query_llm(question, api_key)
                
                # Format answer with line breaks
                answer = answer.replace('\n', '<br>')
                
            except Exception as e:
                error = f"An error occurred: {str(e)}"
    
    return render_template('index.html',
                         error=error,
                         warning=warning,
                         success=success,
                         question=question,
                         api_key=api_key,
                         processed_question=processed_question,
                         tokens=tokens,
                         answer=answer)

if __name__ == '__main__':
    # Use environment variable for API key if available
    app.secret_key = os.getenv('SECRET_KEY', 'your-secret-key-here')
    app.run(debug=True, host='0.0.0.0', port=5000)
