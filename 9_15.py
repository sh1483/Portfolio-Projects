# Using a loop to see the chances of winning your lottery,
from random import choice


def get_winner(possibilities):
    """Return a winning ticket from a set of possibilities."""
    winner = []

# We don't want to repeat winning numbers or letters, so we'll use a, 
# While loop.
    while len(winner) < 4:
        drawn_item = choice(possibilities)

        # Only add the pulled item to the winning ticket if it hasn't
        #   already been pulled.
        if drawn_item not in winner:
            winner.append(drawn_item)

    return winner


def check_ticket(played_ticket, winner):
    # Check all elements in the played ticket. If any are not in the winning ticket,
    # Return False.
    for element in played_ticket:
        if element not in winner:
            return False

# We must have a winning ticket!
    return True


def make_random_ticket(possibilities):
    """Return a random ticket from a set of possibilities."""
    ticket = []
# We don't want to repeat numbers or letters, so we'll use a while loop.
    while len(ticket) < 4:
        drawn_item = choice(possibilities)

# Only add the drawn item to the ticket if it hasn't already been drawn.
        if drawn_item not in ticket:
            ticket.append(drawn_item)

    return ticket


possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
winner = get_winner(possibilities)

plays = 0
won = False

# Let's set a max number of tries, in case this takes forever!
max_tries = 1_000_000

while not won:
    new_ticket = make_random_ticket(possibilities)
    won = check_ticket(new_ticket, winner)
    plays += 1
    if plays >= max_tries:
        break

if won:
    print("We have a winning ticket!")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winner}")
    print(f"It only took {plays} tries to win!")
else:
    print(f"Tried {plays} times, without pulling a winner. :(")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winner}")
