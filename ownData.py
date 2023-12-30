import os
from dotenv import load_dotenv

# Add OpenAI import
from openai import OpenAI


def main(): 
        
    try:     
        # Get configuration settings 
        load_dotenv()
        openai_key = os.getenv("OPENAI_KEY")
        openai_model = os.getenv("OPENAI_MODEL")
        openai_assistant_id = os.getenv("OPENAI_ASSISTANT_ID")
        
        # Initialize the OpenAI client
        client = OpenAI(
            api_key=openai_key
        )

        # Get the prompt
        text = input('\nEnter a question:\n')

        # Retrieve assistant
        assistant = client.beta.assistants.retrieve(openai_assistant_id)

        # Create a thread that represents a conversation
        thread = client.beta.threads.create()

        # Add the message to the thread
        message = client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=text
        )

        # Send request to OpenAI model
        print("\n...Sending the following request to OpenAI endpoint...")
        print("Request: " + text + "\n")

        # Run the assistant
        run = client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=assistant.id
        )

        # Check run status
        run_completed = False

        while(run_completed != True):
            run = client.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id
            )

            if(run.status == "completed"):
                run_completed = True
        
        # Get Assistant's response
        messages = client.beta.threads.messages.list(
            thread_id=thread.id
        )

        # Print response
        print("Response:\n" + messages.data[0].content[0].text.value + "\n")
        
    except Exception as ex:
        print(ex)


if __name__ == '__main__': 
    main()

