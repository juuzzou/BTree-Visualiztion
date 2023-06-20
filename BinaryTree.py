class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._add(value, self.root)

    def _add(self, value, node):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._add(value, node.left)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._add(value, node.right)

    def remove(self, value):
        if self.root:
            self.root = self._remove(value, self.root)

    def _remove(self, value, node):
        if not node:
            return node

        if value < node.value:
            node.left = self._remove(value, node.left)
        elif value > node.value:
            node.right = self._remove(value, node.right)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            temp = self._find_min(node.right)
            node.value = temp.value
            node.right = self._remove(temp.value, node.right)

        return node

    def search(self, value):
        if self.root:
            found = self._search(value, self.root)
            if found:
                return True
            return False
        else:
            return False

    def _search(self, value, node):
        if value == node.value:
            return node
        elif value < node.value and node.left:
            return self._search(value, node.left)
        elif value > node.value and node.right:
            return self._search(value, node.right)

    def find_max(self):
        if self.root is None:
            return None
        else:
            return self._find_max(self.root)

    def _find_max(self, node):
        if node.right is None:
            return node
        else:
            return self._find_max(node.right)

    def find_min(self):
        if self.root is None:
            return None
        else:
            return self._find_min(self.root)

    def _find_min(self, node):
        if node.left is None:
            return node
        else:
            return self._find_min(node.left)

    def inorder_traversal(self):
        values = []
        self._inorder_traversal(self.root, values)
        return values

    def _inorder_traversal(self, node, values):
        if node:
            self._inorder_traversal(node.left, values)
            values.append(node.value)
            self._inorder_traversal(node.right, values)

    def find_neighbors(self, value):
        if self.root:
            return self._find_neighbors(value, self.root)

    def _find_neighbors(self, value, node, previous_node=None, next_node=None):
        if node:
            if value < node.value:
                next_node = node
                return self._find_neighbors(value, node.left, previous_node, next_node)
            elif value > node.value:
                previous_node = node
                return self._find_neighbors(value, node.right, previous_node, next_node)
            else:
                if node.left:
                    temp = node.left
                    while temp.right:
                        temp = temp.right
                    previous_node = temp
                if node.right:
                    temp = node.right
                    while temp.left:
                        temp = temp.left
                    next_node = temp
                return previous_node, next_node
        else:
            return previous_node, next_node
