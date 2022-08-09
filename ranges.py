
for value in range(1,5):#range starts at first number end ends one before last number
	print(value)

for value in range(1,6):
		print(value)

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))#the range is 2-11, the next number is what it counts by
print(even_numbers)

squares = []
for value in range(1,11):#getting the square of each number 1-10
	square = value ** 2
	squares.append(square)

print(squares)

squares = []#same as above, but more efficient coding
for value in range(1,11):
	squares.append(value**2)

print(squares)

#Here is a "List Comprehension" of the previous code. This is a way to write a code efficiently in just one line.
squares = [value**2 for value in range(1,11)]
print(squares)

digits = ['1','2','3','4','5','6','7','8','9','0']
print(min(digits))
print(max(digits))

