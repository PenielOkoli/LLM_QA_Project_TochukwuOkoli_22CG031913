import streamlit as st
import string
import os
import google.generativeai as genai

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
        
        # Try different model names in order
        model_names = [
            'gemini-1.5-flash-latest',
            'gemini-1.5-flash',
            'gemini-1.5-pro',
            'gemini-pro'
        ]
        
        last_error = None
        for model_name in model_names:
            try:
                model = genai.GenerativeModel(model_name)
                response = model.generate_content(prompt)
                return response.text
            except Exception as e:
                last_error = str(e)
                continue
        
        return f"Error: Could not connect to any Gemini model. Last error: {last_error}"
        
    except Exception as e:
        return f"Error querying LLM: {str(e)}"

# ← IMPORTANT: Blank line after function definition
# Page configuration
st.set_page_config(
    page_title="LLM Q&A System",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #1E88E5;
        text-align: center;
        padding: 1rem 0;
    }
    .sub-header {
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .stTextInput > div > div > input {
        font-size: 1.1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🤖 LLM Question-Answering System</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">By: Tochukwu Okoli (22CG031913)</p>', unsafe_allow_html=True)

# Sidebar for API key
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # Try to get API key from environment (Streamlit Secrets)
    env_api_key = os.getenv("GEMINI_API_KEY", "")
    
    if env_api_key:
        # Key exists in secrets - use it and inform user
        api_key = env_api_key
        st.success("✅ Using API key from secure storage")
        st.info("API key is securely loaded and hidden")
    else:
        # No key in secrets - ask user to input
        api_key = st.text_input(
            "Enter Google Gemini API Key:", 
            type="password",
            help="Your API key is not saved and only used for this session"
        )
    
    st.markdown("---")
    st.markdown("### About")
    st.info("This application uses Google's Gemini AI to answer your questions. Get your free API key at [aistudio.google.com](https://aistudio.google.com/app/apikey)")

# Main interface
col1, col2 = st.columns([2, 1])

with col1:
    question = st.text_input("🔍 Enter your question:", placeholder="What is machine learning?")
    
if st.button("Get Answer", type="primary", use_container_width=True):
    if not api_key:
        st.error("⚠️ Please enter your Google Gemini API key in the sidebar!")
    elif not question:
        st.warning("⚠️ Please enter a question!")
    else:
        # Preprocess
        with st.spinner("Processing question..."):
            processed_question, tokens = preprocess_question(question)
        
        # Display preprocessing results
        st.success("✅ Question processed!")
        
        with st.expander("📝 Preprocessing Details", expanded=True):
            col_a, col_b = st.columns(2)
            with col_a:
                st.write("**Original Question:**")
                st.info(question)
            with col_b:
                st.write("**Processed Question:**")
                st.info(processed_question)
            
            st.write("**Tokens:**")
            st.code(str(tokens), language="python")
        
        # Query LLM
        with st.spinner("🔄 Querying LLM API..."):
            answer = query_llm(question, api_key)
        
        # Display answer
        st.markdown("---")
        st.markdown("### 💡 Answer")
        st.markdown(f"""
        <div style="background-color: #E3F2FD; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #1E88E5;">
            {answer}
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #888; padding: 1rem;">
    <p>CSC415/CSC331 Project 2 | Covenant University | 2024/2025 Alpha Semester</p>
</div>
""", unsafe_allow_html=True)
