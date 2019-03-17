
from dogClass import dogClass
from petTree import petTree

def main():

    objective = ""
    sentinel = 1
    pets = petTree()
    pets.readCSVtoPetTree("dogs/petInventory.csv", dogClass)
    # Greeting
    print("Hello welcome to DogFeeder")

    # while loop to continue program
    while sentinel:
        objective = getObjectiveInput()
        if objective.upper() == "QUIT" or objective.upper() == "Q":
            print("Goodbye")
            sentinel = 0
            break
        elif objective.upper() == "ADD" or objective.upper() == "A":
            print("Okay lets add your dog to your household.")
            dog = dogClass()
            dog.getSetDogInfo()
            dog.createDogDirectorySystem()
            pets.insertNode(dog)
            print(dog.getName(), "has been successfully added to your household.")
            sentinel = int(input("Enter 1 to continue or 0 to quit: "))

    pets.printInOrderPetTree()
    pets.writePetTreeToCSV("dogs/petInventory.csv")

def getObjectiveInput():

    sentinel = True

    while sentinel:
        objective = input("What would you like to do?\nEnter 'Quit' to quit.\nEnter 'Add' to add dog to household.\nInput: ")
        if objective.upper == "QUIT" or objective.upper() == "Q":
            return "Q"
        elif objective.upper() == "ADD" or objective.upper() == "A":
            return "A"
        else:
            print("Invalid Input, Please try again.")




main()