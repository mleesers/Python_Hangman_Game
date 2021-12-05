import random
def mainMenu():
    print("Welcome to the hangman game!\nYou have three choices of subjects to choose from.\n")
    print("you can choose from pokemon, mortal kombat characters or horror characters.\n")
    print("You have 9 chances to guess the letter and only 1 chance to guess the word correctly. Good luck!")
    count = 0
    while(count != 1):
        choice = int(input("\n\n\nWhat choice would you like[1/2/3]?: "))
        if choice == 1:
            pokemon()
            count += 1
        elif(choice == 2):
            count += 1
            mortal()
        elif(choice == 3):
            count += 1
            horror()
        else:
            print("\nPlease choose a valid option")




def pokemon():
    pokemon = ["pikachu","gengar","bulbasaur","chimchar","charmander","squirtle","eevee","magikarp","dratini","gardevoir"]
    word = random.choice(pokemon)
    print("\n\n\nyou chose pokemon " + word)
    blanks(word)

def mortal():
    mortalKombatCharacters = ["mileena","reptile","johnny","scorpion","subzero","raiden","kitana","baraka","shinnok","takeda"]
    word = random.choice(mortalKombatCharacters)
    print("\n\n\nYou chose mortal kombat characters" + word)
def horror():
    horrorCharacters = ["freddie","jason","michael","pinhead","ghostface","chucky","hannibal","leatherface","jigsaw","carrie"]
    word = random.choice(horrorCharacters)
    print("\n\n\nYou chose horror characters " + word)

def blanks(word):
    letters = []
    blank = []
    for x in range(len(word)):
        letters.append(word[x])
    for x in range(len(letters)):
        blank.append('_')
    gameplay(letters,blank)

def gameplay(letters,blank):
    
    letters = letters
    blank = blank
    chances = 9
    print(" ".join(str(x) for x in blank))
    while(chances > 0):
        choice = int(input("Do you want to guess the letter or word?[1/2]: "))
        if choice == 1:
            check = 0
            letterChoice = input("what letter do you want to choose?: ").lower()
            LetterInWord = False
            for x in range(len(letters)):
                if(letters[x] == letterChoice):
                    LetterInWord = True
            if LetterInWord == False:
                chances -= 1
                print("wrong bitch")
                print(chances)
            elif LetterInWord == True:
                print("you right")
        elif choice == 2:
            wordGuess = input("what is your guess: ").lower()
            print(wordGuess)







mainMenu()