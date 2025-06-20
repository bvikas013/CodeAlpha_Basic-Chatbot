def chatbot():
    print("🤖 Hello! I'm ChatBot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hello", "hi", "hey"]:
            print("Bot: Hello there!")
        elif user_input in ["how are you", "how are you doing"]:
            print("Bot: I'm doing great, thanks for asking!")
        elif user_input in ["what's your name", "who are you"]:
            print("Bot: I'm a simple chatbot created to talk with you.")
        elif user_input in ["what can you do", "help"]:
            print("Bot: I can chat with you using predefined replies!")
        elif user_input in ["thank you", "thanks"]:
            print("Bot: You're welcome!")
        elif user_input in ["bye", "goodbye", "see you"]:
            print("Bot: Goodbye! Have a great day!")
            break
        else:
            print("Bot: I'm not sure how to respond to that.")

chatbot()
