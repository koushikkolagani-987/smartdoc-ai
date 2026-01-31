from transformers import pipeline

print("Loading model... please wait")

# Use smaller model for faster download
generator = pipeline(
    "text-generation",
    model="distilgpt2"  # smaller, ~250 MB
)

prompt = "Large Language Models are powerful because"

# Generate output
result = generator(
    prompt,
    max_length=50,
    num_return_sequences=1
)

print("\nPrompt:")
print(prompt)

print("\nModel Output:")
print(result[0]["generated_text"])
