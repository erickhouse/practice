
def CanChicken(options, target):

    results = [0]
    def canMakeChicken(options, results):
        if len(options) == 0:
            return False
        
        res = []
        for r in results:

            curr = options[0]
            count = 1

            getNext = lambda: (curr * count) + r
            nextVal = getNext()

            while nextVal <= target:
                if nextVal == target:
                    return True
                res.append(nextVal)
                count += 1
                nextVal = getNext()

        options.pop(0)
        return canMakeChicken(options, res + results)

    return canMakeChicken(options,results)

print(CanChicken([4,7,10], 11))
print(CanChicken([4,7,10], 17))
print(CanChicken([4,7,10], 13))
print(CanChicken([4,7,10], 16))
print(CanChicken([4,7,10], 22))
print(CanChicken([4,7,10], 5))
print(CanChicken([], 12))


  

	
  
