# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 10:56:04 2024

@author: kdelint
"""

def calculate_guidescore(guide_sequence):
    # Define a dictionary to store the values for each letter at each position
    value_table = {
        'A': [0.322, 0.409, 0.324, 0.072, 0.039, 0.143, 0.178, -0.013, 0.439, 0.458, 0.318, 0.254, -0.242, 0.291, 0.106, 0.151, -0.191, -0.673, -0.523, 0.048],
        'T': [0.172, -0.174, 0.087, -0.367, -0.207, -0.402, -0.365, -0.014, -0.206, -0.468, -0.258, 0.006, -0.209, 0.461, 0.227, -0.144, -1, -1, -1, -1],
        'G': [0.281, -0.103, 0.088, 0.437, 0.11, 0.344, 0.169, 0.003, 0.013, 0.103, 0.052, -0.431, -0.056, -0.585, -0.223, -0.377, 0.012, -0.326, 0.442, 0.584],
        'C': [-0.776, -0.131, -0.5, -0.143, 0.059, -0.079, 0.017, 0.03, -0.245, -0.092, -0.107, 0.174, 0.509, -0.163, -0.108, 0.366, 0.177, 1, 0.075, -0.631]
    }

    # Check if guide_sequence has the correct length
    if len(guide_sequence) != 20:
        raise ValueError("Input sequence must be a twenty-letter string.")

    # Check if the sequence contains invalid letters
    if any(letter.upper() not in {'A', 'T', 'C', 'G'} for letter in guide_sequence):
        raise ValueError("Invalid letters found in the sequence. Only 'A', 'T', 'C', and 'G' are allowed.")

    # Calculate the score by summing up the values for each letter at each position
    score = sum(value_table[guide_sequence[i].upper()][i] for i in range(20))

    return score

# Ask for input of sequence, calculate score and print
guide_sequence = input("Enter 5' to 3' 20nt DNA sequence: ")
result = round(calculate_guidescore(guide_sequence), 3)
print(f"The calculated score for the sequence '{guide_sequence}' is: {result}")