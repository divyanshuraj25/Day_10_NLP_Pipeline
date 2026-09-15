from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class VectorizerModule:
    """
    TF-IDF vectorization and cosine similarity module.
    """

    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.corpus_vectors = None

    def fit(self, corpus):
        """
        Fit the TF-IDF vectorizer on the document corpus.

        Parameters:
            corpus (list): List of documents.

        Returns:
            self
        """

        if not corpus:
            raise ValueError("Corpus cannot be empty.")

        self.corpus_vectors = self.vectorizer.fit_transform(corpus)

        return self

    def transform(self, query):
        """
        Transform a query into the same TF-IDF space.

        Parameters:
            query (str): User search query.

        Returns:
            array: Cosine similarity scores with corpus documents.
        """

        if not isinstance(query, str):
            raise TypeError("Query must be a string.")

        if not query.strip():
            raise ValueError("Query cannot be empty.")

        if self.corpus_vectors is None:
            raise ValueError("Vectorizer must be fitted before transformation.")

        query_vector = self.vectorizer.transform([query])

        scores = cosine_similarity(
            query_vector,
            self.corpus_vectors
        )[0]

        return scores