# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt") as name_data:
    data = name_data.read()
    names = data.splitlines()

with open("Input/Letters/starting_letter.txt") as letter_data:
    letter = letter_data.read()

for name in names:
    merged_letter = letter.replace(PLACEHOLDER, name)
    with open(f"Output/ReadyToSend/Letter_for_{name}.txt", mode="w") as output_letter:
        output_letter.write(merged_letter)
