from random import randint

class Dice():
	def __init__(self):
		self.score=0
	def roll(self):
		self.score = randint(1, 6)
		return self.score

class Player():
	def __init__(self,num):
		self.num=num
		self.current_score=0
		self.total_score=0
		self.turn=True
class Pig():
	def __init__(self,num_players):
		self.pig_players=[Player(x)for x in range(0,num_players)]
		self.die=Dice()
		self.turn(self.pig_players[0])
	def turn(self,pig_players):
		while pig_players[0].status==True:
			roll=self.die.roll()
			if (roll.score==1):
				print("You have rolled a 1 and your turn is over")
				pig_players[0].turn=False
			else:
				pig_players[0].current_score=roll
				pig_players[0].total_score+=roll
				print("Congratulations Player", str(pig_players[0].num), "your current score is", str(pig_players[0].total_score))
				
		
test_roll=Dice()


print(test_roll.score)
test_roll.roll()
print(test_roll.score)
pgame=Pig(5)
p_one=pgame.pig_players[4]

print(p_one.turn)