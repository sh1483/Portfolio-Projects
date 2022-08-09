user_names = ['admin','achilles','juan pablo','persephone','hercules','hades']

for user_names in user_names:
    if user_names == 'admin':
        print(f"Hello, {user_names.title()} would you like a statues update?")
    else:
        print(f"Hello, {user_names.title()}. Nice to see you again!")