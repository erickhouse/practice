using System.Collections.Generic;
using System;

public class NodeGraph
{
    private Dictionary<int,Node> lookup = new Dictionary<int,Node>();

    private class Node
    {
        private int _id;
        public string Value;
        public List<Node> adjacent = new List<Node>();
        public Node(int id)
        {
            _id = id;
        }
        public Node(int id, string value)
        {
            _id = id;
            Value = value;
        }
    }
    private Node getNode(int id)
    {
        if(lookup.ContainsKey(id))
        {
            return lookup[id];
        }
        var node = new Node(id);
        lookup[id] = node;
        return node;
    }
    public void AddEdge(int source, int destination)
    {
        var node = getNode(source);
        node.adjacent.Add(getNode(destination));
    }
    
}