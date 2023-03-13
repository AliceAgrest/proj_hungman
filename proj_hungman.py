def openning ():
    """
    The func print the opening of the game
    """
    HANGMAN_ASCII_ART = "| |  | |                                      \n| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  \n|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ \n| |  | | (_| | | | | (_| | | | | | | (_| | | | |\n|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|\n                     __/ |                      \n                    |___/\n"
    MAX_TRIES = 6
    print(HANGMAN_ASCII_ART, MAX_TRIES)

HANGMAN_PHOTOS = {'1': '    x-------x',
                  '2': '    x-------x\n    |\n    |\n    |\n    |\n    |',
                  '3': '    x-------x\n    |       |\n    |       0\n    |\n    |\n    |',
                  '4': '    x-------x\n    |       |\n    |       0\n    |       |\n    |\n    |',
                  '5': '    x-------x\n    |       |\n    |       0\n    |      /|\\\n    |\n    |',
                  '6': '    x-------x\n    |       |\n    |       0\n    |      /|\\\n    |      /\n    |',
                  '7': '    x-------x\n    |       |\n    |       0\n    |      /|\\\n    |      / \\\n    |'}

def print_hangman(num_of_tries):
    """
    The func print the hungman photos by num of left tries
    :param num_of_tries: number of left tries
    :type num_of_tries: int
    :return: hungman photo
    """
    if num_of_tries == 0:
        print(HANGMAN_PHOTOS['1'])
    elif num_of_tries == 1:
        print(HANGMAN_PHOTOS['2'])
    elif num_of_tries == 2:
        print(HANGMAN_PHOTOS['3'])
    elif num_of_tries == 3:
        print(HANGMAN_PHOTOS['4'])
    elif num_of_tries == 4:
        print(HANGMAN_PHOTOS['5'])
    elif num_of_tries == 5:
        print(HANGMAN_PHOTOS['6'])
    elif num_of_tries == 6:
        print(HANGMAN_PHOTOS['7'])

def choose_word(file_path, index):
    """
    The func choose word to guess by file from the input and index of the word
    :param file_path: file path from the player
    :param index: index of the word
    :type file_path: string
    :type index: int
    :return: the word from the file
    :rtype: tuple
    """
    input_file = open(file_path, 'r')
    f = input_file.read()
    input_index = index - 1
    repeated_words = []
    the_word = ''
    list_of_words = f.split(' ')
    if len(list_of_words) > input_index:
        the_word += list_of_words[input_index]
    else:
        every_index = 0
        to_continue = True
        while to_continue:
            for i in range(len(list_of_words)):
                if input_index == every_index:
                    the_word += list_of_words[i]
                    print(list_of_words[i])
                    to_continue = False
                    break
                every_index += 1

    for i in list_of_words:
        if list_of_words.count(i) > 1 and i not in repeated_words:
            repeated_words.append(i)
    for i in repeated_words:
        list_of_words.remove(i)

    tuple_of_word = (len(list_of_words),the_word)
    return tuple_of_word

def show_hidden_word (secret_word, old_letters_guessed):
    """
    The func prints the word
    :param secred_word: the word that need to guess
    :param old_letters_guessed: guessed words
    :type secred_word: string
    :type old_letters_guessed: list
    :return: string with guessed words
    :rtype: string
    """
    s = ""
    if len(old_letters_guessed) == 0:
        for i in range(len(secret_word)):
            if i < (len(secret_word) - 1):
                s += '_ '
            else:
                s += '_'
    else:
        for i in range(len(secret_word)):
            found = 0
            for x in old_letters_guessed:
                if secret_word.find(x) != -1 and secret_word[i] == x:
                    s += x
                    found += 1
                    break
            if found < 1:
                s += '_ '
            elif found >= 1 and i < (len(secret_word) - 1):
                s += ' '
    
    return s

def show_history_of_letters(old_letters_guessed):
    """
    The func prints all guessed letters
    :param old_letters_guessed: all guessed letters
    :type old_letters_guessed: list
    """
    if len(old_letters_guessed) > 0:
        new_sorted = sorted(old_letters_guessed)
        max_letter = max(old_letters_guessed)
        for i in range (len(old_letters_guessed) - 1):
            print(new_sorted[i] + " -> ", end="")
        print(max_letter)

def check_valid_input (letter_guessed, old_letters_guessed):
    """
    The function chacks if the input is right also checks if the letter was in old letters that player guessed
    :param letter_guessed: input from the player
    :param old_letter_guessed: input from  the player
    :type letter_guessed: string
    :type old_letter_guessed: list
    :return: if the input right or not
    :rtype: boolean
    """
    letter_guessed = letter_guessed.lower()
    if len(letter_guessed) != 1 and letter_guessed.isalpha() == False:
        return False
    elif len(letter_guessed) != 1 and letter_guessed.isalpha() == True:
        return False
    elif len(letter_guessed) == 1 and letter_guessed.isalpha() == False:
        return False
    elif len(letter_guessed) == 1 and letter_guessed in old_letters_guessed:
        return False
    else:
        return True

def try_update_letter_guessed (letter_guessed, old_letters_guessed):
    """
    The func checks if the input is proper then adds to the list or not and prints appropriate message
    :param letter_guessed: input from the player
    :param old_letter_guessed: input from  the player
    :type letter_guessed: string
    :type old_letter_guessed: list
    :return: if list updeted or no
    :rtype: boolean
    """
    if check_valid_input(letter_guessed, old_letters_guessed) == False:
        print("X")
        show_history_of_letters(old_letters_guessed)
        return False
    else:
        old_letters_guessed.append(letter_guessed)
        return True
    
def check_win (secret_word, old_letters_guessed):
    """
    The func check if the player guessed all the words
    :param secred_word: the word that need to guess
    :param old_letters_guessed: guessed words
    :type secred_word: string
    :type old_letters_guessed: list 
    :return: does player won or not
    :rtype: bool
    """
    found = 0
    for i in range(len(secret_word)):
        for x in old_letters_guessed:
            if secret_word[i] == x:
                found += 1
    if found < len(secret_word):
        return False
        
    return True

def main():
    openning()
    file_path = input('Enter a file path: ')
    index_input = int(input('Enter index: '))
    word_info = choose_word(file_path, index_input)
    the_word = word_info[1]
    num_of_tries = 0
    old_letters_guessed = []

    print("Let's start!")
    print_hangman(num_of_tries)
    print(show_hidden_word(the_word, old_letters_guessed))
    while num_of_tries < 7:
        letter_guessed = input("Guess a letter: ")
        try_update_letter_guessed(letter_guessed, old_letters_guessed)
        
        how_many_guessed = show_hidden_word(the_word, old_letters_guessed)
        if how_many_guessed.find(letter_guessed) == -1:
            num_of_tries += 1
            print(':(')
        print_hangman(num_of_tries)
        print(how_many_guessed)
        
        if check_win(the_word, old_letters_guessed) == True:
            print(show_hidden_word(the_word, old_letters_guessed))
            print('WON')
            break

        if num_of_tries > 6:
            print('LOSE')
            break

if __name__ == '__main__':
    main()