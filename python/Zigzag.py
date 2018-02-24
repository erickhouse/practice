# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

# For example:
# Given binary tree [3,9,20,null,null,15,7]

# input

#   3
#  / \
# 9  20
#   /  \
#  15   7

# output

# [
#   [3],
#   [20,9],
#   [15,7]
# ]

# This implementation is quite expensive on an unbalanced tree. A better implementation would be using dfs to get O(n) time
# Future: implement as dfs
import math

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def zigzagLevelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root:
        return []
        
    i = 0
    level = 0
    target = 0

    queue = [root]
    curr_seq = []
    result = []

    is_left = True

    while(queue):
        curr = queue.pop(0)

        if curr is None:
            queue.append(None)
            queue.append(None)
        else:
            if is_left:
                curr_seq.append(curr.val)
            else:
                curr_seq.insert(0, curr.val)
            queue.append(curr.left)
            queue.append(curr.right)

        if i == target:
            if not curr_seq:
                return result
                
            level += 1
            i = 0
            target = math.pow(2, level)
            result.append(curr_seq)
            curr_seq = []
            is_left = not is_left

        i += 1  


