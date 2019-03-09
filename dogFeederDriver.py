def main():

    objective = ""
    continu = True

    # Greeting
    print("Hello welcome to DogFeeder")

    # while loop to continue program
    getObjectiveInput(objective)


def getObjectiveInput(objectiveIn):

    continu = True

    while continu:
        objectiveIn = input("What would you like to do? ")

        if objectiveIn == "add":
            print("Dog was added to list")
            continu = False

        else:
            print("Invalid Input, Please try again.")


main()