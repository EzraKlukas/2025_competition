import requests
from openai import OpenAI

def generateClues():

    URL = "https://phas.ubc.ca/~miti/ENPH353/ENPH353Keys.txt"
    response = requests.get(URL)

    # Inspect the result
    print("Server returned:", repr(response.text))

    # Probably only contains the API key
    API_KEY = response.text.strip()

    client = OpenAI(api_key=API_KEY)

    prompt = """You will generate clues that describe a potential funny crime 
                for your game in random order. 
                The clues must have less than 13 characters. 
                Use themes from planet Earth.
                Display the clues in the following order:
                    NUMBER OF VICTIMS
                    WHO ARE THE VICTIMS
                    WHAT IS THE CRIME
                    WHEN WAS THE CRIME COMMITTED
                    WHERE WAS THE CRIME COMMITTED
                    WHY WAS THE CRIME COMMITED
                    WHAT WEAPON WAS THE CRIME COMMITED WITH
                    WHO WAS THE CRIMINAL
                """

    completion = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a game creator..."},
            {"role": "user", "content": prompt}
        ]
    )

    story = completion.choices[0].message.content
    print(story)

generateClues()
