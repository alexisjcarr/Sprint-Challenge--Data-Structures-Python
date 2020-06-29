from stack import Stack
from queue import Queue


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # take the current value of our node (self.value)    
        # compare to the new value we want to insert
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        # compare the target to current value
        # if current value < target
        found = False
        if self.value < target:
            # check the left subtree (self.left.contains(target))
            # if you cannot go left, return False
            if self.right is None:
                return False
            found = self.right.contains(target)

        # if current value >= target
        if self.value >= target:
            # check if right subtree contains target
            # if you cannot go right, return False
            if self.left is None:
                return False
            found = self.left.contains(target)

        return found

    # Return the maximum value found in the tree
    def get_max(self):
        # the largest value will always be to the right of the current node
        # if we can go right, lets find the largest number there by calling get_max on the right subtree
        # if we cannot go right, return the current value
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call function on the current value fn(self.value)
        # if you can go left, call for_each on the left tree
        # if you can go right, call for_each on the right tree

        if self.left:
            self.left.for_each(fn)

        fn(self.value)

        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # Algorithm Inorder(tree)
        # 1. Traverse the left subtree, i.e., call Inorder(left-subtree)
        # 2. Visit the root.
        # 3. Traverse the right subtree, i.e., call Inorder(right-subtree)
        if node is None:
            return

        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # create a queue for nodes
        # add the first node to the queue
        # while queue is not empty
            # remove the first node from the queue
            # print the removed node 
            # add all children into the queue

        q = Queue()
        q.enqueue(node)

        while q.size > 0:
            n = q.dequeue()
            print(n.value)

            if n.left:
                q.enqueue(n.left)
            if n.right:
                q.enqueue(n.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # create a stack for nodes
        # add the first node to the stack
        # while the stack is not empty
            # get the current node from the top of the stack
            # print that node
            # add all children to the stack
        s = Stack()
        s.push(node)

        while s.size > 0:
            n = s.pop()
            print(n.value)

            if n.left:
                s.push(n.left)
            if n.right:
                s.push(n.right)


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        # 1. Visit the root.
        # 2. Traverse the left subtree, i.e., call Preorder(left-subtree)
        # 3. Traverse the right subtree, i.e., call Preorder(right-subtree)

        if node is None:
            return

        print(node.value)
        self.pre_order_dft(node.left)
        self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        # 1. Traverse the left subtree, i.e., call Postorder(left-subtree)
        # 2. Traverse the right subtree, i.e., call Postorder(right-subtree)
        # 3. Visit the root.

        if node is None:
            return

        self.post_order_dft(node.left)
        self.post_order_dft(node.right)
        print(node.value)

    def __repr__(self):
        return f'value: {self.value}\nleft: {self.left}\nright: {self.right}'