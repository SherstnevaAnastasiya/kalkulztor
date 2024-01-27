
n = input().split()



def summa(a, b):
    return a + b


def raznost(a, b):
    return a - b


def umn(a, b):
    return a * b


def delen(a, b):
    return a // b


if len(n) != 3:
    print('throws Exception')
elif not n[0].isnumeric():
    print('throws Exception')
elif not n[2].isnumeric():
    print('throws Exception')
else:
    n[0] = int(n[0])
    n[2] = int(n[2])
    if (0 >= n[0] or n[0] >= 11) or (0 >= n[2] or n[2] >= 11):
        print('throws Exception')
        sum = + 1
    elif n[1] not in '+-*/':
        print('throws Exception')
    else:
        n[0] = int(n[0])
        n[2] = int(n[2])
        if n[1] == '+':
            print(summa(n[0], n[2]))
        if n[1] == '-':
            print(raznost(n[0], n[2]))
        if n[1] == '*':
            print(umn(n[0], n[2]))
        if n[1] == '/':
            print(delen(n[0], n[2]))
