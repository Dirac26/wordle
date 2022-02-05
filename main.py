import random

def get_words_list(f):
    """
    from file path f with words separated by new line
    parse the file and return list of words
    """
    words_list = []
    with open(f) as fl:
        for line in fl:
            words_list.append(line.strip())
    return words_list

def get_random_from_list(l):
    """
    return random element from list l
    """
    return random.choice(l)

def filter_words(words, answer, answer_mask):
    """
    filter the words list based on the answer and
    the mask of the answer, the mask must return 0 for no occurance. 1 for occurance
    and 2 for correct place letters
    """
    correct_letters = []
    wrong_letters = []
    new_words = []
    for i, l in enumerate(answer):
        if answer_mask[i] == "1":
            correct_letters.append(l)
        if answer_mask[i] == "0":
            wrong_letters.append(l)
    for word in words:
        check = True
        for c in correct_letters:
            if c not in word:
                check = False
        for p, c in enumerate(answer):
            if (word[p] != c) and answer_mask[p] == "2":
                check = False
        for c in wrong_letters:
            if c in word:
                check = False
        if check:
            new_words.append(word)
    return new_words

def main():
    """
    main method
    """
    answer_mask = None
    words = get_words_list("words.txt")
    while True:
        answer = get_random_from_list(words)
        print(f"Please try this word: {answer}")
        answer_mask = input("Enter the mask: ")
        words = filter_words(words, answer, answer_mask)
        if len(words) == 1:
            print(f"The answer is: {words[0]}")
            break

if __name__ == "__main__":
    main()
