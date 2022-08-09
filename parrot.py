#Using INPUT to require user input to run the code (will only work in terminal)
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

#Setting the program to run until the user decides to quit
prompt = input("Tell me something, and I will repeat it back to you: ")
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
#Below won't display 'quit' as a message when you quit the game.
    if message != 'quit':
        print(message)

#Using a FLAG in case you want multiple ways to quit a game
prompt = input("Tell me something, and I will repeat it back to you: ")
prompt += "\nEnter 'quit' to end the program. "

active = True #This is the FLAG
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)