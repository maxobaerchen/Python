from cProfile import Profile
import pstats


def get_input(text_message, data_type, exception_type=ValueError):
    while True:
        user_input = input(text_message)
        try:
            num_input = data_type(user_input)
            return num_input
        except exception_type:
            print('This is no valid input')
            continue


def find_slow(function):
    with Profile() as pr:
        function()

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()


if __name__ == '__main__':
    pass
