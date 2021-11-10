# Reduce a binary number, as a string, to zero and return the number of operation needed to do so

from math import log


def solution(S):
    num = int(S, 2)
    counter = int(log(num) // log(2)) + bin(num).count("1")
    print(counter)
    return counter

## Not efficient enough
# def reduce(num):
#     if num % 2 == 0:
#         return num // 2
#     else:
#         return num - 1


# def solution(S):
#     num = int(S, 2)
#     counter = 0

#     while num:
#         counter += 1
#         num = reduce(num)
#     print(counter)
#     return counter


solution("011100")
solution("111")
solution("1111010101111")
