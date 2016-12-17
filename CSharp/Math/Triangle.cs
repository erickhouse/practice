using System;

public class Triangle
{
    public static bool IsTriangle(int a, int b, int c)
    {
        int[] sides = {a,b,c};
        if(a > 0 && b > 0 && c > 0)
        {
            int largest = -1;
            foreach(var side in sides)
            {
                if(side > largest)
                {
                    largest = side;
                }
            }
            if(a == largest)
            {
                return a < b + c;
            }
            if(b == largest)
            {
                return b < a + c;
            }
            return c < a + b;
            
        }
        return false;
    }
}