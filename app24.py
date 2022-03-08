# 2:32:24 Dictionary
user = {
    "name": "Bono Uganda",
    "age": 23,
    "is_admin": True
}

name = user["name"]
print(name)

if "name" in user:
    print(user["name"])
if "aaa" in user:
    print(user["aaa"])

print(user.get("name"))
print(user.get("aaa"))
print(user.get("aaa", "Name not found"))

user["gender"] = "male"
print(user)

user["age"] = 62
print(user)