/**
  * Created by EHouse on 7/11/2017.
  */
object permutations extends App{

  def permute(nums: Array[Int]): List[List[Int]] = {

    if(nums.length == 1) return List(nums.toList)
    var tally : List[List[Int]]  = List()

    for(value <- nums) {
      val res = permute(nums.filter(_ != value))
      tally = tally ::: res.map(value :: _)
    }
    return tally
  }

}
