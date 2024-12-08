def display_options():
    print("\nAvailable options:")
    print("1. Hello")
    print("2. How are you?")
    print("3. What's your name?")
    print("4. What can you do?")
    print("5. What is your age?")
    print("6. Goodbye")
    print("Please enter the number or type your own message.\n")

def get_response(user_input):
    # Handle numeric options
    if user_input.isdigit():
        option = int(user_input)
        if option == 1:
            return "Hello! How can I help you today?"
        elif option == 2:
            return "I'm doing well, thank you for asking!"
        elif option == 3:
            return "My name is codsoftChatBot. Nice to meet you!"
        elif option == 4:
            return "I can help you with basic conversation. Try saying hello, asking my name, or asking how I am!"
        elif option == 5:
            return "I'm a computer program, so I don't have an age."
        elif option == 6:
            return "Goodbye! Have a great day!"
        else:
            return "Invalid option. Please choose from 1-6 or type your own message."

    # Convert input to lowercase for easier matching
    user_input = user_input.lower()

    # Define response rules
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    
    elif "how are you" in user_input:
        return "I'm doing well, thank you for asking!"
    
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    
    elif "name" in user_input:
        return "My name is  codsoftChatBot. Nice to meet you!"
    
    elif "what can you do" in user_input:
        return "I can help you with basic conversation. Try saying hello, asking my name, or asking how I am!"
    
    elif "what is your age" in user_input:
        return "I'm a computer program, so I don't have an age."
    
    else:
        return "I'm not sure how to respond to that. Try asking something else!"

def main():
    print("ChatBot: Hi! I'm a simple chatbot. Type 'bye' to exit.")
    display_options()
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("ChatBot: Goodbye!")
            break
            
        response = get_response(user_input)
        print("ChatBot:", response)
        display_options()  # Show options after each response

if __name__ == "__main__":
    main()
