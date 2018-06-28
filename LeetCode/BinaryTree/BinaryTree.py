# coding=utf-8

class BinaryNode:
    def __init__(self, value=-1, lchild=None, rchild=None):
        """
        :param value: value of a node
        :param lchild:  left child of this node
        :param rchild:  right child of this node
        """
        self.value = value
        self.lchild = lchild
        self.rchild = rchild


class BinaryTree:
    def __init__(self):
        self.root = BinaryNode()
        self.myQueue = []

    def add(self, value):
        """
        construct a binary tree
        :param value:  node value
        :return:
        """
        node = BinaryNode(value)
        if self.root.value == -1: # if root is null, assign node to root
            self.root = node
            self.myQueue.append(self.root)
        else:
            treeNode = self.myQueue[0] # nodes exist in this queue lack left child or right child
            if treeNode.lchild == None:
                treeNode.lchild = node
                self.myQueue.append(treeNode.lchild)
            else:
                treeNode.rchild = node
                self.myQueue.append(treeNode.rchild)
                # treeNode have both left child and right child, pop it from the queue
                self.myQueue.pop(0)


    def pre_recursive(self, root):
        """
        traverse a binary tree use pre-order
        :param root: root node of a tree
        :return:
        """
        if root == None:
            return
        print(str(root.value) + ' ', end="")
        self.pre_recursive(root.lchild)
        self.pre_recursive(root.rchild)

    def in_recursive(self, root):
        """
        traverse a binary tree use in-order
        :param root: root node of a tree
        :return:
        """
        if root == None:
            return

        self.in_recursive(root.lchild)
        print(str(root.value) + " ", end="")
        self.in_recursive(root.rchild)

    def post_recursive(self, root):
        """
        traverse a binary tree use post-order
        :param root: root node of a tree
        :return:
        """
        if root == None:
            return
        self.post_recursive(root.lchild)
        self.post_recursive(root.rchild)
        print(str(root.value) + ' ', end="")

    def pre_stack(self, root):
        """
        pre-order traverse binary tree use stack, root, lchild, rchild
        :param root: root node of a tree
        :return:
        """
        if root == None:
            return

        stack = []
        node = root
        while node or stack:
            while node:
                print(str(node.value) + ' ', end="")
                stack.append(node)
                node = node.lchild
            node = stack.pop()
            node = node.rchild

    def in_stack(self, root):
        """
        in-order traverse binary tree use stack, lchild root rchild
        :param root: root node of a tree
        :return:
        """

        if root == None:
            return

        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.lchild
            node = stack.pop()
            print(str(node.value) + ' ', end="")
            node = node.rchild

    def post_stack(self, root):
        """
        post order traverse binary tree use stack, lchild rchild root
        :param root: root node of a binary tree
        :return:
        """
        if root == None:
            return

        stack1 = []
        stack2 = []
        node = root
        stack1.append(node)
        while stack1:
            node = stack1.pop()
            stack2.append(node) # stack2 存储的最终顺序的逆序
            if node.lchild != None:
                stack1.append(node.lchild)
            if node.rchild != None:
                stack1.append(node.rchild)
        while stack2:
            node = stack2.pop()
            print(str(node.value) + ' ', end="")

    def level_queue(self, root):
        """
        level traverse binary tree use queue
        :param root: root node of a binary tree
        :return:
        """
        if root == None:
            return
        queue = []
        node = root
        queue.append(node)
        while queue:
            node = queue.pop(0)
            print(str(node.value) + ' ', end="")
            if node.lchild != None:
                queue.append(node.lchild)
            if node.rchild != None:
                queue.append(node.rchild)


if __name__ == '__main__':
    values = range(10)
    tree = BinaryTree()
    for value in values:
        tree.add(value)
    print(f"pre-order traverse use recursive:")
    tree.pre_recursive(tree.root)

    print('\n' + '=' * 50)
    print(f"pre-order traverse use stack: ")
    tree.pre_stack(tree.root)
    print('\n' + '=' * 50)
    print(f"in-order traverse use recursive: ")
    tree.in_recursive(tree.root)
    print('\n' + '=' * 50)
    print(f"in-order traverse use stack:")
    tree.in_stack(tree.root)
    print('\n' + '=' * 50)
    print(f"post-order traverse use recursive: ")
    tree.post_recursive(tree.root)
    print('\n' + '=' * 50)
    print(f"post-order traverse use stack: ")
    tree.post_stack(tree.root)
    print('\n' + '=' * 50)
    print(f"level traverse use queue: ")
    tree.level_queue(tree.root)




