
pizzas = ['pepperoni','sausage','supreme','cheese']
for pizza in pizzas:
    print(pizza)

pizzas = ['pepperoni','sausage','supreme','cheese']
for pizza in pizzas:
    print(f"I love {pizza.title()} pizza!")
print(f"I love pizza!")

friend_pizza = pizzas[:]

pizzas.append('margarita')
friend_pizza.append('dessert')

print("\nMy favorite pizzas are:")
for pizza in pizzas:
    print(pizza.title())

print("\nMy friends favorite pizzas are:")
for pizza in friend_pizza:
    print(pizza.title())

#checking for inequality
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("\nHold the anchovies!")

requested_topping = ['mushrooms','onions','pineapple']
print('mushrooms' in requested_topping)
print('pepperoni' in requested_topping)

#if looping
requested_toppings = ['mushrooms','extra cheese']
if 'mushrooms' in requested_toppings:
    print('\nAdding mushrooms')
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese')

print('\nFinished making your pizza!')


#simplified version of above
requested_toppings = ['mushrooms', 'green peppers','extra cheese']

for requested_toppings in requested_toppings:
    print(f"Adding {requested_toppings}.")

print("\nFinished making your pizza!")


#adding if statement into above (out of green peppers)
requested_toppings = ['mushrooms', 'green peppers','extra cheese']

for requested_toppings in requested_toppings:
    if requested_toppings == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_toppings}.")

print("\nFinished making your pizza!")


#checking that a list is not empty
requested_toppings = []

if requested_toppings:
    for requested_toppings in requested_toppings:
        print(f"Adding {requested_toppings}.")
    print("\nFinished making your pizza!")
else:
    print("\nAre you sure you want a plain pizza?")

print("\n")
#using multiple lists
available_toppings = ['mushrooms','olives','green peppers','pepperoni',
                        'pineapple','extra cheese']

requested_toppings = ['mushrooms','french fries','extra cheese']

for requested_toppings in requested_toppings:
    if requested_toppings in available_toppings:
        print(f"Adding {requested_toppings}.")
    else:
        print(f"Sorry, we dont have {requested_toppings}.")

print("\nFinished making your pizza!")

print("\n")
print("...")
print("\n")

# **A LIST IN A DICTIONARY**
# Store information about a pizza being ordered
pizza = {
    'crust' : 'thick',
    'toppings' : ['mushrooms','extra cheese'],
}

# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza"
    " with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")
