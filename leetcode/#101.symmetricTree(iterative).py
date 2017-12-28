import tree

def isSymmetric(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if root is None:
        return True
    else:
        stack = [[root.left, root.right]]
        while len(stack) != 0:
            left, right = stack.pop()
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            elif left.val == right.val:
                stack.append([left.left, right.right])
                stack.append([left.right, right.left])
            else:
                return False
        return True

if __name__ == '__main__':
    root_symmetric = tree.deserialize('[-1, 0, 0, 1, 3, 3, 1]')
    root_asymmetric = tree.deserialize('[-1, 0, 0, 1, 3, 3]')
    assert(isSymmetric(root_symmetric) == True)
    assert(isSymmetric(root_asymmetric) == False)
    print("Pass")