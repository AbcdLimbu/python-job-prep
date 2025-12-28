import datetime

class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def calc_birth_year(self):
        currentYear = datetime.datetime.today().year
        birthYear = currentYear - self.age
        return birthYear

    def display_info(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Email: ", self.email)
        print("Birth Year: ", self.calc_birth_year())



user1 = User("Rakesh", 34, "rakesh@gmail.com")
user2 = User("Akash", 22, "akash@gmail.com")

user1.display_info()
print("----------------")
user2.display_info()