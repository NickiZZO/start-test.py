import math

R1 = int(input('Введите R1: '))
R2 = int(input('Введите R2: '))
H = int(input('Введите H: '))


def in2(number):
    return number * number


S = (1 / 3) * math.pi * H * (in2(R1) + R1 * R2 + in2(R2))
print(S)
