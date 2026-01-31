from langchain_huggingface import HuggingFacePipeline
from transformers import pipeline

print("Loading instruction-tuned model...")

pipe = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_new_tokens=100
)

llm = HuggingFacePipeline(pipeline=pipe)

while True:
    query = input("You: ")
    if query.lower() in ["exit", "quit"]:
        break

    response = llm.invoke(query)
    print("Bot:", response)
