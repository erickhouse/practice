/**
  * Created by EHouse on 7/11/2017.
  */
object validateBinaryTree extends App{

   class TreeNode(var _value: Int) {
     var value: Int = _value
     var left: TreeNode = null
     var right: TreeNode = null
   }

  var root = new TreeNode(2)
  root.left = new TreeNode(1)
  root.right = new TreeNode(3)

  def isValidBST(root: TreeNode): Boolean = {
    if(root == null) true
    else if(root.left == null && root.right == null) true
    else util(root, Float.MinValue, Float.MaxValue)
  }

  def util(current:TreeNode, min:Float, max:Float) :Boolean = {
    if(current == null) true
    else if(current.value < min || current.value > max || current.value == min || current.value == max) false
    else util(current.left, min, current.value) && util(current.right, current.value, max)
  }

  println(isValidBST(root))

}
