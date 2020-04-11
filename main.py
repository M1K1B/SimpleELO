import playerStats
import game

players = []
nop = input("Number of players: ")

for i in range(int(nop)):
	user = input("Username of player {0}: ".format(i+1))
	players.append(playerStats.Player(user, 1000))


def startGame():
	selected = []
	expected = [] # Format: p1, p2

	print("Users and their ELO points")
	for p in players:
		print("{0} ........ {1}".format(p.user, p.elo))

	for i in range(2):
		s = input("Insert username of the Player {0}: ".format(i+1))

		for player in players:
			if s == player.user:
				selected.append(player)

	print("---- Simulated outcome ----------------------")

	# Calculate outcome and expected result
	outcome = game.calculateOutcome()
	expected = game.calculateWP(selected[0], selected[1])


	selected[0].updateElo(abs(outcome), expected[0])
	selected[1].updateElo(abs(1-outcome), expected[1])

	# Print calculated data

	print("Chances to win:")
	print("{0} : {1}".format(selected[0].user, expected[0]))
	print("{0} : {1}".format(selected[1].user, expected[1]))
	print("\n")
	if outcome == 1:
		print("{0} wins!".format(selected[0].user))
	else:
		print("{0} wins!".format(selected[1].user))

	print("\n")


while(1):
	startGame()