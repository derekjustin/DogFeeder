import csv
from dogClass import *

class petTree:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = petTree(data)
                else:
                    self.left.insert(data)
            elif data >= self.data:
                if self.right is None:
                    self.right = petTree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # Print the tree
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    def readCSVtoPetTree(self, fileNameIn):
        with open('petInventory.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                dog = dogClass()
                dog.setName(row[0])
                dog.setAge(row[1])
                dog.setWeight(row[2])
                self.insert(dog)
        line_count += 1

    def initWritePetTreeToCSV(self, fileNameIn):
        with open(fileNameIn, mode='w') as csv_file :
            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            self.writePetTreeNodeToCSV(self.data, csv_writer)

    def writePetTreeNodeToCSV(self, data, csv_writer):
        csv_writer.writerow(data)

    def petTreeTraversal(self):
        if self.left:
            self.left.petTreeTraversal()
        return self.data
        if self.right:
            self.right.petTreeTraversal()
