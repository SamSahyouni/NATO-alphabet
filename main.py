import pandas as p

#TODO 1. Create a dictionary
nato_data = p.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index,row) in nato_data.iterrows()}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name_entry = input("Enter your name\n").upper()
name_as_list = list(name_entry)
nato_list = [nato_dict[letter] for letter in name_as_list]
print(nato_list)
