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
# INCIDENT REPORT AGENT
# =========================

def generate_incident_report(log_text):

    prompt = f"""
You are a SOC incident response analyst.

Generate a professional incident report based on the following security logs.

Include:
1. Executive Summary
2. Threat Overview
3. Affected Systems
4. Risk Level
5. Incident Timeline
6. Recommendations
7. Final Conclusion

Security Logs:
{log_text}

Generate a detailed SOC-style incident report.
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

        return f"❌ Incident Agent Error: {str(e)}"