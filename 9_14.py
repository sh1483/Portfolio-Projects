# Make a list or tuple containing a series of 10 numbers and 5 letters.
# Randomly select 4 numbers or letters from the list and print a message,
# Saying that any ticket that matches these letters and numbers wins the lottery.
from random import choice


possibilities = ['A', 'B', 'C', 'D', 'E', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

winner = []
print("Time to draw the winner.")

# We don't want to repeat winners so we will use a while loop.
while len(winner) < 4:
    drawn_possibility = choice(possibilities)

    # Only add the drawn possibility if it hasn't been drawn before.
    if drawn_possibility not in winner:
        print(f"We drew a {drawn_possibility}")
        winner.append(drawn_possibility)

print(f"\nThe winner is {winner}")
