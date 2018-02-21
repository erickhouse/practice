# Given a set of distinct integers, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# For example,
# If nums = [1,2,3], a solution is:

#[
#  [3],
#  [1],
#  [2],
#  [1,2,3],
#  [1,3],
#  [2,3],
#  [1,2],
#  []
#]

def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    def combo(nums):
        if len(nums) == 1:
            return [nums]

        res = []
        res.append([nums[0]])

        for r in combo(nums[1:]):
            res.append(r)
            res.append([nums[0]] + r)

        return res
        
    res = combo(nums)
    res.insert(0,[])
    return res