student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
nato_dataframe = pandas.read_csv(r"Day 26 list comprehension and nato alphabet\Nato Alphabet project\nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index,row) in nato_dataframe.iterrows()}
#print(nato)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("enter word: ")
nato_form = [nato_dict[letter] for letter in user_input.upper()]

print(f"{user_input} is {nato_form}")