def sum_numbers(*args):
    sum_num = 0
    for number in args:
        sum_num += number
    return sum_num


def show_user(*kwargs):
    for val in kwargs.items():
        print(val)

show_user(
    name="Ainur",
    age=19,
    city="Kazan"
)