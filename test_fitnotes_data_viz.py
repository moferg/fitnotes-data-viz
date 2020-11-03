# Marshall Ferguson - 10/2020

# Imports

import unittest
import fitnotes_data_viz

class TestFitnotesDataViz(unittest.TestCase):

    def test_unique_values(self):
        self.assertEqual(fitnotes_data_viz.unique_values([1, 1, 2, 2, 3, 3]), [1, 2, 3])

    def test_sets_on_date(self):
        self.assertEqual(fitnotes_data_viz.sets_on_date, [18, 27, 20, 27, 28, 20, 26, 27, 19, 27, 28, 19, 25, 28, 19, 28, 30, 20])
        self.assertEqual(len(fitnotes_data_viz.sets_on_date), 18)

    def test_volumes_on_unique_dates(self):
        self.assertEqual(fitnotes_data_viz.volumes_on_unique_dates, 
        [10470.0, 11905.0, 13925.0, 17905.0, 14780.0, 15470.0, 20020.0, 14280.0, 16380.0, 21010.0, 15280.0, 17230.0, 22395.0, 
        16265.0, 17715.0, 22840.0, 16565.0, 17740.0])
        self.assertEqual(len(fitnotes_data_viz.volumes_on_unique_dates), 18)

if __name__ == '__main__':
    unittest.main()