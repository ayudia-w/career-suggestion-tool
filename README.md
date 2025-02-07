# Career Suggestion Tool

## 📌 Overview
**🚨 Disclaimer:** The dataset here is a work in progress, I'm still working on importing datasets. Constructive feedback is welcome! 😃

The **Career Suggestion Tool** is a Python-based project that provides personalized career recommendations based on user inputs such as **personality traits, MBTI type, interests, work experience, education, and skills**. The tool uses a structured dataset to suggest careers that best match the user's profile.

## 🔥 Features
- Provides **top 3 career suggestions** based on multiple user inputs.
- Uses a **custom career knowledge base** (`career-knowledge.json`) with predefined career details.
- Takes into account **MBTI, interests, education, experience, and skills** for better matching.
- Designed for **beginners interested in AI/ML-powered career guidance**.
- Now supports **Streamlit** for an interactive web-based experience!

## 🛠️ Installation & Setup
1. **Clone the repository**:
   ```bash
   git clone https://github.com/YOUR-USERNAME/career-suggestion-tool.git
   cd career-suggestion-tool
   ```
2. **Install required libraries**:
   ```bash
   pip install pandas streamlit
   ```
3. **Run the tool**:
   ```bash
   streamlit run career-suggest.py
   ```

## 📂 Project Structure
```
career-suggestion-tool/
│-- career-suggest.py       # Main script for career suggestions (Streamlit-based UI)
│-- input-career.py         # User input handling script
│-- career-knowledge.json   # Career knowledge base
│-- README.md               # Project documentation
```

## 🎯 Usage
1. Run the **Streamlit** app using `streamlit run career-suggest.py`.
2. Enter your **personality traits, MBTI, interests, experience, education, and skills**.
3. The tool will analyze the input and return the **top 3 career recommendations** interactively.

## 📝 Future Enhancements
- 🔹 Expand the career knowledge base for more diverse career recommendations.
- 🔹 Implement **machine learning** to improve career matching dynamically.
- 🔹 Further enhance the **web-based version** with better UI/UX.

## 🤝 Contributing
Contributions are welcome! Feel free to **fork** this repository, create a **new branch**, and submit a **pull request**.

## 📜 License
This project is open-source under the **MIT License**.

---
🚀 **Happy Coding & Career Matching!**
