import json

#	Initialize the number of players and their level, and
#	how many mosters they if would like

#TO DO: Create error catch for all three inputs
player_count = int(input("How many players do you have?"))

avg_level = int(input("What is the aproximate average level of your party?"))
#	Uncomment this next line when ready to code it
#monster_num = int(input("How many monsters would you prefer, if a specific amount?"))



#   Using the above inputs, generate a number to search for monsters
#	with appropriate Challenge Rating for the party in the dictionary


if player_count > 5:
	CR_Balance = avg_level + (player_count - 5)
elif player_count >= 3 and player_count <= 5:
	CR_Balance = avg_level
elif player_count < 3:
	CR_Balance = avg_level - 1
elif player_count < 3 and avg_level == 1:
	CR_Balance = 1

#	Open the file with a error catch
try:
	monsters = open("5e_Monsters.json", "r")
except:
	print("Error reading '5e_Monsters' file")
#	Reading the file
monster_list = json.loads(monsters.read())

#	Create a list to add results from the balancing math
#	and the monster monster_list

result_list = []

#	Iterate over the list of monsters setting the challenge
# 	rating against the CR_Balance from earlier, adding the
#	results to result_list

for amonster in monster_list:
	if amonster["challenge_rating"] == CR_Balance:
		result_list.append(amonster)

for result in result_list:
	print(result["name"],result["challenge_rating"])

info_request = input("Enter the name of the monster you would like information on:")



for result in result_list:
	if info_request.lower() == result["name"].lower():
		the_chosen_one = result

print(the_chosen_one)