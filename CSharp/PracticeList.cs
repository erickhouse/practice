using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace InterviewPractice
{
    class PracticeList
    {
        private Node head;

        //private constructor
        private PracticeList()
        {
            head = new Node(0);
        }

        public void findKth()
        {
             Node found = null;

             findKthHelper(this.head, 2, ref found);

             if (found != null)
             {
                 Debug.WriteLine("found= " + found.data);
             }
             else
             {
                 Debug.WriteLine("found = null");
             }

        }

        private int findKthHelper(Node current, int k, ref Node found)
        {
            if (current == null)
            {
                return 0;
            }

            int i =  findKthHelper(current.next, k, ref found) + 1;
            Debug.WriteLine("i = " + i);

            if (i == k)
            {
                
                found = current;
                Debug.WriteLine("got here" + found.data);
            }

            return i;
        }

        public void print()
        {
            Node current = head.next;
            if (current == null)
            {
                return;
            }
            Debug.WriteLine("");

            while (current.next != null)
            {
                Debug.Write(current.data + "-> ");
                current = current.next;
            }
            Debug.Write(current.data);

            Debug.WriteLine("");
        }

        public void appendToTail(int data)
        {
            Node n = new Node(data);

            Node current = head.next;

            if (current == null)
            {
                head.next = n;
                return;
            }

            while (current.next != null)
            {
                current = current.next;
            }

            current.next = n;
        }

        public void removeNode(int data)
        {
            Node current = head.next;
            Node prev;

            if (current == null)
            {
                return;
            }

            while (current.next != null)
            {
                prev = current;
                current = current.next;

                if (current.data == data)
                {
                    prev.next = current.next;
                    current.next = null;
                }
           
            }
           
        }

        public string reverseString(string str)
        {
            if (str == null || str.Length == 1) { return str; }

            StringBuilder builder = new StringBuilder(str);
            
            int start = 0;
            int end = builder.Length - 1;

            while(start <= end)
            {
                char temp = builder[end];
                builder[end] = builder[start];
                builder[start] = temp;

                start++;
                end--;
            }

            return builder.ToString();
        }


        class Node
        {
            public int data;
            public Node next = null;

            public Node(int d)
            {
                data = d;
            }
        }
    }
}
