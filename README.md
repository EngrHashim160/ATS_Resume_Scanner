# 🧾 ATS Resume Scanner using Gemini Pro

This project is an AI-powered **resume evaluation tool** built with **Streamlit** and **Google Gemini Pro**. It allows job seekers or recruiters to upload resumes and compare them against a given job description. The app intelligently evaluates alignment and generates both feedback and match percentage — just like a real ATS!

---

## 🚀 Features

- 📤 Upload resume in PDF format
- 🧠 Gemini Pro evaluates resume content
- 📈 Get a professional review of strengths and weaknesses
- 🎯 Get a percentage match score with missing keyword suggestions
- 🤖 Built with Google's Gemini 2.5 Pro via `google.generativeai`

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

Create a `.env` file in the root folder and add your Google API key:

```env
GOOGLE_API_KEY=your_google_api_key
```

---

## 🧪 Usage

```bash
streamlit run app.py
```

Then:
- Enter your **job description**
- Upload your **resume (PDF)**
- Click “Tell me about the Resume” or “Percentage Match”

---

## 📂 Project Structure

```
ats-resume-scanner-gemini/
├── app.py               # Main Streamlit app
├── requirements.txt     # Dependencies
└── .env                 # Your API Key (excluded from Git)
```

---

## 🖼 Sample Outputs

- ✅ Resume feedback like a hiring manager
- 📊 Match % score with missing keyword summary

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🙌 Acknowledgements

- [Google Generative AI](https://ai.google.dev)
- [Streamlit](https://streamlit.io)
- [pdf2image](https://github.com/Belval/pdf2image)

---

## 🤝 Contributions

Feel free to fork the repo, raise issues, or submit pull requests to improve the project!