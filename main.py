class TreeNode:
  
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_balanced(root):
   
    def check(node):
       
        if node is None:
            return True, 0

        left_bal, left_h = check(node.left)
        right_bal, right_h = check(node.right)

        # If either subtree is already unbalanced, skip further checks
        if not left_bal or not right_bal:
            return False, 0

        # Check the height difference
        if abs(left_h - right_h) > 1:
            return False, 0

        # Balanced: height is max of subtrees + 1
        return True, max(left_h, right_h) + 1

    balanced, _ = check(root)
    return balanced


if __name__ == "__main__":
    # Optional: quick manual tree
    #   1
    #  / \
    # 2   3
    left = TreeNode(2)
    right = TreeNode(3)
    root = TreeNode(1, left, right)
    print(is_balanced(root))
