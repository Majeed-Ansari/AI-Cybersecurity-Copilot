import os

from dotenv import load_dotenv
from openai import OpenAI

# =========================
# LOAD ENV VARIABLES
# =========================

load_dotenv()

# =========================
# GET NVIDIA API KEY
# =========================

api_key = os.getenv("NVIDIA_API_KEY")

# =========================
# INITIALIZE NVIDIA CLIENT
# =========================

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=api_key
)

# =========================
# AI THREAT ANALYSIS
# =========================

def analyze_threats(log_text):

    if not api_key:
        return "❌ NVIDIA API Key not found. Please check your .env file."

    prompt = f"""
You are an expert cybersecurity SOC analyst.

Analyze the following security logs.

Tasks:
1. Identify suspicious activities
2. Detect attack types
3. Explain threats clearly
4. Suggest mitigation steps
5. Provide overall severity level
6. Summarize findings professionally

Security Logs:
{log_text}

Provide response in this format:

## Threats Detected
## Severity Level
## Attack Analysis
## Mitigation Recommendations
## Final SOC Summary
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
            max_tokens=700
        )

        return response.choices[0].message.content

    except Exception as e:

        return f"❌ Error during AI threat analysis: {str(e)}"