# Passwoed Generator in Python Using Combinations of Letters, Digits And Panctuations


import random
import string

def Get_Random_Alphanumeric_String(letters_count, digits_count, panctuation_count):
    sample_string = ''.join((random.choice(string.ascii_letters) for i in range(letters_count)))
    sample_string += ''.join((random.choice(string.digits) for i in range(digits_count)))
    sample_string += ''.join(random.choice(string.punctuation) for i in range(panctuation_count))

    # Convert string to list and shuffle it to mix letters, digits and panctuation
    sample_list = list(sample_string)
    random.shuffle(sample_list)
    final_string = ''.join(sample_list)
    return final_string

# 9 letters, 3 digits and 2 panctuation
print("First Random Alphanumeric String is:", Get_Random_Alphanumeric_String(9, 3, 2))

# 7 letters, 5 digits and 4 panctuation
print("Second Random Alphanumeric String is:",  Get_Random_Alphanumeric_String(7, 4, 4))

# 8 letters and 7 digits and 1 panctuation
print("Third Random Alphanumeric String is:",  Get_Random_Alphanumeric_String(8, 7, 1))
