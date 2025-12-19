import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url=os.getenv("OPENROUTER_BASE_URL"),
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

def generate_architecture(prompt):
    response = client.chat.completions.create(
        model=os.getenv("MODEL_NAME"),
        messages=[
            {"role": "user", "content": prompt}
        ],
        extra_body={
            "reasoning": {"enabled": True}
        }
    )

    return response.choices[0].message.content
