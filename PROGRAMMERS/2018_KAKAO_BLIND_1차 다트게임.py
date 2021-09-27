def solution(dartResult):
    answer = []
    str_dict = {'S': 1, 'D': 2, 'T': 3, '*': 2, '#': -1}
    for digit in dartResult:
        if digit in ['S', 'D', 'T']: answer[-1] = int(answer[-1]) ** str_dict[digit]
        elif digit in ['*', '#']:
            answer[-1] = int(answer[-1]) * str_dict[digit]
            if len(answer) >= 2 and digit == '*': answer[-2] = answer[-2] * str_dict[digit]
        else:
            if not answer or type(answer[-1]) == int: answer.append(digit)
            else: answer[-1] += digit
    return sum(answer)