from openai import OpenAI

# اینجا توکن Gemini API خودت رو بذار
GEMINI_API_KEY = "AIzaSyBgW8GH7LmY9MrQvMd5wC_zcQhqHjRfJyw"

client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

print("Gemini Chatbot (type 'exit' to quit)")

history = [
    {"role": "system", "content": "You are a helpful assistant."}
]

while True:
    user = input("You: ")
    if user.lower() == "exit":
        break

    history.append({"role": "user", "content": user})

    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=history
    )

    answer = response.choices[0].message.content
    print("Bot:", answer)

    history.append({"role": "assistant", "content": answer})
