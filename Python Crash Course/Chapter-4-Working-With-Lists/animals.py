'''
Name: Guy F.
Date: 3-17-2021
Description: Create a list of animals that all have something in commong. Print out a statement about each animal. State what they have in common.
'''

animals = ["dog", "cat", "wolf"]

for animal in animals:
    if animal == "wolf":
        print(f"A {animal.title()} would not make a great pet.")
    else:
        print(f"A {animal.title()} would make a great pet.")

print(
    f"\nEvery animal in this list is a mammal. In addition:\n{animals[0].title()} has claws and {animals[1].title()} also has claws.\n{animals[2].title()} has claws and so does {animals[0].title()} and {animals[1].title()}.")
