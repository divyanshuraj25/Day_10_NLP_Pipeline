import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


class PreprocessingModule:
    """
    Text preprocessing module.

    Performs:
    - Lowercasing
    - Removing numbers and special characters
    - Tokenization
    - Stopword removal
    - Lemmatization
    """

    def __init__(self):
        self.stop_words = set(stopwords.words("english"))
        self.lemmatizer = WordNetLemmatizer()

    def transform(self, text):
        """
        Preprocess a given text.

        Parameters:
            text (str): Raw input text.

        Returns:
            str: Cleaned and normalized text.
        """

        if not isinstance(text, str):
            raise TypeError("Input must be a string.")

        if not text.strip():
            raise ValueError("Input text cannot be empty.")

        # Lowercase
        text = text.lower()

        # Keep only alphabets and spaces
        text = re.sub(r"[^a-zA-Z\s]", " ", text)

        # Tokenization
        tokens = nltk.word_tokenize(text)

        # Remove stopwords and single-character tokens
        tokens = [
            word for word in tokens
            if word not in self.stop_words and len(word) > 1
        ]

        # Lemmatization
        tokens = [
            self.lemmatizer.lemmatize(word)
            for word in tokens
        ]

        return " ".join(tokens)