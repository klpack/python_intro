# Function Definition
def common_chars(phrase, k_value):

    # Input Manipulation
    k_value = int(k_value)
    phrase = phrase.lower()
    phrase_list = list(phrase)

    # Output Dictionary Creation
    phrase_breakdown = dict()

    # Letter Handling in Dictionary
    for letters in phrase_list:
            #Letter Not in Dictionary
        if letters in phrase_breakdown:
            phrase_breakdown[letters] += 1

            #Letter already in dictionary
        else:
            phrase_breakdown[letters] = 1

    # Dictionary Key Culling if Value Not > K

    # Since iterating over dictionary will give an error
    # a copy of original dictionary is made
    copy_phrase_breakdown = dict(phrase_breakdown)

    # For Loops If Statement is done on dictionary copy
    # then deletes keys from the original dictionary.
    for (key,value) in copy_phrase_breakdown.items():
        if value < k_value:
            del phrase_breakdown[key] 

    return(phrase_breakdown)

print(common_chars('The quick brown fox jumps over the lazy dog', 2))