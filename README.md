#  AI Resume Analyzer

AI Resume Analyzer is an NLP-based application that compares a candidate's resume with a job description and provides a resume-job match score, matched skills, missing skills, and improvement suggestions.

##  Objective

The objective of this project is to help students and job seekers understand how relevant their resume is to a particular job role.

##  Features

- Upload resume in PDF format
- Enter or paste a job description
- Extract text from resume
- Calculate resume-job similarity score
- Identify matched skills
- Identify missing skills
- Provide resume improvement suggestions
- Simple and user-friendly interface

##  Technologies Used

- Python
- Streamlit
- Natural Language Processing
- TF-IDF Vectorization
- Cosine Similarity
- PyPDF2
- Scikit-learn

##  Methodology

1. User uploads a resume in PDF format.
2. Text is extracted from the resume.
3. Resume text and job description are cleaned.
4. TF-IDF converts text into numerical vectors.
5. Cosine Similarity calculates the similarity between the resume and job description.
6. Skills are extracted and compared.
7. The system displays the match score and suggestions.

## Project Architecture

```text
User
  ↓
Resume PDF + Job Description
  ↓
PDF Text Extraction
  ↓
Text Preprocessing
  ↓
TF-IDF Vectorization
  ↓
Cosine Similarity
  ↓
Match Score + Skills Analysis
  ↓
Improvement Suggestions
```

##  How to Run

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

##  Expected Output

The application displays:

- Resume-job match percentage
- Matched skills
- Missing skills
- Resume improvement suggestions

##  Future Scope

- Support for DOCX resumes
- Advanced AI-based skill extraction
- Resume formatting analysis
- Job recommendation system
- Integration with online job portals
- Use of transformer-based NLP models

##  Developed By

Vanshika Dadhich  
Integrated M.Tech in Artificial Intelligence  
VIT Bhopal University

##  References

- Python Documentation
- Streamlit Documentation
- Scikit-learn Documentation
- PyPDF2 Documentation
