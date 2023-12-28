import requests
import time
import os
from dotenv import load_dotenv

def main(): 
        
    try:
        # Get OpenAI Service settings
        load_dotenv()
        api_key = os.getenv("OPENAI_KEY")
        api_base = "https://api.openai.com/"
        api_version = "v1"
        
        # Get prompt for image to be generated
        prompt = input("\nEnter a prompt to request an image: ")

        # Make the call to request the image
        url = "{}{}/images/generations".format(api_base, api_version)
        headers= { "Authorization": "Bearer {}".format(api_key), "Content-Type": "application/json" }
        
        body = {
            "model" : "dall-e-3",
            "prompt": prompt,
            "n": 1,
            "size": "1024x1024"
        }

        response = requests.post(url=url, headers=headers, json=body)

        # Get the results
        image_url = response.json()['data'][0]['url']

        # Display the URL for the generated image
        print(image_url)
        

    except Exception as ex:
        print(ex)

if __name__ == '__main__': 
    main()

