import playerStats
import random
import math

# Calculate outcome of the game
# 1 -> player 1 wins
def calculateOutcome():
	ran = random.randint(0, 1)

	return ran

# Calculate chance of winning game for both players
def calculateWP(p1, p2):
	ep1 = 1/(1 + 10 ** ((p2.elo - p1.elo)/400))

	ep2 = 1 - ep1

	return [ep1, ep2]