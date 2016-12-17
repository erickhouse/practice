public class TreeSwap {
    public static TreeNode InvertTree(TreeNode root) {
        //TODO
        return root;
    }
    
    private void swap(TreeNode current)
    {
      if(current == null)
        return;
        
      swap(current.Left);
      swap(current.Right);
      
      TreeNode buf = current.Left;
      current.Left = current.Right;
      current.Right = buf;
    }

  public class TreeNode
  {
    public int Value { get; set; }
    public TreeNode Left { get; set; }
    public TreeNode Right { get; set; }
  }
}

