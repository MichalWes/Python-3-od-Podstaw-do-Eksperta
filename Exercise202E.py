class User:
    name = "Andrzej"  # zmienna statyczna
    nextId = 1

    def __init__(self, name=""):
        self.name = name
        self.id = User.nextId
        User.nextId += 1
