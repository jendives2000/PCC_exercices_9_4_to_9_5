# Exercises 9-4 & 9-5 from the book Python Crash Course by Eric Matthes.
# These exercises are about Classes and introduces Object Oriented Programming concepts.
# -----------------------------------------------------------------------------
# Exercise 9-4:
# 1a. Start with your program from Exercise 9-1 (page 162).
# 1a.1. Add an attribute called number_served with a default value of 0.
# 1a.2. Create an instance called restaurant from this class.
# 1a.3. Print the number of customers the restaurant has served,
# 1a.4. and then change this value and print it again.
# 2a. Add a method called set_number_served() that lets you set the number of customers that have been served.
# 2a.1. Call this method with a new number
# 2a.2.  and print the value again.
# 3a. Add a method called increment_number_served() that lets you increment the number of customers who’ve been served.
# 3a.1 Call this method with any number you like that could represent how many customers were served in, say, a day of business.

# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------


class Restaurant:  # 1a.
    """A simple attempt to model a Restaurant."""

    def __init__(self, name: str, cuisine_type: str, number_served=0):  # 1a.1.
        """Initialize name and cuisine type."""
        self.name = name.title()
        self.cuisine_type = cuisine_type.title()
        self.number_served = number_served

    def describe_restaurants(self):
        """Prints name and cuisine_type."""
        print_1 = f"\nYou chose this restaurant: {self.name},"
        print_1 += f"which offers:\n\t{self.cuisine_type} food."
        print(print_1)

    def open_restaurants(self):
        """Prints message indicating the restaurant is open."""
        print_a = f"{self.name} is open, you may book a table."
        print(print_a)

    def how_many_clients_served(self):
        """Prints how many clients were served so far"""
        print_b = f"\n{self.name} has served {self.number_served} customers so far."
        print(print_b)

    def set_clients_served(self, new_number_served):  # 2a.
        """Set the number of clients served"""
        self.number_served = new_number_served

    def add_clients_served(self, more_clients: int):  # 3a.
        """Adds more clients to number served so far & Prints number of clients"""
        if more_clients > 0:
            self.number_served += more_clients
            print_c = f"\n{self.name} has served:"
            print_c += f"\n\tan additional {more_clients} clients, totaling {self.number_served} customers so far."
            print(print_c)
        else:
            print_c = f"\nAdding this number: {more_clients} is impossible."


restaurant = Restaurant("Punjabi", "Indian", number_served=7982)  # 1a.2.
restaurant.how_many_clients_served()  # 1a.3.
restaurant.number_served = 8361  # 1a.4.
restaurant.how_many_clients_served()
restaurant.set_clients_served(8362)  # 2a.1.
restaurant.how_many_clients_served()  # 2a.2.
restaurant.add_clients_served(157)  # 3a.1
