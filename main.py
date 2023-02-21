import sys
import csv
import os


def load_files(folder: str) -> list:
    dataArray = list(())
    for file in os.listdir(folder):
        dataArray.append(folder+file)
    return dataArray



def menu() -> None:
    print("Hello, which guessing game would you like to play: ")
    dataArray = load_files("data/")
    count = 1
    for x in dataArray:
        print(str(count) + ". " + x)
        count = count + 1
    choice = int(input("\n      choice:"))
    #TODO: fix bounds checking
    while (choice > count) | (choice < 1):
        choice = int(input("\n      choice:"))

    file = dataArray[choice-1]
    game(file)

def chapterGame() -> None:
    pass

def game(file: str) -> None:
    with open(file) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        count = 0
        score = 0

        idArray = reader.__next__()
        print("Pick what you want to guess:")
        idx = 1
        for id in idArray:
            print(str(idx) + ". " + id)
            idx = idx + 1

        guessColumn = int(input("You want to guess this: "))-1
        while (guessColumn > idx) | (guessColumn < 1):
            guessColumn = int(input("You want to guess this: ")) - 1

        inferColumn = int(input("from this: "))-1
        while (inferColumn > idx) | (inferColumn < 1):
            inferColumn = int(input("from this: ")) - 1

        numQ = input("How many questions would you like me to ask: ")
        for row in reader:
            if count == 0:
                pass
            else:
                guess = input("What is the :" + idArray[guessColumn] + ": of :" + row[inferColumn] + ": ")
                if guess==row[guessColumn]:
                    score = score + 1
                    print("Correct Answer!")
                else:
                    print("Wrong Answer!")
            if count == int(numQ):
                break
            count = count + 1
        print("You got " + str(score) + " right.")

if __name__=="__main__":
    menu()