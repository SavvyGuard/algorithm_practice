import utilities
import collections

binary_tree = utilities.get_random_tree(3)

def bfs(path, quarry, waiting = None):
    node = path[-1]
    if node.value == quarry:
        return path
    if waiting is None:
        waiting = collections.deque()
    if not waiting and not node.left and not node.right:
        return False
    elif not node.left and not node.right:
        return bfs(waiting.popleft(), quarry, waiting)
    if node.left:
        waiting.append(path + [node.left])
    if node.right:
        waiting.append(path + [node.right])
    return bfs(waiting.popleft(),quarry, waiting)

print binary_tree.as_dict()
print bfs([binary_tree], 3)
