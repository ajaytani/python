import collections
class Node():
    def __init__(self,key):
        self.left = None
        self.right = None
        self.value = key

def levelOrderTree(tree):

    if not tree:
        return
    currentcount = 1
    nextcount = 0
    nodes = collections.deque([tree])
    while len(nodes) != 0:

        currentnode = nodes.popleft()
        currentcount -= 1
        print currentnode.value,

        if currentnode.left:
            nodes.append(currentnode.left)
            nextcount += 1
        if currentnode.right:
            nodes.append(currentnode.right)
            nextcount += 1

        if currentcount == 0:
            print '\n'
            currentcount, nextcount = nextcount, currentcount



root = Node(1)
root.left = Node(2)
root.right = Node(3)

levelOrderTree(root)
