class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
      if root is None:
        return False
      else:
        # Only leaf could return true
        if sum == root.val and root.left is None and root.right is None:
          return True
        else:
          return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
