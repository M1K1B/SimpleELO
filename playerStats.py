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

	def checkRank(self):
		elo = self.elo

		if elo < 300:
			if elo < 200:
				if elo < 100:
					return "Rank E"
				else:
					return "Rank D"
			else:
				return "Rank C"
		else:
			if elo > 400:
				return "Rank A"
			else:
				return "Rank B"