
def merge(a,b):
    
    merged = []

    while a and b:
        if a[0] <= b[0]:
            merged.append(a.pop(0))
        else:
            merged.append(b.pop(0))
    if a:
        return merged + a
    else:
        return merged + b


def mergeSort(data):
    
    size = len(data)

    if size <= 1:
        return data

    mid = (size // 2)

    left = mergeSort(data[:mid])
    right = mergeSort(data[mid:])

    return merge(left, right)





unsorted = [2,3,1,5,12,3,7,4]

complete = mergeSort(unsorted)
print(complete)
