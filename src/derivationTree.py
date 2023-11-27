class Node:
    def __init__(self, token):
        self.token = token
        self.child = []

def newNode(token):
    return Node(token)
