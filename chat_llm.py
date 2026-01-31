from transformers import pipeline

print("Loading model... please wait")

chatbot = pipeline(
    "text-generation",
    model="gpt2",
    max_new_tokens=100
)

print("Chatbot ready! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bye 👋")
        break

    response = chatbot(user_input)
    print("Bot:", response[0]["generated_text"])
