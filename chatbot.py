# chatbot.py
def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! I'm RoboZiad. How can I help you today?"
    elif "product" in user_input:
        return "We have a range of AI-based products. Would you like to know more?"
    elif "support" in user_input or "help" in user_input:
        return "Sure! Please describe your issue, and I'll do my best to help."
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day. 👋"
    else:
        return "Sorry, I didn’t understand that. Could you rephrase?"

print("🤖 Welcome! I'm RoboZiad - your assistant chatbot.")
print("Type 'exit' to end the chat.\n")

while True:
    user = input("You: ")
    if user.lower() == "exit":
        print("RoboZiad: Goodbye! 👋")
        break
    response = chatbot_response(user)
    print("RoboZiad:", response)
