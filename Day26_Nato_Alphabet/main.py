import pandas

CSV = "nato_phonetic_alphabet.csv"
data = pandas.read_csv(CSV)

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word to be parsed in NATO code: ").upper()
phonetic_list = [nato_dict[letter] for letter in user_input]
print(phonetic_list)
