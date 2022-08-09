#Here we will be using a "slice" to retrieve portions of a list
players = ['charles','martina','michael','florence','eli']
print(players[0:3])#first 3
print(players[1:4])#middle 3
print(players[:4])#first 4
print(players[2:])#3 and on
print(players[-3:])#third from end and on

#looping through a slice
print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())

