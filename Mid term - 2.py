# Write a function that receives a string as an input and returns the most frequent letter from the given string.
# Your solution should be case-insensitive, so a capital letter (like A) and its non-capital version (a)
# should be counted as the same letter. In the given string there can be spaces as well, but your solution
# should not count spaces. If there are multiple letters with the same occurrence, you can decide which one to return.


def most_common_letter(string_or_sent):
    assert type(string_or_sent) == str
    my_str = string_or_sent.replace(" ", "")
    lower_cased = my_str.lower()
    letter_counter = {}
    for character in list(lower_cased):
        if character not in letter_counter:
            letter_counter[character] = 0
        letter_counter[character] += 1
    max_appearance = max(letter_counter, key=letter_counter.get)
    return max_appearance


print(most_common_letter('apple'))  # should print p
print(most_common_letter('This is not so hard'))  # should print s
