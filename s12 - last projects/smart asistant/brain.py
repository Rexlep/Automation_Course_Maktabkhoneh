from transformers import pipeline

print("Loading model... please wait.")
classifier = pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment",
    low_cpu_mem_usage=True
)


def analyze_ticket(text):

    max_len = 400
    chunks = [text[i:i+max_len] for i in range(0, len(text), max_len)]

    results = []
    for chunk in chunks:
        r = classifier(chunk, truncation=True)[0]
        results.append(r['label'])

    final_label = max(set(results), key=results.count)

    mapping = {
        '1 star': "CRITICAL (خیلی عصبانی)",
        '2 stars': "CRITICAL (عصبانی)",
        '3 stars': "NEUTRAL (معمولی)",
        '4 stars': "POSITIVE (رضایت‌بخش)",
        '5 stars': "POSITIVE (رضایت‌بخش)"
    }

    return mapping.get(final_label, "UNKNOWN")
