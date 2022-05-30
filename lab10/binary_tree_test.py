import unittest
import random
from lab10.film import Film
from lab10.binary_tree import BinaryTree


class MyTestCase(unittest.TestCase):

    def test_something(self):

        def run_test():
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

            random.shuffle(names)

            test_list = []

            for i in range(10):
                test_list.append(Film(
                    names[i],
                    random.randint(2000, 2022),
                    random.randint(120, 180),
                    'action',
                    'Hollywood'
                ))

            test_subject_1 = test_list[6]
            test_subject_2 = test_list[9]

            bin_tree = BinaryTree()

            for film in test_list:
                bin_tree[film.name] = film

            bin_tree.remove(test_subject_1.name)
            bin_tree.remove(test_subject_2.name)

            self.assertEqual(None, bin_tree[test_subject_1.name])

            self.assertEqual(test_list[0], bin_tree[test_list[0].name])
            self.assertEqual(test_list[1], bin_tree[test_list[1].name])
            self.assertEqual(test_list[2], bin_tree[test_list[2].name])
            self.assertEqual(test_list[3], bin_tree[test_list[3].name])

            self.assertEqual(None, bin_tree[test_subject_2.name])

            self.assertEqual(test_list[4], bin_tree[test_list[4].name])
            self.assertEqual(test_list[5], bin_tree[test_list[5].name])
            self.assertEqual(test_list[7], bin_tree[test_list[7].name])
            self.assertEqual(test_list[8], bin_tree[test_list[8].name])

        for i in range(10_000):
            run_test()


if __name__ == '__main__':
    unittest.main()
