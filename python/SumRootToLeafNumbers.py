
#Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

#An example is the root-to-leaf path 1->2->3 which represents the number 123.

#Find the total sum of all root-to-leaf numbers.

#For example,

#    1
#   / \
#  2   3
#The root-to-leaf path 1->2 represents the number 12.
#The root-to-leaf path 1->3 represents the number 13.

#Return the sum = 12 + 13 = 25.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def calcSum(root, seq):
            if root is None: 
                return 0
            elif root.left is None and root.right is None:         
                sum = root.val
                for i in range(0, len(seq)):
                    sum += seq[i] * pow(10, (i + 1)) 
                return sum
            else:
                seq.insert(0, root.val)
                res = calcSum(root.left, seq) + calcSum(root.right, seq)
                seq.pop(0)
                return res

        return calcSum(root, list([]))





