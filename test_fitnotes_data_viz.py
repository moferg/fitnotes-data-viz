# Marshall Ferguson - 10/2020

# Imports

import unittest
import fitnotes_data_viz

class TestFitnotesDataViz(unittest.TestCase):

    def test_unique_values(self):
        self.assertEqual(fitnotes_data_viz.unique_values([1, 1, 2, 2, 3, 3]), [1, 2, 3])

    def test_sets_on_date(self):
        self.assertEqual(fitnotes_data_viz.sets_on_date, [18, 27, 20, 27, 28, 20, 26, 27, 19, 27, 28, 19, 25, 28, 19, 28, 30, 20])

    # def test_volumes_for_workout(self):
    #     self.assertEqual(fitnotes_data_viz.volumes_for_workout, [])

    def test_volumes_on_unique_dates(self):
        self.assertEqual(fitnotes_data_viz.volumes_on_unique_dates, 
        [10470, 11905, 13925, 17905, 14780, 15470, 20020, 14280, 16380, 21010, 15280, 17230, 22395, 16265, 17715, 22840, 16565, 17740])

if __name__ == '__main__':
    unittest.main()