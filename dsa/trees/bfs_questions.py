import collections

def binary_tree_rightside(root) -> list:
    q = collections.deque([root])
    view = list()
    while q:
        rightmost = None
        for _ in range(len(q)):
            curr = q.popleft()
            if curr:
                q.append(curr.left)
                q.append(curr.right)
            rightmost = curr
        if rightmost:
            view.append(rightmost)
    return view

            

