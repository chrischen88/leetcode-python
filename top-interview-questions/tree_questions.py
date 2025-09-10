from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth_iterative(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    max_depth = 0
    queue = [root]
    while queue:
        max_depth += 1
        for _ in range(len(queue)):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return max_depth

def max_depth_recursive(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return 1 + max(max_depth_recursive(root.left), max_depth_recursive(root.right))

def is_symmetric_iterative(root: Optional[TreeNode]) -> bool:
    queue = [root]
    while queue:
        for _ in range(len(queue)):
            node = queue.pop(0)
            if node is None:
                continue
            if node.left:
                queue.append(node.left)
            else: queue.append(None)
            if node.right:
                queue.append(node.right)
            else: queue.append(None)
        front = 0
        back = len(queue)-1
        print([None if node is None else node.val for node in queue])
        while front < back:
            front_val = None if queue[front] is None else queue[front].val
            back_val = None if queue[back] is None else queue[back].val
            if front_val != back_val:
                return False
            else:
                front+=1
                back-=1
    return True

if __name__ == "__main__":
    three_node = TreeNode(3, None, None)
    two_node = TreeNode(2,None,three_node)
    root_node = TreeNode(1,two_node, two_node)
    print(is_symmetric_iterative(root_node))