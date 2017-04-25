# TicTacToe
Simple game in order to test reinforcement learning.

## Some probabilities
One simple experiment is to test the game with to random players on a classic 3 x 3 grill and see what is the game's outcome.  
On 10 000 games, the probabilities are:  
	- 0.5828 of victory for the player which begins the game
	- 0.2837 of the second player's victory
	- 0.1335 of draw  

How can we explain such outcomes ?  
Intuitively, it seems easier to win the game when we begin it, however the players have no strategy and the victory happens in more than half of the game.  

So let's do some funny math !  
This experiment is simply the exploration of one randomly selected branch of the game three. So in order to compute the previous probability, it is necessary to compute the number of branch in the three.   
First naive approach is to say that the first player has 9 position, the second 8 and so one... For a total of 9! possible branches
It is not false, it just does not take into account the symetry of this game: there are only three possibilities for the first player (all others are rotation of those ones)  

X|\#|\#		\#|X|\#		\#|\#|\#  
\#|\#|\#	\#|\#|\#	\#|X|\#  
\#|\#|\#	\#|\#|\#	\#|\#|\#  

Next move, the second player has 5 possibilities for the two first cases and only two for the third.  

Case 1  
X|O|\#		X|\#|O		X|\#|\#		X|\#|\#		X|\#|\#  
\#|\#|\#	\#|\#|\#	\#|\#|O		\#|\#|\#	\#|O|\#  
\#|\#|\#	\#|\#|\#	\#|\#|\#	\#|\#|O		\#|\#|\#  

Case 2  
\#|X|O		\#|X|\#		\#|X|\#		\#|X|\#		\#|X|\#  
\#|\#|\#	\#|\#|O		\#|\#|\#	\#|\#|\#	\#|O|\#  
\#|\#|\#	\#|\#|\#	\#|\#|O		\#|O|\#	\#|\#|\#

Case 3  
\#|O|\#		\#|\#|O  
\#|X|\#		\#|X|\#  
\#|\#|\#	\#|\#|\#  

This emphasizes that the different branches will no longer have the same weight. We can repeat the process until having reached a final state. However it will be long to enumerate all the possibilities... but let us continue just one more time to emphasize a tivial but interesting fact.

From the case 1a and 3b, we can obtain the same state !  
\#|X|O  
\#|X|\#  
\#|\#|\#  

I know, it is less impressive than you've imagined, but in a graph structure, that represents some merged nodes (but no loop, because we never merge a state with one of the same branch, otherwise that would mean that a level of lower deep has the same number of moves. Or by definition, a level is a new move ! From graph theory point of view, our tree remains a graph connex without cycle)  

So, when you have so much states to compute, use a computer ! It is the goal of the file analysis.py which estimates first the probabilities by simulating 10 000 games, then it computes the full tree and estimates the probabilities.

Here are some interesting results:
	-	By playing randomly, you have a probability 0.66 of winning the game if you begin, but only 0.32 if you are the second.
	- The total number of totally different states of this game is 764.
	-	There are 138 ends possible for this game.
	-	The number of possible different state by depth in the tree increases until the 6th round of the game.
	-	The average length of a game is : 6.93

That is all for this pre analysis ! This vision of the game is really simple because in fact no gamer will play randomly, you have to think that your enemy wants to maximize its gain. Next step : Min Max Algorithm !

# Dependencies
Executed with python3.5  
Need numpy
