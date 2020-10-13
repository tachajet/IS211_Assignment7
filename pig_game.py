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
		self.turn(self.pig_players)
	def turn(self,pig_players):
		for p in range(0,len(pig_players)):
			roll=self.die
			while pig_players[p].turn==True:
				roll.roll()
				if (roll.score==1):
					print("Sorry Player", str(pig_players[p].num+1), "You have rolled a 1 and your turn is over")
					pig_players[p].turn=False
				else:
					pig_players[p].current_score=roll.score
					pig_players[p].total_score+=roll.score
					print("Congratulations Player", str(pig_players[p].num+1), "you rolled a", str(roll.score), " and your current score is", str(pig_players[p].total_score))
					choice=input("Would you like to hold or continue to roll? Type h for hold and r to roll")
					if choice.upper()=="H":
						pig_players[p].turn=False
					elif choice.upper()=="R":
						pig_players[p].turn=True
					else:
						print("Not a valid input, please try again")
						
				if pig_players[p].total_score==100:
					print("Congratulations", str(pig_players[p].num+1), "you won!")
					
					
						
				
		
test_roll=Dice()


print(test_roll.score)
test_roll.roll()
print(test_roll.score)
pgame=Pig(2)