#Tuples (an immutable list, or one that can not by changed)
dimensions = (200,  50)
print(dimensions[0])
print(dimensions[1])
#trying to change the value in dimensions would cause an error, for instance
#trying to change the first dimension with: dimensions[0] = 250 creates a
#traceback error

for dimension in dimensions:
    print(dimension)

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)



