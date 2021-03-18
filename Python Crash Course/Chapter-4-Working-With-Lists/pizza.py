'''
Name: Guy F.
Date: 3-17-2021
Description: Iterate of a list of 3 favorite pizza types and use them in a sentence.
'''

pizzas = ['pepperoni', 'hawaiian', 'supreme']

for pizza in pizzas:
    if pizza == 'hawaiian':
        print(f"Yes, I like {pizza.title()} pizza!")

    print(f"I like {pizza.title()} pizza.")

print("Pizza is great...sometimes.")
