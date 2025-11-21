# LLM Question-Answering System
**By: Tochukwu Okoli (22CG031913)**

A Natural Language Processing Question-and-Answering system using Google's Gemini API with both CLI and Web GUI interfaces.

## 🚀 Features

- **CLI Application**: Command-line interface for quick Q&A
- **Web GUI**: Interactive Streamlit web application
- **Text Preprocessing**: Lowercasing, tokenization, and punctuation removal
- **LLM Integration**: Powered by Google's Gemini Pro model
- **Real-time Responses**: Get instant answers to your questions

## 📁 Project Structure

```
LLM_QA_Project_TochukwuOkoli_22CG031913/
├── LLM_QA_CLI.py
├── app.py
├── requirements.txt
├── LLM_QA_hosted_webGUI_link.txt
└── README.md
```

## 🔧 Installation & Setup

### 1. Get Your Google Gemini API Key
1. Visit [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
2. Sign in with any Google account (Gmail works fine)
3. Click **"Create API Key"**
4. Click **"Create API key in new project"**
5. Copy the API key and save it securely

**Note**: Gemini API works with ANY Google account - no organization approval needed!

### 2. Local Setup (Optional)

```bash
# Clone the repository
git clone [YOUR_REPO_URL]
cd LLM_QA_Project_TochukwuOkoli_22CG031913

# Install dependencies
pip install -r requirements.txt

# Set environment variable (optional)
export GEMINI_API_KEY="your_api_key_here"
```

### 3. Running the CLI Application

```bash
python LLM_QA_CLI.py
```

Enter your API key when prompted (if not set as environment variable).

### 4. Running the Web GUI Locally

```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

## 🌐 Direct Deployment (No Local Testing Required)

### Step-by-Step Deployment:

#### **Step 1: Create GitHub Repository**
1. Go to [github.com](https://github.com) and sign in
2. Click the **"+"** icon (top right) → **"New repository"**
3. Repository name: `LLM_QA_Project_TochukwuOkoli_22CG031913`
4. Select **Public**
5. Check **"Add a README file"**
6. Click **"Create repository"**

#### **Step 2: Upload Files to GitHub**
1. In your repository, click **"Add file"** → **"Upload files"**
2. Download all project files from the artifacts
3. Drag and drop these files:
   - `LLM_QA_CLI.py`
   - `app.py`
   - `requirements.txt`
   - `LLM_QA_hosted_webGUI_link.txt`
4. Add commit message: "Initial project upload"
5. Click **"Commit changes"**

#### **Step 3: Deploy to Streamlit Cloud**
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click **"Sign in with GitHub"**
3. Authorize Streamlit to access your repositories
4. Click **"New app"** (or **"Create app"**)
5. Configure deployment:
   - **Repository**: `LLM_QA_Project_TochukwuOkoli_22CG031913`
   - **Branch**: `main`
   - **Main file path**: `app.py`
6. Click **"Advanced settings"**
7. In the **Secrets** section, add:
   ```
   GEMINI_API_KEY = "your_actual_gemini_api_key_here"
   ```
   (Replace with your actual Gemini API key)
8. Click **"Deploy"**
9. Wait 2-3 minutes for deployment to complete

#### **Step 4: Update Link File**
1. Once deployed, copy your app URL (e.g., `https://yourapp.streamlit.app`)
2. Go back to your GitHub repository
3. Click on `LLM_QA_hosted_webGUI_link.txt`
4. Click the **pencil icon** (Edit this file)
5. Update with your actual URLs:
   ```
   Name: Tochukwu Okoli
   Matric Number: 22CG031913
   Live URL: https://yourapp.streamlit.app
   GitHub Repository: https://github.com/yourusername/LLM_QA_Project_TochukwuOkoli_22CG031913
   ```
6. Click **"Commit changes"**

#### **Step 5: Download & Submit**
1. On your GitHub repository main page, click the green **"Code"** button
2. Click **"Download ZIP"**
3. Extract the ZIP file
4. Upload the extracted folder to Scorac.com

## 💡 Usage Examples

### CLI Example:
```
Your question: What is artificial intelligence?

Processed question: what is artificial intelligence
Tokens: ['what', 'is', 'artificial', 'intelligence']

Querying LLM...

============================================================
ANSWER:
============================================================
Artificial Intelligence (AI) refers to the simulation of 
human intelligence in machines that are programmed to think
and learn like humans...
============================================================
```

### Web GUI:
1. Enter your Gemini API key in the sidebar
2. Type your question in the input field
3. Click "Get Answer"
4. View preprocessing details and the AI-generated answer

## 🛠️ Technologies Used

- **Python 3.8+**
- **Streamlit**: Web framework for the GUI
- **Google Gemini API**: LLM provider (Gemini Pro model)
- **NLP Preprocessing**: Text processing techniques

## 📝 Preprocessing Steps

The system applies three preprocessing steps to each question:

1. **Lowercasing**: Converts all text to lowercase for consistency
2. **Punctuation Removal**: Removes special characters and punctuation
3. **Tokenization**: Splits text into individual words/tokens

## 🔒 Security Notes

- Never commit API keys directly to GitHub
- Always use environment variables or Streamlit secrets
- Keep your API key confidential
- Do not share your API key in public forums or chat

## ⚡ Why Google Gemini?

- **No organization approval**: Works with any Google account
- **Completely free**: Generous free tier with no credit card required
- **Fast and reliable**: Google's latest AI technology
- **Easy setup**: Get API key in under 1 minute
- **High quality**: Advanced language understanding

## 📊 Project Requirements Met

✅ **Part A**: Python CLI application with preprocessing and LLM integration  
✅ **Part B**: Web GUI with Streamlit  
✅ **Part C**: Deployed on Streamlit Cloud  
✅ **Part D**: GitHub repository with proper structure  

## 🎯 Submission Checklist

- [ ] Google Gemini API key obtained
- [ ] GitHub repository created with correct name
- [ ] All 4 files uploaded to GitHub
- [ ] App successfully deployed on Streamlit Cloud
- [ ] `LLM_QA_hosted_webGUI_link.txt` updated with live URLs
- [ ] Project folder downloaded as ZIP
- [ ] ZIP file submitted to Scorac.com before deadline

## 📧 Contact

**Tochukwu Okoli**  
Matric Number: 22CG031913  
Covenant University  
CSC415/CSC331 - Computational Science and Numerical Methods

## 📄 License

This project is created for academic purposes as part of CSC415/CSC331 coursework.

## 🆘 Troubleshooting

**Problem**: API key not working  
**Solution**: Make sure you copied the entire key from Google AI Studio

**Problem**: Streamlit deployment fails  
**Solution**: Check that `requirements.txt` is uploaded and secrets are properly configured

**Problem**: App shows error when asking questions  
**Solution**: Verify your API key is correctly added in Streamlit secrets section

---

**Submission Deadline**: Friday, November 12, 2025, 12:00 PM  
**Course**: Computational Science and Numerical Methods  
**Institution**: Covenant University  
**Semester**: Alpha 2024/2025
