from openai import openai

client=openai(
    api_key="#####",
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are a virtual assistant named Thing , skilled in genral task like alexa and google cloud"
        },
        {
            "role": "user",
            "content": "Compose a poem that explains the concept of recursion in programming."
        }
    ]
)

print(completion.choices[0].message.content)
