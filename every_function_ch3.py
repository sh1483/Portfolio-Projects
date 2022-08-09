
items=['cars','motorcycles','locations','guests']
print(items)

print(sorted(items))
print(items[2].title())

print(f"One of my favorite things on this list are {items[0].title()}.")
items[3]="helicopters"
print(items)

items.append("guests")
print(items)

items.insert(2,"dogs")
print(items)

del items[2]
print(items)

items.pop()
print(items)

items.pop(0)
print(items)

items.remove('helicopters')
print(items)

print(items[-1])

items.append('bicycles')
items.append('cars')
items.append('guests')
print(items)

print(sorted(items))

items.reverse()

print(items)

items.sort()
print(items)

items.reverse()
print(items)

print(len(items))
