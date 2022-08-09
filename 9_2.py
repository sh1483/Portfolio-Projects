class Restaurant:
    """Making a class to model a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize name and cuisine type attributes."""
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = f"{self.name} is open."
        print(f"\n{msg}")


barris = Restaurant("Barri's", 'pizza')
barris.describe_restaurant()

torchys = Restaurant("Torchy's", 'tacos')
torchys.describe_restaurant()

t_jins = Restaurant("T. Jin's", 'chinese food')
t_jins.describe_restaurant()
