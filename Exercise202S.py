from Exercise202E import User

""" a = "Łukasz"
b = "Roman"
c = "Bartek"

a.name = "Pirat"

print(a.name)
print(b.name)
print(c.name)
print(a.id)
 """
users = [User() for _ in range(8)]

for user in users:
    print(user.id)
