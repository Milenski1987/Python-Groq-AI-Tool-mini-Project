from tkinter.constants import RAISED
import groq
import tkinter as tk

123

# Initialize Groq API client
client = groq.Client(api_key="")

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

#create GUI
root = tk.Tk()
root.title("AI Chatbot 🤖 powered by Groq")
root.geometry("600x600")


#create input field frame
input_frame = tk.Frame(root,relief=RAISED,borderwidth=3)
input_frame.pack()

#create user input field
def temp_text(e):
    user_input_field.delete(0, tk.END)

user_input_field = tk.Entry(input_frame,  bg="black", fg="white", width=50)
user_input_field.insert(0, "Enter your message to Chatbot here...")
user_input_field.pack(pady=20)
user_input_field.bind("<FocusIn>", temp_text)

#create user input send button
send_button = tk.Button(root, text="Send", foreground="green", command=lambda: get_response_by_chatbot())
send_button.pack()

#create response field frame
response_frame = tk.Frame(root,relief=RAISED, borderwidth=3)
response_frame.pack()

#create chatbot response field
chatbot_response = tk.Text(response_frame,bg="black",fg="yellow", width=150, height=40)
chatbot_response.pack()

def get_response_by_chatbot():
    user_input = user_input_field.get()
    user_input_field.delete(0, tk.END)
    response = get_ai_response(user_input)

    chatbot_response.insert(tk.END,f"User: {user_input}\n\n")
    chatbot_response.insert(tk.END,f"Chatbot: {response}\n\n")


root.mainloop()

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


