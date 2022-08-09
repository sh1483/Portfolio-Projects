# Make a CLASS.
class Users:
    """A class of users."""

# Create ATTRIBUTES.
    def __init__(self, first_name, last_name, location, age, sex):
        """Initialize attributes of the users."""
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age
        self.sex = sex
        self.login_attempts = 0

# Make a METHOD.
    def describe_user(self):
        """Summarize user information."""
        print(f"\n{self.first_name.title()} {self.last_name.title()}")
        print(f"\tLocation: {self.location.title()}")
        print(f"\tAge: {self.age}")
        print(f"\tSex: {self.sex.title()}")

# Make another METHOD.
    def greet_user(self):
        """Display a greeting for the user."""
        print(f"Welcome back {self.first_name.title()}!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets login_attempts to zero."""
        self.login_attempts = 0


class Admin(Users):
    """Create an Admin sub-class."""

    def __init__(self, first_name, last_name, location, age, sex):
        """Initialize the Admin."""
        super().__init__(first_name, last_name, location, age, sex)
        self.privileges = []

    def show_privileges(self):
        """Display the available privileges."""
        print('\nThey have the following privileges:')
        for privilege in self.privileges:
            print(f"\t-{privilege.title()}")


jon = Admin('jon', 'doe', 'tokyo', 25, 'male')
jon.describe_user()


jon.privileges = [
    "can add post",
    "can delete post",
    "can ban user",
    "can add user"
    ]

jon.show_privileges()

# Create an INSTANCE.
kristen = Users('kristen', 'starzynski', 'pflugerville', 37, 'female')
# CALL the METHODS.
kristen.describe_user()
kristen.greet_user()

# Create 3 login_attempts incrementally.
print("Making 3 login attempts...")
kristen.increment_login_attempts()
kristen.increment_login_attempts()
kristen.increment_login_attempts()
print(f" Login attempts: {kristen.login_attempts}")

# Reset the number of login_attempts.
print("Resetting login attempts...")
kristen.reset_login_attempts()
print(f" Login attempts: {kristen.login_attempts}")

marnie = Users('marnie', 'starzynski', 'pflugerville', 7, 'female')
marnie.describe_user()
marnie.greet_user()

kitty = Users('kitty', 'starzynski', 'pflugerville', 12, 'female')
kitty.describe_user()
kitty.greet_user()

james = Users('james', 'haynes', 'pflugerville', 1, 'male')
james.describe_user()
james.greet_user()
