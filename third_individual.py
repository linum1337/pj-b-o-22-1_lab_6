def main():
    sentence = input("Введите предложение: \n")
    letter = input("Введите символ требующийся перед точкой \n")
    print(insert_letter_before_point(sentence, letter))


def insert_letter_before_point(sentence: str, letter: str) -> str:
    sentence_dict = {
        "Предложение до точки": sentence[:-1],
        "Символ между": letter,
    }

    return f"{sentence_dict['Предложение до точки']} {sentence_dict['Символ между']}."


if __name__ == "__main__":
    main()
