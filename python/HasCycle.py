
def canFinish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    def isValid(pair):
        return pair[0] != pair[1]

    def isNext(node, nextNode):
        return node[1] == nextNode[0]
        
    if len(prerequisites) < numCourses:
        return True
      
    visited = list()

    def hasCycle(path):                     
        for nextNode in prerequisites:
            if nextNode not in visited and nextNode not in path:

                if isNext(path[-1], nextNode):

                    if not isValid(nextNode):
                        return False

                    visited.append(nextNode)

                    for node in path:
                        if nextNode[1] == node[0]: 
                            return False

                    path.append(nextNode)
                    return hasCycle(path)

        return True

    front = prerequisites[0]
    visited.append(front)
    return hasCycle([front])


vals = [[2,0],[0,1],[1,2]]

print(canFinish(2, vals))