import random
from hangman_words import word_list
from hangma_art import logo, stages

def play_hangman():
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)

    end_of_game = False
    lives = 6

    print(logo)
    print(f"psss {chosen_word}")

    display = []
    for _ in range(word_length):
        display += "_"

    while not end_of_game:
        guess = input("Выбирай букву! ").lower()
        if guess in display:
            print(f"Ты выбирал уже эту {guess}, пробуй другую ")

        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:
            print(f"Ты выбрал {guess}, такой буквы нет в слове, ты потерял 1 жизнь! 😜️️️️️️")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("Ты проиграл 😭️️️️️️")

        if "_" not in display:
            end_of_game = True
            print("Ты выиграл 😎️️️️️️")

        print(" ".join(display))
        print(stages[lives])
    
    new_game = input("Хотел бы сыграть ешё раз? (да/нет) 🎯️️️️️️ ").lower()
    if new_game == "да":
        play_hangman()
    else:
        print("Спасибо за игру 😉️️️️️️")
    
if __name__ == "__main__":
    play_hangman()
