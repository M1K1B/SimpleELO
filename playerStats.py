class Player:

	# Max points for rank 
	rankA = 500
	rankB = 400
	rankC = 300
	rankD = 200
	rankE = 100

	def __init__(self, user, points):
		self.user = user
		self.elo = points


	#Check for rank based on elo points
	def checkRank(self):
		elo = self.elo

		if elo < 3000:
			if elo < 2000:
				if elo < 1000:
					return "Rank E"
				else:
					return "Rank D"
			else:
				return "Rank C"
		else:
			if elo > 4000:
				return "Rank A"
			else:
				return "Rank B"


	#Update elo points
	def updateElo(self, score, expected):
		self.elo = self.elo + int(32 * (score - expected))