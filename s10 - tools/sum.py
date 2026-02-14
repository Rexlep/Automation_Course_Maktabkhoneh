from transformers import pipelines

summerize = pipelines("text-generator", model="facebook/bart-large-cnn")

text = "Hello my name is amir i love programming very very very much and i adore python with ai models"
print(summerize(text, max_length=50))