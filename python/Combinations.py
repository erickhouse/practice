
def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    
    i = n - 1
    s = {"()"}

    while(i > 0):
        temp = set()
        for pair in s:
            temp.add("()" + pair)
            temp.add('('+ pair + ')')
            temp.add(pair + "()")
            
        s = temp
        i = i - 1
    
    return list(s)


expected = set(["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"])
actual = set(generateParenthesis(4))

print(expected - actual)
print(actual)
