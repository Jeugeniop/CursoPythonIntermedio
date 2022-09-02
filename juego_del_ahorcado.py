import os
import random

CURRENT_WORD = ""
CURRENT_WORD_LETTERS = []
FOUND_LETTERS = []

#Function that selects a random word from the data.txt file
def select_word():
    with open("./archivos/data.txt","r",encoding="utf-8") as f:
        global CURRENT_WORD
        global CURRENT_WORD_LETTERS
        f_list = [word.replace("\n","") for word in f]
        f_dict = {count:value for count, value in enumerate(f_list)}
        num = random.randint(0,len(f_dict)-1)
        CURRENT_WORD = f_dict.get(num)
        CURRENT_WORD_LETTERS = [letter for letter in CURRENT_WORD]
#Function that hides those letter that have not been discovered by the player
def hide_word():
    global CURRENT_WORD_LETTERS
    global FOUND_LETTERS

    hidden_word = ""    
    for letter in CURRENT_WORD_LETTERS:
        if letter in FOUND_LETTERS:
            hidden_word += letter
        else:
            hidden_word += "_"
        hidden_word += " "
    return hidden_word


def refresh_screen():
    os.system("cls")
    print("¡Adivina la palabra!")
    #print(CURRENT_WORD)
    hidden_word = hide_word()
    print(hidden_word)
    return hidden_word


def validate_letter(letter):
    global CURRENT_WORD_LETTERS
    global FOUND_LETTERS
    
    if letter in CURRENT_WORD_LETTERS:
        FOUND_LETTERS.append(letter)

def game_over(status,first_invocation):
    print("")
    if status == "WIN" and first_invocation:
        print("¡Felicidades, has ganado! la palabra es: " + CURRENT_WORD)
    print("")
    new_game = input("¿Deseas jugar otra ronda? Si/No: ")
    if new_game == "Si":
        return True
    elif new_game == "No":
        return False
    else:
        return game_over(status,False)

def clean_globals():
    global CURRENT_WORD
    global CURRENT_WORD_LETTERS
    global FOUND_LETTERS

    CURRENT_WORD = ""
    CURRENT_WORD_LETTERS = []
    FOUND_LETTERS = []

def run():
    global CURRENT_WORD
    while True:
        if CURRENT_WORD == "":
            select_word()
        hidden_word = refresh_screen()
        if hidden_word.find("_") == -1:
            if game_over("WIN",True):
                clean_globals()
            else:
                break
        else:
            print("")
            letter = input("Ingresa una letra: ")
            validate_letter(letter)

if __name__ == "__main__":
    run()