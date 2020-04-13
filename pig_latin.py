def pig_latin(word):
    vowels = ['a', 'e', 'y', 'u', 'i', 'o']

    if word[0].lower() in vowels:
        new_word = word + "way"
    else:
        new_word = word
        for index, letter in enumerate(word, start=0):
            if letter not in vowels:
                new_word += letter
            else:
                new_word = new_word[index:] + "ay"
                break

    return new_word


if __name__ == "__main__":
    while True:
        word = input('Input word (only alphanumeric, single word) >> ')
        if not word.isalpha():
            print('Try again!')
            continue
        else:
            print(pig_latin(word))
            quit()
