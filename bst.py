class Node:
    def __init__(self, key):
        self.left: Node | None = None
        self.right: Node | None = None
        self.val: int = key

    def __str__(self, level=0, prefix="Tree:"):
        ret = "  " * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L:")
        if self.right:
            ret += self.right.__str__(level + 1, "R:")
        return ret


class BSTree:
    root: Node | None = None

    def __init__(self):
        return

    def __str__(self):
        if self.root:
            return f"{self.root}"

        return "The tree is empty."

    def insert(self, key: int):
        self.root = self.__insert(self.root, key)

    def __insert(self, root: Node | None, key: int):
        if root is None:
            return Node(key)
        else:
            if key < root.val:
                root.left = self.__insert(root.left, key)
            else:
                root.right = self.__insert(root.right, key)
        return root

    @property
    def min_node(self):
        min = self.__min_value_node(self.root)
        if not min:
            return None
        return min.val

    @property
    def max_node(self):
        max = self.__max_value_node(self.root)
        if not max:
            return None
        return max.val

    @property
    def sum(self):
        return self.__sum(self.root)

    def __sum(self, node: Node | None, acc: int = 0) -> int:
        if not node:
            return 0

        return node.val + self.__sum(node.right, acc) + self.__sum(node.left, acc)

    def __min_value_node(self, node: Node | None):
        current = node
        while current.left:
            current = current.left
        return current

    def __max_value_node(self, node: Node | None):
        current = node
        while current.right:
            current = current.right
        return current

    def delete(self, key: int):
        self.__delete(self.root, key)

    def __delete(self, root: Node | None, key: int):
        if not root:
            return root

        if key < root.val:
            root.left = self.__delete(root.left, key)
        elif key > root.val:
            root.right = self.__delete(root.right, key)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp
            root.val = self.__min_value_node(root.right).val
            root.right = self.__delete(root.right, root.val)
        return root


if __name__ == "__main__":
    # Test
    tree = BSTree()
    print(tree)
    print(f"SUM:{tree.sum}\n")

    values = [5, 8, 6, 4, 2, -1, 7]
    for v in values:
        tree.insert(v)

    print(f"Add values: {values}")
    print(tree)
    print(f"MIN:{tree.min_node} == {min(values)}")
    print(f"MAX:{tree.max_node} == {max(values)}")
    print(f"SUM:{tree.sum} == {sum(values)}\n")

    del_values = [7, 4]
    for v in del_values:
        tree.delete(v)

    print(f"Delete values: {del_values}")
    print(tree)
    temp = list(set(values) - set(del_values))
    print(f"Values: {temp}")
    print(f"MIN:{tree.min_node} == {min(temp)}")
    print(f"MAX:{tree.max_node} == {max(temp)}")
    print(f"SUM:{tree.sum} == {sum(temp)}\n")

    add_values = [10, 1, 12, -3]
    for v in add_values:
        tree.insert(v)

    print(f"Add values: {add_values}")
    print(tree)
    temp = list(temp) + add_values
    print(f"Values: {temp}")
    print(f"MIN:{tree.min_node} == {min(temp)}")
    print(f"MAX:{tree.max_node} == {max(temp)}")
    print(f"SUM:{tree.sum} == {sum(temp)}")
