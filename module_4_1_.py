from fake_math import divide as fake_divide
from true_math import divide as true_divide

# First one
# fake_result = fake_divide(0)
# true_result = true_divide(-0)


# Or this one below:
match input('This 0 or this -0 '):
    case '0':
        fake_divide(0)
    case '-0':
        true_divide(-0)
    case _:
        print('See you later!')