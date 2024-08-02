import random

def generate_number():
    return str(random.randint(1000, 9999))

def calculate_cows_and_bulls(secret, guess):
    cows = sum(1 for s, g in zip(secret, guess) if s == g)
    bulls = sum(1 for g in guess if g in secret) - cows
    return cows, bulls

def main():
    secret_number = generate_number()
    guess_count = 0

    print("Welcome to the Cows and Bulls Game!")
    
    while True:
        guess = input("Enter a 4-digit number: ")
        
        if len(guess) != 4 or not guess.isdigit():
            print("Please enter a valid 4-digit number.")
            continue
        
        guess_count += 1
        cows, bulls = calculate_cows_and_bulls(secret_number, guess)
        
        if cows == 4:
            print(f"Congratulations! You've guessed the number {secret_number} in {guess_count} guesses.")
            break
        else:
            print(f"{cows} cow(s), {bulls} bull(s)")

if __name__ == "__main__":
    main()
