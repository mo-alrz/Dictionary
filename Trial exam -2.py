# Write a function that can read and parse a file. It should take the name of the file as an input and return the
# most common word of the file (case insensitively). If multiple words are found as the most common you can decide
# which one to return. You can assume that:
# the file contains multiple lines
# the words are separated by spaces only
# there can be , and . characters in the sentences
# The function should handle possible exceptions by printing messages to the standard output.

my_sentence = " Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris cursus velit ac luctus accumsan." \
              "Nullam pretium,tortor facilisis elementum lacinia, nibh erat pulvinar odio, at ultrices sapien tortor " \
              "suscipit nisi. Mauris donec sed tincidunt libero. Morbi aliquet quam sed auctor porttitor. " \
              "Nam semper magna gravida scelerisque hendrerit. Donec vel sem ante. Vivamus dapibus nibh et augue " \
              "venenatis, quis ultrices mauris tincidunt. Aliquam felis massa, porta vitae diam non, suscipit " \
              "eleifend est. Cras hendrerit posuere mauris, laoreet. Nam ullamcorper purus sed cursus mattis."


def count_appearance(sentence):
    assert type(sentence) == str
    lower_cased = sentence.lower()
    split_words = lower_cased.split()
    word_counter = {}
    for character in list(split_words):
        if character not in word_counter:
            word_counter[character] = 0
        word_counter[character] += 1
    max_appearance = max(word_counter, key=word_counter.get)
    return max_appearance


print("The most repeated word is : ", count_appearance(my_sentence))
