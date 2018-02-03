

def subStringsKDist(inputStr, num):
    vals = set()
    start = 0
    end = num

    while end <= len(inputStr):

        substr = inputStr[start:end]
        subset = set(substr)

        if len(subset) == num and subset not in vals:
            vals.add(substr)

        start += 1
        end += 1

    return list(vals)

# find the smallest sub sequences (not sets) with the fewest character overlaps
def lengthEachScene(inputList):
    
    pairs = dict()

    # calculate the range for every character 
    for i in range(0, len(inputList)):
        c = inputList[i]
        if inputList[i] not in pairs:
            pairs[c] = [i,i]
        else:
            pairs[c][1] = i # update the upper bound of the range if you have found a better one

    vals = pairs.values()
    ranges = list()

    # merge all of the calculated ranges into groups where the overlap
    for r in vals:
        if not ranges:
            ranges.append(r)
        else:
            last = ranges[-1]

            # determine if they overlap
            if r[0] <= last[1] and r[1] >= last[0]:
                if last[1] < r[1]:
                    last[1] = r[1] # update if the overlap extends the range (makes it bigger)
            else:
                ranges.append(r)
        
    # figure out the distances between the lowest and highest
    return list(map(lambda x: len(range(x[0], x[1])) + 1, ranges))


print(lengthEachScene(list("zzcbzchfihi"))) # [6,5]
print(lengthEachScene(list("abca"))) # [4]
print(lengthEachScene(list("abc"))) # [1,1,1]

