
using System.Collections.Generic;

namespace InterviewPractice
{
    //determines if there are 3 numbers in the set that all add up to equal the target
    //runtime is O(N^2)
    public static class FindTarget
    {
        public static bool FindTargetFunc(HashSet<int> hashSet, int target)
        {
            //edge cases
            if(hashSet.Count < 3 || target < 2) //1 + 1 + 0 
            {
                return false;
            }

            foreach(var a in hashSet)
            {
                int newTarget = target - a;
                foreach(var b in hashSet)
                {
                    int c = newTarget - b;
                    if (hashSet.Contains(c))
                    {
                        return true;
                    }
                }
            }
            return false;
        }
    }
}
