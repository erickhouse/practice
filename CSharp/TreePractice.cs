using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace InterviewPractice
{
    class TreePractice
    {
         private TreeNode root = null;

        private bool isEmpty()
        {
            return (root == null);
        }

        public void insert(TreeNode toInsert)
        {
            bool isInserted = false;
            insertHelper(root, toInsert, ref isInserted);
        }

        private void insertHelper(TreeNode current, TreeNode toInsert, ref bool isInserted)
        {
            if (isEmpty())
            {
                root = toInsert;
                return;
            }

            if (isInserted)
            {
                return;
            }

            if (toInsert.data < current.data)
            {
                if (current.left == null)
                {
                    current.left = toInsert;
                    isInserted = true;
                }

                insertHelper(current.left, toInsert, ref isInserted);
            }
            else
            {
                if (current.right == null)
                {
                    current.right = toInsert;
                    isInserted = true;
                }

                insertHelper(current.right, toInsert, ref isInserted);
            }
        }

        public void printInOrder()
        {
            inOrderHelper(root);
        }

        private void inOrderHelper(TreeNode current)
        {
            if (current != null)
            {
                inOrderHelper(current.left);
                Debug.WriteLine(current.data);
                inOrderHelper(current.right);
            }
        }

        public class TreeNode
        {
            public int data;
            public TreeNode left = null;
            public TreeNode right = null;

            public TreeNode(int d)
            {
                data = d;
            }
        }
    }
}
