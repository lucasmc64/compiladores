class Node:
    def __init__(self, token, parent):
        self.token = token
        self.parent = parent
        self.child = []

def newNode(token, parent):
    return Node(token, parent)
