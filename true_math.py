from math import inf

result = ()

def divide(first, second = 0):
    try:
        first / second
    except:
        print(f'true_math is: {float(inf)}')

print(divide(result))