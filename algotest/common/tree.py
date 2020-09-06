# -*- coding: utf-8 -*-


class BinaryNode(object):
    def __init__(self, node):
        """
        :param node: ID of this node
        x: position on x-axis
        y: position on y-axis
        """
        self.id = node
        # left_leaf: ID of left leaf
        self.left_leaf = 2 * node + 1
        # right_leaf:  ID of right leaf
        self.right_leaf = 2 * (node + 1)


class BinaryTree(object):
    def __init__(self, depth):
        self.depth = depth
        self.nb_node = 2 ** (depth + 1) - 1
        self.nodes = [BinaryNode(index) for index in range(self.nb_node)]

        # Generate coordinates
        self.positions = self.nb_node * [0]
        for index in range(2 ** depth - 1):
            node = self.nodes[index]
            y = self.positions[index]
            self.positions[node.left_leaf] = y - 1
            self.positions[node.right_leaf] = y + 1

    @property
    def vertical_sum(self):
        data = {}
        for position, node in zip(self.positions, self.nodes):
            if position in data.keys():
                data[position] += node.id
            else:
                data[position] = node.id

        return data
