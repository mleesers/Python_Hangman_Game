import random
def mainMenu():
    print("\nWelcome to the hangman game!\n\nYou have three choices of subjects to choose from.\n")
    print("You can choose from pokemon, mortal kombat characters or horror characters.")
    print("\nYou have 9 chances to guess the letter and only 1 chance to guess the word correctly. Good luck!")
    count = 0
    while(count != 1):
        choice = input("\n\n\nWhat choice would you like[1/2/3]?: ")
        if choice == '1':
            pokemon()
            count += 1
        elif(choice == '2'):
            count += 1
            mortal()
        elif(choice == '3'):
            count += 1
            horror()
        else:
            print("\nPlease choose a valid option")



def pokemon():
    pokemon = ["pikachu","gengar","bulbasaur","chimchar","charmander","squirtle","eevee","magikarp","dratini","gardevoir"]
    word = random.choice(pokemon)
    print("\n\n\nYou chose pokemon!")
    blanks(word)

def mortal():
    mortalKombatCharacters = ["mileena","reptile","johnny","scorpion","subzero","raiden","kitana","baraka","shinnok","takeda"]
    word = random.choice(mortalKombatCharacters)
    print("\n\n\nYou chose mortal kombat characters!")
    blanks(word)
def horror():
    horrorCharacters = ["freddie","jason","michael","pinhead","ghostface","chucky","hannibal","leatherface","jigsaw","carrie"]
    word = random.choice(horrorCharacters)
    print("\n\n\nYou chose horror characters")
    blanks(word)

def blanks(word):
    letters = []
    blank = []
    for x in range(len(word)):
        letters.append(word[x])
    for x in range(len(letters)):
        blank.append('_')
    gameplay(letters,blank,word)

def gameplay(letters,blank,word):
    chances = 9
    used = []
    while(chances > 0):
        print(" ".join(str(x) for x in blank))
        print("\n")
        if blank == letters:
                print("Congrats! You won")
                end()
        choice = (input("Do you want to guess the letter or word?[l/w]: ")).lower()
        if choice == 'l':
            check = 0
            letterChoice = input("what letter do you want to choose?: ").lower()
            LetterInWord = False
            for x in range(len(letters)):
                if(letters[x] == letterChoice):
                    LetterInWord = True
            if letterChoice in used:
                print("\nyou've already chosen this letter\n")    
            elif LetterInWord == False:
                chances -= 1
                used.append(letterChoice)
                if chances > 0:
                     print("\nIncorrect! You have ",chances," chances remaining")
                else:
                    print("\nYou're out of chances! Game Over")
                    end()
            elif LetterInWord == True:
                used.append(letterChoice)
                for x in range(len(blank)):
                    if(letters[x] == letterChoice):
                        blank[x] = letterChoice
                print("\nCorrect!")
        elif choice == 'w':
            wordGuess = input("what is your guess?: ").lower()
            if(wordGuess == word):
                print("\nyay you won!")
                end()
            else:
                print("\nYou lost :(")
                end()  
        else:
            print("\nEnter a valid choice")

def end():
    retry = input("Would you like to to try again?[y/n]: ")
    if(retry == 'y'):
        mainMenu()
    else:
        exit()




mainMenu()