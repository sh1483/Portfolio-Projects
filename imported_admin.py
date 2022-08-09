class User:
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, location, age, sex):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.location = location.title()
        self.age = age
        self.sex = sex.title()
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Location: {self.location}")
        print(f"  Age: {self.age}")
        print(f"  Sex: {self.sex}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"\nWelcome back, {self.first_name}!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0


class Admin(User):
    """A user with administrative privileges."""

    def __init__(self, first_name, last_name, location, age, sex):
        """Initialize the admin."""
        super().__init__(first_name, last_name, location, age, sex)

        # Initialize an empty set of privileges.
        self.privileges = Privileges()


class Privileges:
    """A class to store an admins' privileges."""

    def __init__(self, privileges=None):
        if privileges is None:
            privileges = []
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- This user has no privileges.")
