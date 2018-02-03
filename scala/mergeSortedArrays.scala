/**
  * Given two collections with unique values that are already sorted,
  * combine them into a sorted array
  */
object mergeSortedArrays extends App{

  val first = List(1,3,5,6,15)
  val second = List(2,7)

  def merge(x:List[Int], y: List[Int]) : List [Int] = {
    if(x.isEmpty && y.isEmpty) List()
    else if(x.isEmpty) y.head :: merge(x, y.tail)
    else if(y.isEmpty) x.head :: merge(x.tail, y)
    else {
      if(x.head < y.head) x.head :: merge(x.tail, y)
      else y.head :: merge(x, y.tail)
    }
  }


  println(merge(first, second))

}
