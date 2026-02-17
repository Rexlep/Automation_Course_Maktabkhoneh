from transformers import pipeline

print("Loading model... please wait.")
classifier = pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment",
    low_cpu_mem_usage=True
)


def analyze_ticket(text):
    result = classifier(text)[0]
    label = result['label']

    mapping = {
        '1 star': "CRITICAL (خیلی عصبانی)",
        '2 stars': "CRITICAL (عصبانی)",
        '3 stars': "NEUTRAL (معمولی)",
        '4 stars': "POSITIVE (رضایت‌بخش)",
        '5 stars': "POSITIVE (رضایت‌بخش)"
    }

    return mapping.get(label, "UNKNOWN")

print(analyze_ticket("love"))