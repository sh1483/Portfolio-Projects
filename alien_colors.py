
alien_color = 'red'
if alien_color == 'green':
    print("You earned 5 points!")
if alien_color != 'green':
    print(f"The alien is actually {alien_color}.")

#runs the else block
if alien_color == 'green':
    print("\nYou earned 5 points!")
else:
    print("\nYou earned 10 points!")

#runs the if block
if alien_color != 'green':
    print("\nYou earned 10 points!")
else:
    print("\nYou earned 5 points!")

#if-elif-else chains
alien_color = 'red'
if alien_color == 'green':
    print("\n5 points!")
elif alien_color == 'yellow':
    print("\n10 points!")
else:
    print("\n15 points!")

alien_color = 'yellow'
if alien_color == 'green':
    print("\n5 points!")
elif alien_color == 'yellow':
    print("\n10 points!")
else:
    print("\n15 points!")

alien_color = 'green'
if alien_color == 'green':
    print("\n5 points!")
elif alien_color == 'yellow':
    print("\n10 points!")
else:
    print("\n15 points!")


   