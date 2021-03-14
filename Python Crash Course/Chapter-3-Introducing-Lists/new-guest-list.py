'''
Name: Guy F.
Date: 3/14/2021 12:08am
Description: Create a list of people living or dead and then invite them to your party.
'''

guests = ["Steve Jobs", "Bill Gates", "Scott Galloway"]

for guest in guests:
    print(f"Hello, {guest}! You are ivnited to my party!")

print(f"{guests[0]} is unable to attend!")

guests.remove("Steve Jobs")

guests.insert(0, "Neil DeGrasse Tyson")

for guest in guests:
    print(f"Hello, {guest}! You have been invited to my party!")
