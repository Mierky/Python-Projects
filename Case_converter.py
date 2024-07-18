def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]

    return ''.join(snake_cased_char_list).strip('_')


if __name__ == "__main__":
    word = input("Enter a word: ")
    print(convert_to_snake_case(word))
    #Test: aLongAndComplexString