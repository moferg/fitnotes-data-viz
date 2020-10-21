# Marshall Ferguson - 10/2020

# Imports

import unittest
import fitnotes_data_viz

class TestFitnotesDataViz(unittest.TestCase):

    def test_unique_values(self):
        self.assertEqual(fitnotes_data_viz.unique_values([1, 1, 2, 2, 3, 3]), [1, 2, 3])


if __name__ == '__main__':
    unittest.main()