def main():
    sentence = input("Input anything: \n")
    symbol_one = input("Input first symbol to search: \n")
    symbol_two = input("Input secont symbol to search: \n")
    find_appends(sentence, symbol_one, symbol_two)


def find_appends(sentence: str, symbol_one: str, symbol_two: str):
    cut_sentence = sentence.split()
    highlighted_sentence = []
    for word in cut_sentence:
        if symbol_one in word:
            highlighted_sentence.append(word.upper())
        elif symbol_two in word:
            highlighted_sentence.append(word.upper())
        else:
            highlighted_sentence.append(word)

    print(" ".join(highlighted_sentence))


if __name__ == '__main__':
    main()
