# Day 10 – NLP Pipeline 🔍

A beginner-friendly Natural Language Processing (NLP) pipeline built using Python. This project preprocesses text, converts documents into numerical vectors using TF-IDF, and ranks documents according to their similarity with a user query using Cosine Similarity.

## 📌 Project Overview

The NLP Pipeline is designed to find relevant documents based on a given search query.

For example, when the user enters **"artificial intelligence"**, the pipeline analyzes the available documents and returns the most relevant documents along with their similarity scores.

This project demonstrates the basic working of a text-based search and document-ranking system.

## 🚀 Features

* Text preprocessing and cleaning.
* Conversion of text into numerical vectors using TF-IDF.
* Document ranking using Cosine Similarity.
* Search for relevant documents using natural-language queries.
* Similarity scores for each ranked document.
* Edge-case testing for invalid queries.
* Modular Python code with separate files for different tasks.

## 🛠️ Technologies Used

* **Python**
* **Natural Language Processing (NLP)**
* **TF-IDF (Term Frequency–Inverse Document Frequency)**
* **Cosine Similarity**
* **Regular Expressions**
* **Object-Oriented Programming**
* **VS Code**

## 📂 Project Structure

```text
Day_10_NLP_Pipeline/
│
├── main.py
├── pipeline.py
├── preprocessing.py
├── vectorizer.py
├── README.md
└── __pycache__/
```

### 📄 File Descriptions

| File               | Description                                                       |
| ------------------ | ----------------------------------------------------------------- |
| `main.py`          | Runs the pipeline and tests different queries.                    |
| `pipeline.py`      | Coordinates preprocessing, vectorization and ranking.             |
| `preprocessing.py` | Cleans and prepares text for processing.                          |
| `vectorizer.py`    | Converts documents into TF-IDF vectors and calculates similarity. |
| `README.md`        | Project documentation.                                            |

## ⚙️ How the Pipeline Works

```text
User Query
    ↓
Text Preprocessing
    ↓
TF-IDF Vectorization
    ↓
Cosine Similarity Calculation
    ↓
Document Ranking
    ↓
Relevant Search Results
```

### 1. Text Preprocessing

The input text is cleaned by performing operations such as:

* Converting text to lowercase.
* Removing unnecessary characters.
* Removing extra spaces.
* Preparing the text for vectorization.

### 2. TF-IDF Vectorization

TF-IDF converts text into numerical vectors.

It assigns importance to words based on how frequently they appear in a document and how common they are across the collection of documents.

### 3. Cosine Similarity

Cosine Similarity measures how similar two text vectors are.

A higher score generally indicates greater similarity between the query and a document.

The formula is:

```text
Cosine Similarity =
(A · B) / (||A|| × ||B||)
```

### 4. Document Ranking

The documents are sorted according to their similarity scores. The most relevant documents appear at the top of the results.

## ▶️ How to Run the Project

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

### Step 2: Open the Project Folder

```bash
cd Day_10_NLP_Pipeline
```

### Step 3: Install Required Library

If your code uses scikit-learn, install it with:

```bash
pip install scikit-learn
```

> Install any additional libraries required by your Python files.

### Step 4: Run the Program

```bash
python main.py
```

## 🧪 Example Output

The pipeline can produce results similar to the following:

```text
============================================================
QUERY: artificial intelligence
============================================================

1. Score: 0.5766 | python widely used machine learning artificial intelligence
2. Score: 0.5046 | artificial intelligence enables machine perform intelligent task
3. Score: 0.0000 | python library nltk scikit learn support nlp project
4. Score: 0.0000 | nlp used chatbots translation sentiment analysis
5. Score: 0.0000 | neural network inspired human brain
6. Score: 0.0000 | search engine use text similarity find relevant document
```

**Note:** Similarity scores may vary depending on the documents, preprocessing method and TF-IDF configuration used in the program.

## 🧩 Edge-Case Testing

The project also tests invalid queries, including:

| Input                    | Expected Behavior                                               |
| ------------------------ | --------------------------------------------------------------- |
| Empty query              | Displays an error because the query is empty.                   |
| One-character query      | Displays an error because the query is too short.               |
| Only numbers and symbols | Displays an error if preprocessing removes all meaningful text. |

Example:

```text
Testing query: ''

Handled Error: Query cannot be empty.

Testing query: 'a'

Handled Error: Query must contain more than one character.

Testing query: '12345!!!'

Handled Error: Query cannot be empty.
```

## 🎯 Learning Outcomes

Through this project, I learned:

* The fundamentals of Natural Language Processing.
* How text preprocessing works.
* How TF-IDF represents text numerically.
* How Cosine Similarity measures document similarity.
* How to build a basic document-ranking pipeline.
* How to handle invalid inputs and edge cases.
* How to organize a Python project into multiple modules.

## 🔮 Future Improvements

* Add a web interface using Flask or Streamlit.
* Allow users to upload their own documents.
* Support larger document collections.
* Improve text preprocessing using advanced NLP techniques.
* Add a graphical display of similarity scores.
* Deploy the application online.

## 👨‍💻 Author

**Divyanshu Raj**

B.Tech CSE (AI & ML) Student

This project is part of my **60 Days Python / AI-ML Learning Challenge**.

## ⭐ Acknowledgement

This project was created as part of my continuous learning journey in Python, Natural Language Processing and Artificial Intelligence.

If you find this project useful, consider giving the repository a star ⭐.
