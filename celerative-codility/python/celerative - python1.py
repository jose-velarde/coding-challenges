# return the highest number resulting of inserting a '5' in any position of a number

def solution(N):
    # write your code in Python 3.6
    N_string = ""
    insert_minus = False
    combinations = []

    if N < 0:
        N_string = str(N)[1:]
        insert_minus = True
    else:
        N_string = str(N)

    for index in range(len(N_string) + 1):
        combinations.append(N_string[:index] + "5" + N_string[index:])

    if insert_minus:
        max = "-" + combinations[0]
    else:
        max = combinations[0]

    for combination in combinations:
        if insert_minus:
            combination = "-" + combination
        if int(combination) > int(max):
            max = int(combination)
    return max


solution(268)
solution(670)
solution(0)
solution(-999)
