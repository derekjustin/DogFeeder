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
            elif data > self.data:
                if self.right is None:
                    self.right = petTree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def readCSVtoPetTree(self, fileNameIn):
        with open(fileNameIn, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                dog = dogClass()
                dog.setName(row[0])
                dog.setAge(row[1])
                dog.setWeight(row[2])
                self.insert(dog)
        line_count += 1
