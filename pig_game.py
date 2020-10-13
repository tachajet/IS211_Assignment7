from random import randint
from itertools import chain, repeat
#This program unfortunately does not work as I'd hoped, but at least I think I can explain why
class Dice():
	def __init__(self):
		self.score=0
	def roll(self):
		self.score = randint(1, 6)
		return self.score
#Dice and Player classes are OK, I think
class Player():
	def __init__(self,num):
		self.num=num
		self.current_score=0
		self.total_score=0
		self.turn=True
#Here's where I lost the thread:
class Pig():
	def __init__(self,num_players):
		#I had wanted to try to make a version with a customizable number of players...
		self.pig_players=[Player(x)for x in range(0,num_players)]
		self.die=Dice()
		self.game_over=False
		self.turn(self.pig_players)
	#...but that led to me short-sightedly trying to define the entire game below:
	def turn(self,pig_players):
		for p in range(0,len(pig_players)):
			roll=self.die
			#Looping through the player objects doesn't work once you run out of players! It just terminates the loop without meeting endgame conditions.
			#I should have broken this up further for any hope of making it functional
			while pig_players[p].turn==True and pig_players[p].total_score<=100:
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

					
def main():
	import argparse
	parser=argparse.ArgumentParser()
	parser.add_argument('--numPlayers', type=int)
	args=parser.parse_args()
	pass_page=Pig(args.numPlayers)
if __name__=="__main__":
	main()