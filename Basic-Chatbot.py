def chatbot_response(user_input):
    """
    Generate a chatbot response based on user input.

    Parameters:
    -----------
    user_input : str
        The message entered by the user.

    Returns:
    --------
    str
        A relevant chatbot response based on keyword matching.
    """
    # Taking input from user and converting input to lowercase and remove surrounding spaces
    user_input = user_input.lower().strip()

    # Check for specific keywords/phrases and respond accordingly
    # If/elif/else statement are use These conditions check whether the input contains known words or phrases. The chatbot replies accordingly.

    if "hello" in user_input or "hi" in user_input:
        return "Hi! 👋"
    elif "how are you" in user_input:
        return "I'm fine, thanks! 😊"
    elif "bye" in user_input:
        return "Goodbye! 👋"
    elif "what is your name" in user_input:
        return "I'm ChatBuddy, your simple chatbot! 🤖"
    elif "thank" in user_input:
        return "You're welcome! 😊"
    else:
        return "Sorry, I didn't understand that. 🤔"

# Chat loop
# Print initial greeting
print("🤖 ChatBot: Hello! Type something to start chatting (type 'bye' to exit).")
# Start a loop that continues until the user says "bye"

while True: # it prints forever untill breck is triggered

    # Get input from user
    user_message = input("You: ")

    # Get response by calling the function and The function returns a chatbot reply based on the input.
    response = chatbot_response(user_message) 

    # Print chatbot's response
    print("ChatBot:", response)

    # Exit loop if user says goodbye
    if "bye" in user_message.lower():
        break