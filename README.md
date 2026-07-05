# 🎬 CineSage-AI

AI-powered movie information extraction system built using LangChain, Mistral AI, Flask, HTML, CSS, and JavaScript.

CineSage analyzes movie descriptions and automatically extracts structured information such as genre, themes, plot, characters, scientific concepts, and more.

---

## ✨ Features

- Movie information extraction using LLMs
- Clean and modern web interface
- Automatic structured output generation
- LangChain prompt engineering
- Mistral AI integration
- Flask backend API
- Responsive HTML/CSS/JavaScript frontend

---

## 📌 Information Extracted

The system extracts:

- Movie Name
- Category
- Genre
- Director / Creator
- Cast
- Main Characters
- Themes
- Key Topics
- Scientific Concepts
- Technologies
- Locations
- Important Events
- Story / Plot
- Tone
- Notable Features
- Keywords
- Quick Summary

---

## 🛠️ Tech Stack

**Frontend**
- HTML
- CSS
- JavaScript

**Backend**
- Flask
- Python

**AI / NLP**
- LangChain
- Mistral AI

---

## 📂 Project Structure

```text
CineSage-AI
│
├── CineSage
│   ├── core.py
│   │
│   ├── templates
│   │   └── index.html
│   │
│   └── static
│
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone repository:

```bash
git clone https://github.com/yourusername/CineSage-AI.git
```

Move into project:

```bash
cd CineSage-AI
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env`

```env
MISTRAL_API_KEY=your_api_key
```

Run application:

```bash
python core.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

## 🚀 Example Input

```text
Interstellar is a science fiction movie directed by Christopher Nolan that explores themes of space exploration, survival, love, and time.
```

---

## 📷 Output Example

The model generates structured movie insights including plot, themes, concepts, and summaries.

---

## Future Improvements

- Movie poster integration
- Database storage
- User authentication
- Search history
- Recommendation system
- RAG-based movie retrieval

---

## Author

Aditi Krishna
