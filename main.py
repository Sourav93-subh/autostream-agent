from agent import chat

print("AutoStream Agent Started (type 'exit' to stop)\n")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        break

    response = chat(user)
    print("Bot:", response)