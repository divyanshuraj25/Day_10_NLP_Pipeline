from preprocessing import PreprocessingModule
from vectorizer import VectorizerModule


class Pipeline:
    """
    End-to-End NLP Pipeline.

    Combines preprocessing and TF-IDF similarity
    into a single reusable system.
    """

    def __init__(self):
        self.preprocessor = PreprocessingModule()
        self.vectorizer = VectorizerModule()
        self.processed_corpus = []

    def fit(self, corpus):
        """
        Prepare and fit the pipeline on a document corpus.

        Parameters:
            corpus (list): List of documents.

        Returns:
            self
        """

        if not corpus:
            raise ValueError("Corpus cannot be empty.")

        # Preprocess every document
        self.processed_corpus = [
            self.preprocessor.transform(document)
            for document in corpus
        ]

        # Fit TF-IDF vectorizer
        self.vectorizer.fit(self.processed_corpus)

        return self

    def run(self, query, corpus=None):
        """
        Search the corpus using a query and return
        ranked documents with similarity scores.

        Parameters:
            query (str): Search query.
            corpus (list): Optional document corpus.

        Returns:
            list: Ranked results.
        """

        if not isinstance(query, str):
            raise TypeError("Query must be a string.")

        if not query.strip():
            raise ValueError("Query cannot be empty.")

        if len(query.strip()) == 1:
            raise ValueError("Query must contain more than one character.")

        # Fit pipeline if a corpus is provided
        if corpus is not None:
            self.fit(corpus)

        if not self.processed_corpus:
            raise ValueError("Pipeline has not been fitted with a corpus.")

        # Preprocess query
        processed_query = self.preprocessor.transform(query)

        # Get similarity scores
        scores = self.vectorizer.transform(processed_query)

        # Rank documents by similarity score
        ranked_indices = scores.argsort()[::-1]

        results = []

        for index in ranked_indices:
            results.append({
                "document": self.processed_corpus[index],
                "score": round(float(scores[index]), 4)
            })

        return results