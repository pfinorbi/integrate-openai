import os
from dotenv import load_dotenv

from openai import OpenAI


def main(): 
        
    try: 
    
        # Get configuration settings 
        load_dotenv()
        openai_key = os.getenv("OPENAI_KEY")
        openai_model = os.getenv("OPENAI_MODEL")
        
        # Read text from file
        text = open(file="./text-files/sample-text.txt", encoding="utf8").read()
        
        print("\nSending request for summary to Azure OpenAI endpoint...\n\n")
        
        # Initialize the OpenAI client
        client = OpenAI(
            api_key = openai_key
        )

        # Send request to OpenAI model
        response = client.chat.completions.create(
            model=openai_model,
            temperature=1,
            max_tokens=120,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Summarize the following text in 20 words or less:\n" + text}
            ]
        )
        
        print("Summary: " + response.choices[0].message.content + "\n")

    except Exception as ex:
        print(ex)

if __name__ == '__main__': 
    main()