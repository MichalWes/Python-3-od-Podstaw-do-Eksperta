from types import ClassMethodDescriptorType


class User:
    def print_age(self):
        print(self.name, "ma", self.age, "lat")

    def __init__(self, age, name):
        print("Jestem inicjalizatorem")
        self.age = age
        self.name = name

    def name(args):
        pass


user1 = User(34, "Arek")
user2 = User(24, "Mirek")
user3 = User(23, "Michal")
UserList = [user1, user2, user3]


UserList[1].print_age()
# user2.print_age()
