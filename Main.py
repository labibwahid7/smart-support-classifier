import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 1. Raw ticket pasted from service desk
ticket = "User cannot log into the sales portal after changing their password. Getting MFA timeout error."

# 2. Send to OpenAI with clear instructions
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "Classify this IT ticket into: 1) Priority (Low/Med/High), 2) Category, and 3) A 1-sentence fix."
        },
        {
            "role": "user",
            "content": ticket
        }
    ]
)

# 3. Print the result
print(response.choices[0].message.content)