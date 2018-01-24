
def myPow(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    if n == 0:
        return 1
    if n == 1:
        return x
    if n == -1:
        return 1/x
        
    p = 2
    val = x * x
    while p + p <= abs(n):
        p += p
        val *= val
            
    while p < abs(n):
        p += 1
        val *= x
            
    if n < 0:
        return 1/val
            
    return val


def newPow(x, n):

    if n == 0:
        return 1
    if n == 1:
        return x
    if n == -1:
        return 1/x

    powers = {
        10 : x * x * x * x * x * x * x * x * x * x,
        9 : x * x * x * x * x * x * x * x * x,
        8 : x * x * x * x * x * x * x * x,
        7 : x * x * x * x * x * x * x,
        6 : x * x * x * x * x * x,
        5 : x * x * x * x * x,
        4 : x * x * x * x,
        3 : x * x * x,
        2 : x * x,
        1 : x,
    }

    e = abs(n)
    val = 1
    for p in powers:
        if e // p > 0:
            e = e % p
            val *= powers[p] * e // p

    if n < 0:
        return 1/val
            
    return val



print(newPow(2,21))