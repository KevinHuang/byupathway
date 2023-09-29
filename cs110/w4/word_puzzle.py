

def start_game():
    print('Welcome to the word guessing game!')
    print('')
    answer = "moroni"
    user_guess = "      "
    hint = calculate_hint(user_guess, answer)
    is_correct = False

    guess_count = 0;

    while not is_correct:
        print(f"Your hint is: { hint }")
        user_guess = input("What is your guess?")
        guess_count = guess_count + 1

        if (answer.lower() == user_guess.lower()):
            showFinishMessage(guess_count)
            is_correct = True
        else:
            hint = calculate_hint(user_guess, answer)


def calculate_hint(user_guess, answer):

    result = [];
    index = 0;
    for l in user_guess:
        targetWord = answer[index]
        # print(f"targetWord: {targetWord}")
        if (l.lower() == targetWord.lower()):
            result.append(l.upper());
        elif  l in answer :
            result.append(l.lower());
        else:
            result.append("_")
        index = index + 1
        # print(result);

    return ''.join(result);



def showFinishMessage(guess_count):
    print("Congratulations! You guessed it!");
    print(f"It took you {guess_count} guesses.")


start_game();