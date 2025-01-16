from openai import OpenAI


client = OpenAI(
    api_key="=============",
)

completion = client.chat.completions.create(
    model = "gpt - 3.5-turbo",
    messages=[
        {
            "role": "system" , "content":"You are a virtual assistant named kayra skilled in general tasks like alexa and google cloud"},
        { "role" : "user" , "content": "what is ozone layer"   }     
        
    ]
)

print(completion.choices[0].message.content)