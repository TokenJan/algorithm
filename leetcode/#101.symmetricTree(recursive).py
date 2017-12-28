import tree

def isSymmetric(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if root is None:
        return True

    return isMirror(root.left, root.right)

def isMirror(left, right):
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False
    elif left.val == right.val:
        return isMirror(left.left, right.right) and isMirror(left.right, right.left)
    else:
        return False

if __name__ == '__main__':
    root_symmetric = tree.deserialize('[-1, 0, 0, 1, 3, 3, 1]')
    root_asymmetric = tree.deserialize('[-1, 0, 0, 1, 3, 3]')
    assert(isSymmetric(root_symmetric) == True)
    assert(isSymmetric(root_asymmetric) == False)
    print("Pass")