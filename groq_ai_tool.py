import groq


# Initialize Groq API client
my_api_key = "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"
client = groq.Client(api_key=my_api_key)

# Function to get AI response from Groq API
def get_ai_response(current_user_input: str) -> str:
    try:
        current_response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": current_user_input}]
        )
        return current_response.choices[0].message.content  # Corrected access
    except Exception as e:
        return f"Error: {e}"


# Main loop for user input
if __name__ == "__main__":
    print("Welcome to your AI chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            print("\nGoodbye! 👋")
            break
        response = get_ai_response(user_input)
        print("AI:", response)

        # Allow the user to save conversation in file
        save_file_prompt = input("Do you want to save the conversation to a file?")
        if save_file_prompt.lower() == "yes":
            with open("ai_conversation.txt", "a") as file:
                file.write(f"You: {user_input}\n")
                file.write(f"AI: {response}\n")

            print("Conversation successfully added to Python file")
