# This file is for testing and loading model
from llama_cpp import Llama

llm = Llama.from_pretrained(
    repo_id="BioMistral/BioMistral-7B-GGUF",
    filename="ggml-model-Q2_K.gguf",
	verbose=False   # 👈 Suppresses internal logs
)

print("Here-----")

response = llm.create_chat_completion(
    messages = [
        {
            "role": "user",
            "content": "What is the capital of France?"
        }
    ]
)

print(response)

# Print only the assistant's reply
# print(response["choices"][0]["message"]["content"])



