#Louise and Richard play a game. They have a counter set to 
#.In every game, Louise gets the first turn and the turns alternate thereafter.
# In the game, they perform the following operations.

#If  is not a power of , reduce the counter by the largest power of  less than .
#If  is a power of , reduce the counter by half of .
#The resultant value is the new  which is again used for subsequent operations.
#The game ends when the counter reduces to 1, i.e., , and the last person to make a valid move wins.

#Given , your task is to find the winner of the game.


def game(n, person):

    if(n == 1):
        if(person == 1):
           print("Richard") 
        else:
           print("Lousie")
        return

    if not (n & (n -1) == 0):
        count = 0
        temp = n
        while (temp >> 1) > 0:
            count += 1
            temp = temp >> 1

        game(n - (1 << count), person ^ 1)

    else:
        game(n >> 1, person ^ 1)


game(6, 1)





