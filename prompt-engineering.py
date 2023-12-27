import os
from dotenv import load_dotenv

# Add Azure OpenAI package
from openai import OpenAI

# Set to True to print the full response from OpenAI for each call
printFullResponse = False

def main(): 
        
    try: 
    
        # Get configuration settings 
        load_dotenv()
        openai_key = os.getenv("OPENAI_KEY")
        openai_model = os.getenv("OPENAI_MODEL")
        
        # Configure the Azure OpenAI client
        client = OpenAI(
            api_key = openai_key
        )

        while True:
            print('1: Basic prompt (no prompt engineering)\n' +
                  '2: Prompt with email formatting and basic system message\n' +
                  '3: Prompt with formatting and specifying content\n' +
                  '4: Prompt adjusting system message to be light and use jokes\n' +
                  '\'quit\' to exit the program\n')
            command = input('Enter a number:')
            if command == '1':
                call_openai_model(messages="./prompts/basic.txt", model=openai_model, client=client)
            elif command =='2':
                call_openai_model(messages="./prompts/email-format.txt", model=openai_model, client=client)
            elif command =='3':
                call_openai_model(messages="./prompts/specify-content.txt", model=openai_model, client=client)
            elif command =='4':
                call_openai_model(messages="./prompts/specify-tone.txt", model=openai_model, client=client)
            elif command.lower() == 'quit':
                print('Exiting program...')
                break
            else :
                print("Invalid input. Please try again.")

    except Exception as ex:
        print(ex)

def call_openai_model(messages, model, client):
    # In this sample, each file contains both the system and user messages
    # First, read them into variables, strip whitespace, then build the messages array
    file = open(file=messages, encoding="utf8")
    system_message = file.readline().split(':', 1)[1].strip()
    user_message = file.readline().split(':', 1)[1].strip()

    # Print the messages to the console
    print("System message: " + system_message)
    print("User message: " + user_message)

    # Format and send the request to the model
    messages =[
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message},
        ]
    
    # Call the OpenAI model
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.7,
        max_tokens=800
        )
    
    if printFullResponse:
        print(response)

    print("Completion: \n\n" + response.choices[0].message.content + "\n")

if __name__ == '__main__': 
    main()