
from dogClass import dogClass
from petTree import petTree

def main():

    objective = 0
    sentinel = 1
    pets = petTree()
    pets.readCSVtoPetTree("petInventory.csv")
    # Greeting
    print("Hello welcome to DogFeeder")

    # while loop to continue program
    while sentinel:
        objective = getObjectiveInput()
        if objective == 1:
            dog = dogClass()
            dog.setName(input("What is your dogs name: "))
            dog.setAge(input("How old is your dog: "))
            dog.setWeight(input("How much does your dog weigh in pounds: "))
            pets.insertNode(dog)
            print(dog.getName(), "has been successfully added to your household.")
            pets.printInOrderPetTree()
            sentinel = int(input("Enter 1 to continue or 0 to quit: "))

    pets.printInOrderPetTree()
    pets.writePetTreeToCSV("petInventory.csv")

def getObjectiveInput():

    sentinel = True

    while sentinel:
        objective = input("What would you like to do? ")

        if objective == "1":
            print("Okay lets add your dog to your household.")
            return 1
        else:
            print("Invalid Input, Please try again.")


main()