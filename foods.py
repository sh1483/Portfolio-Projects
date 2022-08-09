#copying a list
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friends favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')#this shows that while we copied the list, they are actually two different lists
friend_foods.append('ice cream')

print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friends favorite foods are:")
print(friend_foods)
#if we just set friend_foods to = my_foods the lists would show both items in them

#slices
print("\nThe first three items from the list are:")
for food in my_foods[:3]:
	print(food.title())

print("\nItems from the middle of the list are:")
for food in my_foods[1:3]:
	print(food.title())	

print('\nThe last three items on my list are:')
for food in my_foods[-3:]:
	print(food.title())


print('\nMy smelliest foods are:')
for food in my_foods:
	print(food.title())

print('\nMy friend decided they now hate:')
for food in friend_foods:
	print(food.title())

	