
import random

#rand7() returns each integer with equal probability.
#rand5() must also return each integer with equal probability.
# 2 / 10 / 2017

def rand7():
    return random.randint(1, 7)

# def rand5():
#     int5 = (rand7() * 5) - ((rand7() + 3) / 2)
#     print int5
#     int5 %= 5
#     int5 += 1
#     print

def rand5():
    result = 7 # arbitrarily large
    while result > 5:
        result = rand7()
    return result


rand5()
