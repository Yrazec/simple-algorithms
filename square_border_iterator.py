"""Script to iterate only over a square border in a two-dimensional array."""

import os
import time


def print_data(data: list[list[str]], sleep_time: float = 1.0) -> None:
    """
    Print two-dimensional array of strings and sleep.

    :param list[list[str]] data: two-dimensional array of strings
    :param float sleep_time: sleep time in seconds
    """

    for row in data:
        print(''.join(row))
    time.sleep(sleep_time)


def clear_data(size: int, center: int) -> list[list[str]]:
    """
    Clear two-dimensional array of strings and place X in the center.

    :param int size: square-size of the data array
    :param int center: center index (i and j)
    :return: cleared data
    """

    data = [[f' ' for _ in range(size)] for _ in range(size)]
    data[center][center] = 'X'
    return data


s = 11
if s % 2 == 0:
    raise Exception('Please provide even size value!')
c = int((s - 1) / 2)

border_character = '+'

while True:

    dim = 1
    os.system('cls')
    dataset = clear_data(size=s, center=c)
    print_data(data=dataset)

    for iteration in range(c):

        for i, _ in enumerate(dataset[c - dim]):
            if c - dim <= i <= c + dim:
                dataset[c - dim][i] = border_character

        for i, _ in enumerate(dataset[c + dim]):
            if c - dim <= i <= c + dim:
                dataset[c + dim][i] = border_character

        for i, _ in enumerate(dataset[c - dim: c + dim + 1]):
                dataset[i + c - dim][c - dim] = border_character

        for i, _ in enumerate(dataset[c - dim: c + dim + 1]):
            dataset[i + c - dim][c + dim] = border_character

        dim += 1
        os.system('cls')
        print_data(data=dataset)
        dataset = clear_data(size=s, center=c)
