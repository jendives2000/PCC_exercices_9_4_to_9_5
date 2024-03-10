# Exercises 9-4 & 9-5 from the book Python Crash Course by Eric Matthes.
# These exercises are about Classes and introduces Object Oriented Programming concepts.

# -----------------------------------------------------------------------------
# Exercises 9-5:
# 1a. Add an attribute called login_attempts to your User class from Exercise 9-3 (page 162).
# 1a.1. Write a method called increment_login_attempts() that increments the value of login_attempts by 1.
# 1a.2. Write another method called reset_login_attempts() that resets the value of login_attempts to 0.
# 2a. Make an instance of the User class
# 2a.2. and call increment_login_attempts() several times.
# 2a.3. Print the value of login_attempts to make sure it was incremented properly,
# 2a.4. and then call reset_login_attempts().
# 2a.5. Print login_attempts again to make sure it was reset to 0.
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


class User:
    """A simple attempt to model a user."""

    def __init__(
        self,
        first_name: str,
        last_name: str,
        age: int,
        country: str,
        login_attempts=0,  # 1a.
    ):
        """Initialize all parameters."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.country = country.title()
        self.login_attempts = login_attempts

    def describe_user(self):
        """Prints all passed arguments"""
        print_1 = f"\n{self.first_name} {self.last_name} is"
        print_1 += f"{self.age} years old living in {self.country}."
        print(print_1)

    def greet_user(self):
        """Prints a greeting."""
        print_2 = f"\nHello, {self.first_name} {self.last_name}!"
        print_2 += "It's great to have you onboard!"
        print(print_2)

    def increment_login_attempts(self):  # 1a.1.
        """Increments login_attempts by 1."""
        self.login_attempts += 1
        print(f"Login attempts incremented.\n\tNow = {self.login_attempts}")

    def reset_login_attempts(self):  # 1a.2.
        """Resets login_attempts to 0."""
        self.login_attempts = 0
        print(f"Login attemtps reset.\n\tNow = {self.login_attempts}")


user_1 = User("John", "Doe", 44, "USA")  # 2a.
user_1.increment_login_attempts()  # 2a.2.
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()

print(user_1.login_attempts)  # 2a.3.
user_1.reset_login_attempts()  # 2a.4
print(user_1.login_attempts)  # 2a.5.
