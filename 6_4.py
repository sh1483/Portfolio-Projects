
glossary = {
    'key' : 'item',
    'value' : 'description',
    'tuple' : 'unchangeable collection',
    'list' : 'changeable collection',
    'dictionary' : 'storage device',
    'taco' : 'food',
    'juice' : 'drink',
    'cat' : 'pet',
    'Kristen' : 'wife',
    'James' : 'son',

}

for term, definition in glossary.items():
    print(f"{term.title()} = {definition.title()}")