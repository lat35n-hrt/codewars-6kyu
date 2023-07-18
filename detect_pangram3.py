# Detect Pangram

# Submitted
def is_pangram(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz' 
    for item in alphabet:
        if item not in s.lower():
            return False
    return True
    
##The second splution
# def is_pangram(s):
#     alphabet = 'abcdefghijklmnopqrstuvwxyz' 
#     for item in alphabet:
#         if item in s:
#             pass
#         else:
#             return False
#     return True


# The first solution
# def is_pangram(s):
#     n = 0
#     alphabet = 'abcdefghijklmnopqrstuvwxyz' 
#     for item in alphabet:
#         if item in s:
#             n += 1
#         else:
#             continue
#     if n == 26:
#         return True
#     else:
#         return False
 


# Description
# A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).
# Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation. 