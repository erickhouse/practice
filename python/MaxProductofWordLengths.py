
#Given a string array words, find the maximum value of length(word[i]) * length(word[j]) 
#where the two words do not share common letters. 
#You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

#Example 1:
#Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
#Return 16
#The two words can be "abcw", "xtfn".

#Example 2:
#Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
#Return 4
#The two words can be "ab", "cd".

#Example 3:
#Given ["a", "aa", "aaa", "aaaa"]
#Return 0
#No such pair of words.


def maxProduct(words):
    max = 0
    for i in range(0, len(words)):
        for j in range(0, len(words)):
            intersect = set(words[i]) & set(words[j])
            if(len(intersect) == 0):
                cmax = len(words[i]) * len(words[j])
                if(cmax > max):
                    max = cmax
    return max

                
