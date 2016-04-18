def generate_word(cv):
    """
    :param cv: Generates a random lowercase string of letters in which consonants occupy the given 'c' indices and
    vowels occupy the given 'v' indices. Case sensitive.
    """

    new_word = ""

    # generating the new word sequence
    for letter in cv:
        if letter == "C":
            new_word += random.choice(consonants).upper()

        elif letter == "c":
            new_word += random.choice(consonants)

        elif letter == "V":
            new_word += random.choice(vowels).upper()

        elif letter == "v":
            new_word += random.choice(vowels)

        # error handling if the input is invalid
        else:
            raise ValueError('Please input a string composed of \'C\', \'c\', \'V\', and \'v\' ONLY.')

    return new_word

user_input = input("""Input a string to generate a new word. You may use 'C' or 'c' for consonants and 'V' or 'v'
                    for vowels. Keep in mind that the program is case sensitive. No letters other than the ones
                    specified are accepted. """)

print(generate_word(user_input))
