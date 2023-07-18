def alphabet_position(text):
    return ' '.join(str(ord(a) - 96) for a in text.lower() if a.isalpha())


## The second solution
# def alphabet_position(text):
#     l = []
#     for a in text.lower():
#         if a.isalpha():
#             l.append(str(ord(a) - 96))
#     return ' '.join(l)


# The first solution
# def alphabet_position(text):
#     alphabet = 'abcdefghijklmnopqrstuvwxyz' 
#     n = 0
#     l = []
#     for a in text.lower():
#         if a.isalpha():
#             for b in alphabet:
#                 n += 1
#                 if a == b:
#                     l.append(str(n))
#                     n = 0
#                     break
#     return ' '.join(l)


# DESCRIPTION:
# Welcome.
# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.
# "a" = 1, "b" = 2, etc.
# https://www.codewars.com/kata/546f922b54af40e1e90001da