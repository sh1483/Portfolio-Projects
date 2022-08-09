
print("This is the menu at the buffet:")
foods = ('chicken','beef','peas','carrots','pudding')
for food in foods:
    print(food)

# foods[2] = ('bologna') shows we can't change an item this way

foods = ('chicken','beef','corn','broccoli','pudding')
print("\nThe new menu now includes:")
for food in foods:
    print(food.title())