import csv
from dogClass import *

class Node(object):

    def __init__(self, data):
        self._left = None
        self._right = None
        self._data = data

class petTree(object):

    def __init__(self):
        self._root = None

    def insertNode(self, data):
        node = Node(data)
        if self._root == None:
            self._root = node
            return
        self._insertNode(node, self._root)

    def _insertNode(self, node, root):
        if not root:
            root = node
        elif not root._left and node._data < root._data:
            root._left = node
        elif not root._right and node._data > root._data:
            root._right = node
        elif root._data > node._data:
            self._insertNode(node, root._left)
        elif root._data < node._data:
            self._insertNode(node, root._right)

    # Print the tree
    def printInOrderPetTree(self):
        self._printInOrderPetTree(self._root)

    def _printInOrderPetTree(self, root):
        if not root:
            return
        self._printInOrderPetTree(root._left)
        print(root._data)
        self._printInOrderPetTree(root._right)

    def readCSVtoPetTree(self, fileNameIn, classIn):
        with open(fileNameIn, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if not row:
                    return
                newObject = classIn(row)
                self.insertNode(newObject)
        csv_file.close()


    def writePetTreeToCSV(self, fileNameIn):
        with open(fileNameIn, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            self._writePetTreeToCSV(self._root, csv_writer)
        csv_file.close()

    def _writePetTreeToCSV(self, root, csv_writer):
            if root == None:
                return
            self._writePetTreeToCSV(root._left, csv_writer)
            csv_writer.writerow(root._data.toFile())
            self._writePetTreeToCSV(root._right, csv_writer)

