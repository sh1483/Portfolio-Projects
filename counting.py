
numbers = list(range(1,21))
print(numbers)

for value in range(1,21):
	print(value)

one_million = list(range(1,1_000_001))
#print(one_million)#commenting this out before printing the min, max, and sum speeds things up

print(min(one_million))
print(max(one_million))
print(sum(one_million))	

for value in range(1,21,2):#odd numbers 1-20
	print(value)

#multiples of 3
for value in range(3,31,3):
	print(value)

#cubes
cubes = []
for value in range(1,31):
	cubes.append(value**3)
print(cubes)

#List Comprehension of cubes
cubes = [value**3 for value in range(1,31)]#same as above, but more efficient coding
print(cubes)




