current_users = ['jose','juan pablo','mario','manuel','victor','valeria','maria']
new_users = ['Jose','juan pablo','marco','josue','enrique']

for new_users in new_users:
    if new_users.lower() in current_users:
       print(f"Sorry, {new_users} that name has been taken. Enter a new user name.")
    else:
      print(f"{new_users} is available to use.")