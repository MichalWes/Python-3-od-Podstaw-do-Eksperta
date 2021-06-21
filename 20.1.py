from types import ClassMethodDescriptorType


class User:
    age = 0
    name = ""

    def print_age(self):
        print(self.name, "ma", self.age, "lat")

    def name(args):
        pass


user1 = User()
user2 = User()
user3 = User()
UserList = [user1, user2, user3]

user1.name = "Arek"
user1.age = 27

user2.name = "Witek"
user2.age = 34

UserList[1].print_age()
# user2.print_age()
