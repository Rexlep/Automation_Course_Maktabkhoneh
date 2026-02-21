from transformers import pipeline

# Using a very small and fast model for classification (Approx 40-80 MB)
classifier = pipeline("zero-shot-classification", model="typeform/distilbert-base-uncased-mnli")

# Using a tiny model for summarization (Approx 120 MB)
summarizer = pipeline("summarization", model="t5-small")


def process_content(text):
    # Categorize
    labels = ["Work", "Personal", "Education", "Finance"]
    category_result = classifier(text, candidate_labels=labels)
    category = category_result['labels'][0]

    # Summarize
    # T5 model requires "summarize: " prefix
    summary_result = summarizer("summarize: " + text[:512], max_length=30, min_length=10)
    summary = summary_result[0]['summary_text']

    return category, summary