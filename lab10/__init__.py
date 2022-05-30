import unittest
import random
from lab10.film import Film
from lab10.binary_tree import BinaryTree


def main():
    names = [
        'Top gun',
        'Avatar',
        'Illovaysk',
        'Inception',
        'Pacific rim',
        'Transformers',
        'Interstellar',
        'Oblivion',
        'Dune',
        'Zahar Berkut'
    ]

    genres = [
        'action',
        'adventure'
    ]

    studios = [
        '20th Century Fox',
        'Legendary',
        'Marvel',
        'DC'
    ]

    random.shuffle(names)

    test_list = []

    for i in range(10):
        test_list.append(Film(
            names[i],
            random.randint(2000, 2022),
            random.randint(120, 180),
            genres[random.randint(0, len(genres) - 1)],
            studios[random.randint(0, len(studios) - 1)]
        ))

    test_subject_1 = test_list[6]
    test_subject_2 = test_list[9]

    bin_tree = BinaryTree()

    for film in test_list:
        bin_tree[film.name] = film

    bin_tree.remove(test_subject_1.name)

    print('\nInitial tree:')
    for key, film in bin_tree.top_to_bottom_list():
        print(film)

    bin_tree.remove(test_subject_2.name)

    print(f'\nPrint only films made by {studios[1]}:')
    for key, film in bin_tree.get_by(lambda key, value: value.studio == studios[1]):
        print(film)

    bin_tree.remove_by(lambda key, value: value.genre == genres[1])

    print(f'\nRemove films of genre {genres[1]}:')
    for key, film in bin_tree.top_to_bottom_list():
        print(film)
