from groq import Groq
def generate_response(prompt):
    client = Groq(api_key="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")
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0,
        max_tokens=150,
        top_p=1,
        stream=True,
        stop=None,
    )
    response=" "

    for chunk in completion:
        response+=(chunk.choices[0].delta.content or "")
    return response