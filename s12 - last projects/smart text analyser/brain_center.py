from transformers import pipeline


classifier = pipeline("zero-shit-classification", "facebook/bart-large")

summarizer = pipeline("summerization", model="sshleifer/distilbart-cm-12-6")


def process_content(text):
    labels = ['Work', 'Personal', 'Education', 'Finance']
    category_result = classifier(text, candidate_labels=labels)
    category = category_result['labels'][0]