# 🧾 ATS Resume Scanner using Gemini Pro

An upgraded AI-powered resume evaluation tool that uses **Google Gemini Pro** and **Streamlit** to analyze a candidate's resume against a given job description (JD). It returns a structured response in JSON format, including JD match percentage, missing keywords, and a profile summary.

---

## 🚀 Features

- 📤 Upload resume in PDF format
- 📄 Paste the job description
- ⚖️ Gemini Pro evaluates resume and JD
- ✅ Returns structured feedback in this format:

```json
{
  "JD Match": "85%",
  "MissingKeywords": ["Python", "SQL"],
  "Profile Summary": "The candidate has strong frontend skills but lacks backend experience."
}
```

- 🤖 Powered by Gemini Pro 2.5 (via `google.generativeai`)

---

## 🛠️ Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/ats-resume-scanner-gemini.git
cd ats-resume-scanner-gemini
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Setup

Create a `.env` file in the root directory and add your Google API key:

```env
GOOGLE_API_KEY=your_google_api_key
```

---

## 🧪 Usage

```bash
streamlit run app.py
```

Then:
- Paste a job description
- Upload your resume (PDF)
- Click **Submit**
- Get JD Match %, missing keywords, and a profile summary

---

## 📂 Project Structure

```
ats-resume-scanner-gemini/
├── app.py               # Streamlit app
├── requirements.txt     # Python dependencies
└── .env                 # API key file (not tracked)
```

---

## 💡 Sample Use Case

✅ Paste a Data Scientist JD  
📤 Upload your resume  
🎯 Get back Gemini's intelligent review and score

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🙌 Acknowledgements

- [Google Generative AI](https://ai.google.dev)
- [Streamlit](https://streamlit.io)
- [PyPDF2](https://pypi.org/project/PyPDF2/)

---

## 🤝 Contributions

PRs and feedback are always welcome! Let's make AI-powered job prep accessible for everyone.