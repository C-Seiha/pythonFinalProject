def Menu():
    print("Menu:")
    print("1. Play")
    print("2. Exit\n")

def startScreen():
    print("1. Play using the default words")
    print("2. Create your own word list")
    print("3. Return\n")

def endScreen():
    print("1. Replay")
    print("2. Exit\n")

def restartScreen():
    print("1. Playing using the default words")
    print("2. Update the word list")
    print("3. Continue")
    print("4. Return\n")

def createOwnWordList(): 
    amount = int(input("Enter the amount of words you want to add: "))
    for i in range(amount):
        word = input(f"Enter word #{i + 1}: ")
        word_list.append(word)
    return word_list

def addWord():
    pass

def deleteWord():
    pass

def play():
    pass

word_list = [] 

# Configuring the game
Menu()
choice = int(input("Enter your choice: "))

while choice not in [1, 2]:
    print("Invalid Input")
    choice = int(input("Enter your choice: "))

if choice == 1:
    startScreen()
    word_choice = int(input("Enter your choice: "))

    while word_choice not in [1, 2, 3]:
        print("Invalid Input")
        word_choice = int(input("Enter your choice: "))

    if word_choice == 1:
        word_list = ["apple", "banana", "coconut"]
    elif word_choice == 2:
        word_list = createOwnWordList()
    elif word_choice == 3:
        Menu()
else:
    print("Exiting...")
    exit(0)


# Ending screen after the game
endScreen()

end_choice = int(input("Enter your choice: "))

while end_choice not in [1, 2]:
    print("Invalid input")
    end_choice = int(input("Enter your choice: "))

if (end_choice == 1):
    restartScreen()
    choice = int(input("Enter your choice: "))
    while choice not in [1, 2, 3]:
        print("Invalid input")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            word_list = ["apple", "banana", "coconut"]
        elif choice == 2:
            print("1. Add words")
            print("2. Delete words\n")
            choice = int(input("Enter your choice: "))

            if (choice == 1):
                amount = int(input("Enter the amount of words you want to add: "))
                for i in amount:
                    word = input(f"Enter word {i + 1}: ")
                    word_list.append(word)
            else:
                print("Word List")
                for i in range (len(word_list)):
                    print(f"{i + 1}. {word_list[i]}")
                print()
                amount = int(input("Enter the amount of words you want to delete: "))
                delete_idx = []
                for i in range (amount):
                    idx = int(input("Enter the index of the word you want to delete: "))
                    delete_idx.append(idx)

                delete_idx.sort()
                delete_idx.reverse()
                
                for i in delete_idx:
                    word_list.pop(i - 1)
        elif choice == 3:
            play()
        else:
            Menu()

else:
    print("Exiting")
    exit(0)