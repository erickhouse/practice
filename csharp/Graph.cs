
using System;
using System.Collections.Generic;


namespace InterviewPractice
{

    public class Graph
    {
        public void Print()
        {
            foreach(var edge in Edges)
            {
                edge.Print();
            }
        }
        public void BuildDefaultGraph()
        {
            var a = new Vertex("A");
            var b = new Vertex("B");
            var c = new Vertex("C");
            var d = new Vertex("D");
            var e = new Vertex("E");
            var f = new Vertex("F");
            Verticies = new List<Vertex>{a,b,c,d,e,f};

            Edges = new List<Edge>{
                new Edge(a,b),
                new Edge(c,d),
                new Edge(d,a),
                new Edge(b,f),
                new Edge(f,e)
            };
        }

        public List<Vertex> Verticies; //= new List<Vertex>();
        public List<Edge> Edges; //= new List<Edge>(); 
        public class Vertex
        {
            public Vertex(string label)
            {
                Label = label;
            }
            public string Label;                  
        }

        public class Edge
        {
            public Edge(Vertex a, Vertex b, int weight = 0, bool directed = false)
            {
                A = a;
                B = b;
                Weight = weight;
                isDirected = directed;
            }
            private bool isDirected;
            public Vertex A;
            public Vertex B;
            public int Weight;

            public void Print()
            {
                if(isDirected)
                {
                    Console.WriteLine(A.Label + "-->" + B.Label);
                } 
                else
                {
                    Console.WriteLine(A.Label + "---" + B.Label);
                }       
            }
        }
    }
}
