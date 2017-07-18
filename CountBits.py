



#count the number of bits (1's) in a sequence

# For num = 5 you should return [0,1,1,2,1,2].

# example : [0, 1, 10, 110, 100, 101 ]

def countBits(num):

    def count(i):
        if(i <= 0):
            return 0
        else:
            mod = i % 2
            return mod + count(i // 2)

        return [count(i) for i in range(num + 1)]

