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
            print('\n1: Add comments to my function\n' +
                '2: Write unit tests for my function\n' +
                '3: Fix my Go Fish game\n' +
                '\"quit\" to exit the program\n')
            command = input('Enter a number to select a task:')
            if command == '1':
                file = open(file="./sample-code/function/function.py", encoding="utf8").read()
                prompt = "Add comments to the following function. Return only the commented code.\n---\n" + file
                call_openai_model(prompt, model=openai_model, client=client)
            elif command =='2':
                file = open(file="./sample-code/function/function.py", encoding="utf8").read()
                prompt = "Write four unit tests for the following function.\n---\n" + file
                call_openai_model(prompt, model=openai_model, client=client)
            elif command =='3':
                file = open(file="./sample-code/go-fish/go-fish.py", encoding="utf8").read()
                prompt = "Fix the code below for an app to play Go Fish with the user. Return only the corrected code.\n---\n" + file
                call_openai_model(prompt, model=openai_model, client=client)
            elif command.lower() == 'quit':
                print('Exiting program...')
                break
            else :
                print("Invalid input. Please try again.")

    except Exception as ex:
        print(ex)

def call_openai_model(prompt, model, client):
    # Provide a basic user message, and use the prompt content as the user message
    system_message = "You are a helpful AI assistant that helps programmers write code."
    user_message = prompt

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
        max_tokens=1000
        )
    
    # Print the response to the console, if desired
    if printFullResponse:
        print(response)

    # Write the response to a file
    results_file = open(file="result/app.txt", mode="w", encoding="utf8")
    results_file.write(response.choices[0].message.content)
    print("\nResponse written to result/app.txt\n\n")

if __name__ == '__main__': 
    main()