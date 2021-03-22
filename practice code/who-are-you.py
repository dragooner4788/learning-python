profile = {
    "first name": "",
    "last name": ""
}

user_first_name = input("What is your first name? ")

user_last_name = input("What is your last name? ")

profile["first name"] = user_first_name

profile["last name"] = user_last_name

print(profile)

user_name = list(map(lambda name: name[1], profile))

print(user_name)
