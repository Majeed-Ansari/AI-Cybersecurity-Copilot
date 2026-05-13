import os

from dotenv import load_dotenv
from openai import OpenAI

# =========================
# LOAD ENV VARIABLES
# =========================

load_dotenv()

api_key = os.getenv("NVIDIA_API_KEY")

# =========================
# NVIDIA CLIENT
# =========================

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=api_key
)

# =========================
# MITIGATION AGENT
# =========================

def generate_mitigation(log_text):

    prompt = f"""
You are a cybersecurity mitigation expert.

Analyze the security logs below and provide:

1. Immediate mitigation steps
2. Long-term security recommendations
3. Best practices to prevent future attacks
4. Network protection recommendations

Security Logs:
{log_text}

Provide response in professional cybersecurity format.
"""

    try:

        response = client.chat.completions.create(
            model="meta/llama-3.1-70b-instruct",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3,
            max_tokens=600
        )

        return response.choices[0].message.content

    except Exception as e:

        return f"❌ Mitigation Agent Error: {str(e)}"