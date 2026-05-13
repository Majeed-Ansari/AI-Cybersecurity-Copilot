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
# CVE ANALYSIS AGENT
# =========================

def analyze_cve(cve_id):

    prompt = f"""
You are an expert cybersecurity threat intelligence analyst.

Analyze the following CVE vulnerability:

{cve_id}

Provide:
1. Vulnerability explanation
2. Severity level
3. Affected systems
4. Exploitation risks
5. Real-world impact
6. Mitigation recommendations
7. Best security practices

Provide response in professional SOC intelligence format.
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

        return f"❌ CVE Intelligence Error: {str(e)}"