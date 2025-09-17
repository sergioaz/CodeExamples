import os

from openai import OpenAI
os.environ["OPENAI_API_KEY"] = "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"
client = OpenAI()

response = client.responses.create(
    model="gpt-4.1",
    input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)
