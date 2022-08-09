favorite_numbers = {
    'juan' : [7, 27],
    'pablo' : [13, 12],
    'maria' : [2, 0, 4],
    'jose' : [376, 673],
    'enrique' : [12, 88],
}

for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + " prefers these numbers:")
    for number in numbers:
        print("\t" + str(number))
