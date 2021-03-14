'''
Name: Guy F.
Date: 3/14/2021 12:20am
Description: Create a list of people living or dead and then invite them to your party.

Extend the part and use insert() and append() and pop() methods.
'''

guests = ["Steve Jobs", "Bill Gates", "Scott Galloway"]

for guest in guests:
    print(f"\nHello, {guest}! You are ivnited to my party!")

print(f"\n{guests[0]} is unable to attend!")

guests.remove("Steve Jobs")

guests.insert(0, "Neil DeGrasse Tyson")

for guest in guests:
    print(f"\nHello, {guest}! You have been invited to my party!")

print("\nI've found an even biger table, inviting more guests!")

guests.insert(0, "Elon Musk")

guests.insert(2, "Neil Armstrong")

guests.append("Bill Nye")

for guest in guests:
    print(f"\nHello, {guest}! You have been invited to my party!")

print("\nMy new table won't be ready in time! I can only invite 2 guests!")

removed_guests = []

removed_guests.append(guests.pop(0))
removed_guests.append(guests.pop(1))
removed_guests.append(guests.pop(1))
removed_guests.append(guests.pop(-1))

print(f"Guests removed: {removed_guests}.")

print(f"Guests attending: {guests}.")
