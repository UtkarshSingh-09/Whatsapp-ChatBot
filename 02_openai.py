from openai import OpenAI
client = OpenAI(api_key="enter your API key")
command='''


'''
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a person name Utkarsh who speaks english as well as hindi he is from india and he is a coder . you analyse chat history and response like Utkarsh"},
        {
            "role": "user",
            "content": command
        }
    ]
)

print(completion.choices[0].message)