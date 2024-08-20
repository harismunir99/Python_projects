import random

print("Welcome to Hangman")
print("---------------------------------")

word_dictionary = ["sunflower", "house", "diamond", "memes", "yeet", "hello", "howdy", "like", "subscribe"]

# Choose a random word
random_word = random.choice(word_dictionary)

def print_hangman(wrong):
    if wrong == 0:
        print("\n+---+")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
        
    elif wrong == 1:
        print("\n+---+")
        print("O   |")
        print("    |")
        print("    |")
        print("   ===")
        
    elif wrong == 2:
        print("\n+---+")
        print("O   |")
        print("|   |")
        print("    |")
        print("   ===")
        
    elif wrong == 3:
        print("\n+---+")
        print(" O  |")
        print("/|  |")
        print("    |")
        print("   ===")
        
    elif wrong == 4:
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("    |")
        print("   ===")
        
    elif wrong == 5:
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("/   |")
        print("   ===")
        
    elif wrong == 6:
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("/ \ |")
        print("   ===")
        
def print_word(guessedletters):
    counter = 0
    rightletter = 0
    for char in random_word:
        if char in guessedletters:
            print(char, end=" ")
            rightletter += 1
        else:
            print("_", end=" ")
        counter += 1
    return rightletter

def print_lines():
    print("\r")
    for char in random_word:
        print("\u203E", end=" ")

length_of_word_to_guess = len(random_word)
amount_of_times_wrong = 0
current_letters_guessed = []
current_letters_right = 0

while amount_of_times_wrong != 6 and current_letters_right != length_of_word_to_guess:
    print("\nLetters guessed so far: ")
    for letter in current_letters_guessed:
        print(letter, end=" ")
            
    # Prompt user for input 
    letter_guessed = input("\nGuess a letter: ").lower()
    
    # Check if the letter is already guessed
    if letter_guessed in current_letters_guessed:
        print("You already guessed that letter.")
        continue
        
    # Check if user's guess is correct
    if letter_guessed in random_word:
        current_letters_guessed.append(letter_guessed)
        current_letters_right = print_word(current_letters_guessed)
        print_lines()
    else:
        amount_of_times_wrong += 1
        current_letters_guessed.append(letter_guessed)
        print_hangman(amount_of_times_wrong)
        current_letters_right = print_word(current_letters_guessed)
        print_lines()
    
print("Game is over! Thank you for playing")
