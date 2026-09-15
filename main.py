from pipeline import Pipeline


# 15-document corpus
corpus = [
    "Python is a popular programming language used for data science.",
    "Machine learning allows computers to learn from data.",
    "Natural language processing helps computers understand human language.",
    "Deep learning uses neural networks to solve complex problems.",
    "Artificial intelligence enables machines to perform intelligent tasks.",
    "Python is widely used for machine learning and artificial intelligence.",
    "Text preprocessing removes unwanted words and symbols from text.",
    "TF-IDF converts text documents into numerical vectors.",
    "Cosine similarity measures similarity between two text vectors.",
    "Data science combines statistics programming and machine learning.",
    "Neural networks are inspired by the human brain.",
    "NLP is used in chatbots translation and sentiment analysis.",
    "Machine learning models require training data to make predictions.",
    "Search engines use text similarity to find relevant documents.",
    "Python libraries such as NLTK and scikit-learn support NLP projects."
]


# Create pipeline
pipeline = Pipeline()

# Fit pipeline
pipeline.fit(corpus)


# Five different queries
queries = [
    "Python programming",
    "machine learning",
    "natural language processing",
    "text similarity",
    "artificial intelligence"
]


# Run five queries
for query in queries:

    print("\n" + "=" * 60)
    print("QUERY:", query)
    print("=" * 60)

    results = pipeline.run(query)

    for rank, result in enumerate(results, start=1):
        print(
            f"{rank}. Score: {result['score']:.4f} | "
            f"{result['document']}"
        )


# Edge case testing
print("\n" + "=" * 60)
print("EDGE CASE TESTING")
print("=" * 60)


edge_cases = [
    "",
    "a",
    "12345!!!"
]


for query in edge_cases:

    try:
        print(f"\nTesting query: {repr(query)}")
        results = pipeline.run(query)

        for result in results[:3]:
            print(result)

    except Exception as e:
        print("Handled Error:", e)