using System;
using System.Collections.Generic;
using System.Text;

namespace InterviewPractice
{
    class BinaryTree
    {
        private Node root;
        private class Node
        {
            public string data = null;
            public Node left = null;
            public Node right = null;
            public bool visited = false;
        }

        public BinaryTree()
        {
            root = null;
        }

        //creates a balanced binary tree (not BST)
        //by adding in elements from left to right 
        //once a row is filled it goes to the next row 
        public void Insert(string data)
        {
            if (root == null)
            {
                root = new Node();
                root.data = data;
                return;
            }

            Queue<Node> q = new Queue<Node>();
            root.visited = true;
            q.Enqueue(root);
    
            while (q.Count != 0)
            {
                Node current = q.Dequeue();
                
                if (current.left == null)
                {
                    current.left  = new Node();
                    current.left.data = data;
                    break;                  
                }
                if (current.right == null)
                {
                    current.right = new Node();
                    current.right.data = data;
                    break;
                }

                if (current.left.visited == false)
                {
                    current.left.visited = true;
                    q.Enqueue(current.left);
                }
                if (current.right.visited == false)
                {
                    current.right.visited = true;
                    q.Enqueue(current.right);
                }

            }
            resetVisitedAll();
        }

        public void PrintInOrder()
        {
            inOrderHelper(root);
        }

        //Looks for the data in the tree, if it finds it
        //then it returns the path representaion of the location of the object in the tree
        // A/B/C 
        // A = grandparent, B = parent, C = child
        public string GetPath(string data)
        {
            bool found = false;
            Stack<string> path = new Stack<string>();
            getPathHelper(root, data, ref path, ref found);

            StringBuilder finalPath = new StringBuilder();
            var arrayPath = path.ToArray();

            if(found)
            {
                for(int i = path.Count - 1; i >= 0; i--)
                {
                    finalPath.Append(arrayPath[i]);
                    finalPath.Append('/');
                }
                finalPath.Remove(finalPath.Length - 1, 1);
            }
            return finalPath.ToString();           
        }

        private void getPathHelper(Node current, string data, ref Stack<string> path, ref bool found)
        {
            if(found || current == null)
            {
                return;
            }

            path.Push(current.data);
            getPathHelper(current.left, data, ref path, ref found);
            getPathHelper(current.right, data, ref path, ref found);

            if(!found)
            {
                if(data == current.data)
                {
                    found = true; 
                    return;        
                }
                path.Pop();
            }
            
        }

        private void resetVisitedAll()
        {
            resetVisitedAllHelper(root);
        }

        private void resetVisitedAllHelper(Node current)
        {
            if (current == null)
            {
                return;
            }

            resetVisitedAllHelper(current.left);
            current.visited = false;
            resetVisitedAllHelper(current.right);
        }

        private void inOrderHelper(Node current)
        {
            //Debug.WriteLine("level");
            if (current == null)
            {
                return;
            }           
            inOrderHelper(current.left);  
            Console.WriteLine(current.data);           
            inOrderHelper(current.right);
        }

    }


}
