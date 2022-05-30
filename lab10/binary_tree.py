

class BinaryTree:

    def __init__(self):

        self._root = None
        self._current_iterator = None

        pass

    def __getitem__(self, key):

        found_node, node_parent, right_node = self._find_node_by_key(key)

        return found_node.value if found_node is not None else None

    def __setitem__(self, key, value):

        found_node = self._add_or_find_node_by_key(key)[0]
        found_node.value = value

    def __str__(self):
        return str(self.top_to_bottom_list())

    def remove(self, key):
        found_node, node_parent, right_node = self._find_node_by_key(key)

        if found_node is None:
            return None

        value = found_node.value

        if found_node.right is not None:
            replacement, replacement_parent = self._find_the_smallest_key_in_the_branch(found_node.right, found_node)

            if replacement_parent is not found_node:
                replacement_parent.left = replacement.right
            else:
                found_node.right = replacement.right

            found_node.key = replacement.key
            found_node.value = replacement.value

        elif found_node.left is not None:
            replacement, replacement_parent = self._find_the_biggest_key_in_the_branch(found_node.left, found_node)

            if replacement_parent is not found_node:
                replacement_parent.right = replacement.left
            else:
                found_node.left = replacement.left

            found_node.key = replacement.key
            found_node.value = replacement.value

        elif node_parent is not None:

            if right_node:
                node_parent.right = None
            else:
                node_parent.left = None

        else:
            self._root = None

        return value

    def remove_by(self, comparator):

        list_to_remove = self.get_by(comparator)

        for key, item in list_to_remove:
            self.remove(key)

    def get_by(self, comparator):
        return [(x.key, x.value) for x in self._top_to_bottom_node_iterator() if comparator(x.key, x.value)]

    def top_to_bottom_list(self):
        return [(x.key, x.value) for x in self._top_to_bottom_node_iterator()]

    def _top_to_bottom_node_iterator(self):

        nodes_to_iterate_over = [self._root, ]
        next_nodes_to_iterate_over = []

        while len(nodes_to_iterate_over) > 0:
            for node in nodes_to_iterate_over:

                if node.left is not None:
                    next_nodes_to_iterate_over.append(node.left)
                if node.right is not None:
                    next_nodes_to_iterate_over.append(node.right)

                yield node

            nodes_to_iterate_over = next_nodes_to_iterate_over
            next_nodes_to_iterate_over = []

    def _find_node_by_key(self, key):

        current_node = self._root
        node_parent = None
        right_node = False

        while current_node is not None and key != current_node.key:
            node_parent = current_node
            right_node = hash(key) > hash(current_node.key)
            current_node = current_node.right if right_node else current_node.left

        return current_node, node_parent, right_node

    def _add_or_find_node_by_key(self, key):

        found_node, node_parent, right_node = self._find_node_by_key(key)

        if found_node is not None:
            return found_node, node_parent, False
        elif node_parent is not None:
            if right_node:
                node_parent.right = BinaryTree.Node(key, None)
                return node_parent.right, node_parent, True
            else:
                node_parent.left = BinaryTree.Node(key, None)
                return node_parent.left, node_parent, True
        else:
            self._root = BinaryTree.Node(key, None)
            return self._root, None, True

    @staticmethod
    def _find_the_smallest_key_in_the_branch(node, parent):

        node_parent = parent
        current_node = node

        while current_node.left is not None:
            node_parent = current_node
            current_node = current_node.left

        return current_node, node_parent

    @staticmethod
    def _find_the_biggest_key_in_the_branch(node, parent):

        node_parent = parent
        current_node = node

        while current_node.right is not None:
            node_parent = current_node
            current_node = current_node.right

        return current_node, node_parent

    class Node:

        def __init__(self, key, value):

            self.key = key
            self.value = value

            self.left = None
            self.right = None
