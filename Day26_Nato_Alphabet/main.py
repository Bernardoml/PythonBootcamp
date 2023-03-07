import pandas

CSV = "nato_phonetic_alphabet.csv"
data = pandas.read_csv(CSV)

# # TODO 1. Create a dictionary in this format:
# # {"A": "Alfa", "B": "Bravo"}
# nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
#
# # TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# user_input = input("Enter a word to be parsed in NATO code: ").upper()
# phonetic_list = [nato_dict[letter] for letter in user_input]
# print(phonetic_list)

# Updated after Day 30 - Error Handling

# {"A": "Alfa", "B": "Bravo"}
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    user_input = input("Enter a word to be parsed in NATO code: ").upper()
    try:
        phonetic_list = [nato_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(phonetic_list)


generate_phonetic()
