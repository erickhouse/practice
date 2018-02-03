
//PROBLEM 1: GRAPH COLORING.
//
//Given a graph, want to give each node a color such that no
//  two neighbors have the same color.  Goal is to do this with the fewest
//  total number of different colors (easy to do with n colors).
//
//E.g., pentagon.
//
//  Think of problem of scheduling exams.  Each node is a class, and there
//  is an edge between two if lots of students are taking both classes.
//  Goal is to use fewest number of different time slots such that no two
//  adjacent nodes are given the same time slot.  In compilers, graph
//coloring comes up when assigning variables to registers.
//
//Unfortunately, graph-coloring problem is NP-hard.  In fact, even
//telling if possible to color with <= 3 colors is NP-hard in general.
//  But, 2-coloring problem (color with 2 colors if possible else say
//"impossible") is easy.  How to do it?
//
//2-coloring: given graph G, find a 2-coloring if one exists, else
//output "not 2-colorable".

object colorGraph extends App{
  case class Node(val id:Int, var neighbors: Set[Node], var color:Int, var visited:Boolean){
    override def equals(that: Any) = that match {
      case that:Node => that.id == this.id
      case _ => false
    }
    override def toString : String = id.toString
  }

  var n3 = Node(2, Set(), -1, false)
  var n2 = Node(1, Set(), -1, false)
  var n1 = Node(0, Set(), -1, false)
  var n4 = Node(3, Set(), -1, false)

  n1.neighbors = Set(n2,n3,n4)
  n2.neighbors = Set(n1,n3,n4)
  n3.neighbors = Set(n2,n1)
  n4.neighbors = Set(n1,n2)

  def color(node: Node): Unit = {

    val colors = 0 to node.neighbors.size

    node.visited = true
    for(n <- node.neighbors if !n.visited) {
      color(n)
    }

    val marked = (node.neighbors + node).filter(_.color != -1).map(_.color).toList
    node.color = (colors diff marked).head

  }

  color(n1)

  println(n1.color)
  println(n2.color)
  println(n3.color)
  println(n4.color)
}
