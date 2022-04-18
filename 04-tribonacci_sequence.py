num = int(input())


def tribonacci(n):
    tribonacci_list = []
    for i in range(n):
        if i == 0 or i == 1:
            number = 1
        elif i == 2:
            number = 2
        else:
            number = tribonacci_list[i-1] + tribonacci_list[i-2] + tribonacci_list[i-3]
        tribonacci_list.append(number)
    sequence = ' '.join(list(map(str, tribonacci_list)))
    print(sequence)

tribonacci(num)
