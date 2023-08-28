import random

# Word lists for different levels
#include more words later
word_lists = {
    "easy": ["apple", "banana", "cherry", "grape", "orange"],
    "medium": ["elephant", "giraffe", "kangaroo", "zebra", "rhinoceros"],
    "hard": ["chocolate", "pineapple", "watermelon", "strawberry", "blueberry"]
}

def choose_word(level):
    return random.choice(word_lists[level])

def play_again():
    return input("Do you want to play again? (yes/no): ").lower() == "yes"

#include hint function
def give_hint(word, revealed_letters):
    unrevealed_letters = [letter if letter not in revealed_letters else '_' for letter in word]
    hint_letter = random.choice([letter for letter in unrevealed_letters if letter != '_'])
    revealed_letters.add(hint_letter)
    return revealed_letters

def select_level():
    while True:
        print("Select a level:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        
        choice = input("Enter the number of the selected level: ")
        
        if choice == "1":
            return "easy"
        elif choice == "2":
            return "medium"
        elif choice == "3":
            return "hard"
        else:
            print("Invalid choice. Please select a valid level.")

#ask for name
def main():
    player_name = input("Enter your name: ")
    print(f"Welcome, {player_name}!")
    
    while True:
        level = select_level()
        print(f"You selected {level} level.")
        
        print("\nLet's play the Word Guessing Game!")
        word_to_guess = choose_word(level)
        attempts = 3  # Number of attempts 
        revealed_letters = set()
        
        while attempts > 0:
            print(" ".join([letter if letter in revealed_letters else '_' for letter in word_to_guess]))
            
            guess = input("Guess the word or type 'hint' for a hint: ").lower()
            
            if guess == "hint":
                revealed_letters = give_hint(word_to_guess, revealed_letters)
                continue
            
            try:
                if guess == word_to_guess:
                    print("Congratulations! You guessed the word correctly.")
                    break
                else:
                    attempts -= 1
                    print(f"Wrong guess! You have {attempts} attempts left.")
            except:
                print("Invalid input. Please try again.")
        
        if attempts == 0:
            print(f"Oops! You're out of attempts. The word was '{word_to_guess}'.")
        
        if not play_again():
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()