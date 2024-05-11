import random

five_letter_words = [
    "house", "water", "music", "earth", "plant", "smile", "dream", "happy", "beach", "chair",
    "cloud", "phone", "sleep", "bread", "fruit", "dance", "tiger", "mouse", "paper", "money",
    "angel", "puppy", "lemon", "queen", "horse", "tiger", "apple", "candy", "grape", "heart",
    "fairy", "river", "quiet", "light", "smile", "woman", "adult", "study", "dream", "space",
    "peace", "magic", "watch", "clock", "chair", "cloud", "beach", "plant", "drink", "bread",
    "pizza", "cake", "sugar", "spice", "angel", "demon", "tiger", "mouse", "snake", "sheep",
    "tiger", "horse", "house", "mouse", "money", "music", "ocean", "river", "queen", "smile",
    "happy", "puppy", "beach", "angel", "earth", "fruit", "chair", "cloud", "clock", "bread",
    "candy", "dance", "dream", "drink", "fairy", "lemon", "light", "magic", "paper", "plant",
    "quiet", "river", "sleep", "snake", "space", "study", "sugar", "watch", "woman", "tiger"
]

missed_letters = []
wrong_letters = []

def the_wordle(random_list, user_list):
    the_empty_list = ["x" for x in random_list]
    for letter in list_of_user_guess:
        index = user_list.index(letter)
        if letter in random_list:
            if user_list[index] not in missed_letters:
                missed_letters.append(user_list[index])

            if user_list[index] == random_list[index]:
                the_empty_list[index] = user_list[index]

            else:
                the_empty_list[index] = "0"

        else:
            if user_list[index] not in wrong_letters:
                wrong_letters.append(user_list[index])

    return the_empty_list


the_chosen_word = random.choice(five_letter_words)

list_of_random_word = list(the_chosen_word)

life = 5

while life != 0:
    while True:
        users_guess = input("predict the word:").lower()
        if len(users_guess) > 5:
            print("the word should only contain 5 letters MF")
        else:
            break
    list_of_user_guess = list(users_guess)
    print(the_wordle(list_of_random_word,list_of_user_guess))
    print("wrong_letters:",wrong_letters)
    print("missed_letters:", missed_letters)
    if list_of_user_guess == list_of_random_word:
        print("you won")
        break
    else:
        life -= 1

print("you lose sucker. The word is:",the_chosen_word)







