'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurrences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # "th" has the length of 2
    # After each iteration and "th" is not found add 1 to index else add 2

    # Define base case to check if length of word is less than length of "th"

    if len(word) < 2:
        return 0

    # Slice String From index 0 to 2(length of "th") and check if its equal to the "th"

    if (word[0: 2] == "th"):

        # If "th" is found slice string, and pass the rest of the string from index 2 and count 1

        return count_th(word[2:]) + 1

    # If "th" is not found slice the string at index 1 and pass the rest of the string to keep on looking

    return count_th(word[1:])
