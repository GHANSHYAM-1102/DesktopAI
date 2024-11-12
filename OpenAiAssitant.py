import os.path   # find thing in your os
from openai import OpenAI   #to take referance from chatgpt

    
    
    
        
def ai(query):
    
    
    query = query.replace("using ai", "")   
    query = query.replace("jarvis", "")
    query = query.replace("ai", "")

    text = f"Jarvis response for query : {query}\n" # write in your o/p 
    # below code is also copied by chatgpt for referaance 
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": query
            },
            {
                "role": "user",
                "content": ""
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    text += response.choices[0].message.content.strip()+"\n"  #dlt spaces and provide proper msg 
    print(text) #print your msg here
    
    # print(response.choices[0].message.content.strip() + "\n")

    if not  os.path.exists("Openai"):
        os.mkdir("Openai")           # generate directory in your file if directory id alreay in your file then it just open this directory

    with open(f"Openai/{query}.txt", "w") as f:
        f.write(text)                          #open your question here 


