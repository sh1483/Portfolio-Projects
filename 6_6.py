
favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python'
}

friends = ['phil','sarah', 'edward', 'jen', 'erin', 'jim',
'paul','peter','samuel','ethan','john']
    
for friend in friends:
    if friend in favorite_languages.keys():
        print(f"\n{friend.title()}, Thanks for taking the poll!")
    else:
        print(f"\n{friend.title()}, Please take the poll!")
 
