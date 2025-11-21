import os
import re
import string
import google.generativeai as genai

def preprocess_question(question):
    """
    Apply basic preprocessing to the input question
    - Lowercasing
    - Tokenization
    - Punctuation removal
    """
    # Lowercase
    question_lower = question.lower()
    
    # Remove punctuation
    question_no_punct = question_lower.translate(str.maketrans('', '', string.punctuation))
    
    # Tokenization (split into words)
    tokens = question_no_punct.split()
    
    # Join back for display
    processed = ' '.join(tokens)
    
    return processed, tokens

def query_llm(question, api_key):
    """
    Send question to Google Gemini LLM API and return the response
    """
    try:
        genai.configure(api_key=api_key)
        
        # Construct prompt
        prompt = f"Answer the following question concisely and accurately: {question}"
        
        # Create model
        model = genai.GenerativeModel('gemini-2.0-pro')
        
        # Make API call
        response = model.generate_content(prompt)
        
        # Extract answer
        answer = response.text
        return answer
        
    except Exception as e:
        return f"Error querying LLM: {str(e)}"

def main():
    """
    Main CLI application loop
    """
    print("=" * 60)
    print("LLM Question-Answering System (CLI)")
    print("By: Tochukwu Okoli (22CG031913)")
    print("=" * 60)
    print()
    
    # Get API key from environment variable or user input
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        api_key = input("Enter your Google Gemini API key: ").strip()
    
    if not api_key:
        print("Error: API key is required!")
        return
    
    print("\nWelcome! Ask me anything (type 'quit' or 'exit' to stop)")
    print("-" * 60)
    
    while True:
        # Get user input
        question = input("\nYour question: ").strip()
        
        # Check for exit commands
        if question.lower() in ['quit', 'exit', 'q']:
            print("\nThank you for using the LLM Q&A System. Goodbye!")
            break
        
        if not question:
            print("Please enter a valid question.")
            continue
        
        # Preprocess question
        processed_question, tokens = preprocess_question(question)
        print(f"\nProcessed question: {processed_question}")
        print(f"Tokens: {tokens}")
        
        # Query LLM
        print("\nQuerying LLM...")
        answer = query_llm(question, api_key)
        
        # Display answer
        print("\n" + "=" * 60)
        print("ANSWER:")
        print("=" * 60)
        print(answer)
        print("=" * 60)

if __name__ == "__main__":
    main()
