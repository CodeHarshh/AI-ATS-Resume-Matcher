
# AI ATS Resume Matcher 🤖

---

## 🚀 About

**AI ATS Resume Matcher** is a smart tool that helps job seekers and recruiters analyze resumes efficiently.
It leverages **Google Gemini AI** to compare resumes against job descriptions and provides:

* ✅ **ATS Match Percentage**
* 💡 **Strengths and Weaknesses** of the resume
* ✏️ **Actionable suggestions** for improvement

Built with **Python**, **Streamlit**, and **React**, it’s perfect for anyone looking to optimize resumes for ATS systems.

---

## ✨ Features

* Upload **PDF resumes** and **job descriptions**
* Get a **concise resume evaluation** in bullet points
* **Interactive ATS Match gauge**
* Clear **improvement suggestions**
* Modern, **user-friendly interface** with Streamlit cards

---

## 🛠 Installation

### 1. Clone the repository

```bash
git clone https://github.com/CodeHarshh/AI-ATS-Resume-Matcher.git
cd AI-ATS-Resume-Matcher
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

* **Windows:**

```bash
venv\Scripts\activate
```

* **Mac/Linux:**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Set up environment variables

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_google_generative_ai_key
```

---

## 🎯 Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

1. Paste the **Job Description** in the left panel
2. Upload the **Resume PDF** in the right panel
3. Click **Resume Review** for a detailed evaluation
4. Click **Percentage Match** to see the ATS match gauge

---

## 🗂 Project Structure

```
AI-ATS-Resume-Matcher/
│
├─ app.py                  # Main Streamlit app
├─ requirements.txt        # Python dependencies
├─ package.json            # Node dependencies
├─ .gitignore              # Git ignore file
├─ README.md               # Project documentation
├─ .env                    # Environment variables (API keys)
└─ temp.py                 # Temporary/test scripts
```

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create your feature branch

```bash
git checkout -b feature/YourFeature
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push to your branch

```bash
git push origin feature/YourFeature
```

5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**.
See [LICENSE](LICENSE) for details.

---

