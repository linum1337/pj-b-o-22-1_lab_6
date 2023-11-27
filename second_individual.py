from sys import stdin


def main():
    print("Введите слова (По окончанию ввода отправьте комбинацию ctrl+D)\n")
    words = []
    for word in stdin:
        words.append(word[:-1])
    print(correct_sequence(words))


def correct_sequence(words: list) -> list:
    corrected_words = []
    for word in words:
        corrected_word = word.replace('чя', 'ча').replace('щя', 'ща')
        corrected_words.append(corrected_word)
    return corrected_words


if __name__ == "__main__":
    main()
