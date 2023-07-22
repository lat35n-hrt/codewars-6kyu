
# The second solution
def tribonacci(s, n):
    if n <= 2:
        return s[:n]
    for i in range(n-3):
        s.append(s[i] + s[i+1] + s[i+2])
    return s




# THe first solution
# def tribonacci(signature, n):
#     s = signature
#     next = 0
#     if n==0:
#         return []
#     elif n== 1:
#         return [s[0]]
#     elif n== 2:
#         return [s[0], s[1]]
#     for i in range(n-3):
#         next = s[i] + s[i+1] + s[i+2]
#         s.append(next)
#     return s




        # test.assert_equals(tribonacci([1, 1, 1], 10), [1, 1, 1, 3, 5, 9, 17, 31, 57, 105])