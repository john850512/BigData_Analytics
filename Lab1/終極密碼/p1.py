###############################################################################################
# Date:20180305
# Name:p1.py
# StudentID:A1035501
# Author:孫茂勛
# Note:Lab1
###############################################################################################
import random

ans = random.randint(0,100)
range_max = 100
range_min = 0
is_gameOver = False

def game_start():    
    print(ans)
    while is_gameOver == False:
        print("Guess a number between",range_min,"and",range_max,":")
        try:
            #Since input() will return a string,explicit convet int() will work correct when we input is an integer
            #if we input a float, then int() will cause ValueError
            guess = int(input())
        except ValueError:
            print('Your input doesnt an Integer!')
            continue
        check_fun(guess,ans)
def check_fun(guess,ans):
    global range_max,range_min,is_gameOver
    if guess == ans:
        is_gameOver = True
        print("Congulation!!You are guess the correct number!")
    elif guess < ans:
        range_min = guess + 1
        print("You guess wrong!!Guess a number between",range_min,"and",range_max,":")
    else: # guess > ans
        range_max = guess - 1
        print("You guess wrong!!Guess a number between",range_min,"and",range_max,":")

if __name__ == '__main__':
    game_start()
    
