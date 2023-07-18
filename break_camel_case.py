def solution(s):
    return ''.join(map(lambda item: ' ' + item if item.isupper() else item, s))


# # The first solution
# def solution(s):
#     l = []
#     for item in s:
#         if item.isupper()==True:
#             l.append(" "+item)
#         else:
#             l.append(item)
#     return ''.join(l)


# DESCRIPTION:
# Complete the solution so that the function will break up camel casing, using a space between words.

# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""