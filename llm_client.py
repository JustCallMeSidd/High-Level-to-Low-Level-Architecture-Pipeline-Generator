import streamlit as st
from openai import OpenAI

# Load values from Streamlit secrets
client = OpenAI(
    base_url=st.secrets["OPENROUTER_BASE_URL"],
    api_key=st.secrets["OPENROUTER_API_KEY"],
)

MODEL_NAME = st.secrets.get("MODEL_NAME", "google/gemini-3-flash-preview")  # default if not set

def generate_architecture(prompt):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "user", "content": prompt}
        ],
        extra_body={
            "reasoning": {"enabled": True}
        }
    )

    return response.choices[0].message.content
