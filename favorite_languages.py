favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python'
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.\n")


#looping through each key-value pair
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")


#looping through all the keys in the dictionary
print("\n")
for name in favorite_languages.keys():#using .keys may make easier to read
    print(name.title())

#looping through keys is defualt. Can write above as:
print("\n")
for name in favorite_languages:
    print(name.title())

#adding a message for specific people in the dictionary and a list
print("\n")
friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

#seeing if a particular person was polled about favorite language
if 'erin' not in favorite_languages.keys():
    print("\nErin, please take our poll!")


#looping through a dictionary in a certain order
favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python'
}
#sorted will sort values alphabetically
for name in sorted(favorite_languages.keys()):
    print(f'{name.title()}, thank you for taking the poll.')

#looping through just the values
print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

#ensuring there are no repeated values
print("\nThe following languages have been mentioned:")
for language in set (favorite_languages.values()):
    print(language.title())

#another way to write the above as a set
languages = {'python', 'ruby', 'python', 'c'}
#sets and dictionaries are both in braces, sets have no key:value pairs though


print(languages)

print("\n")
print("...")
print("\n")


favorite_languages = {
    'jen' : ['python', 'ruby'],
    'sarah' : ['c'],
    'edward' : ['ruby', 'go'],
    'phil' : ['python','haskell'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
