import unittest
import random
from Utilities.SampleUtilities import SampleUtilities

TEST_VALUES: list = [0.593, 0.142 ,0.329 ,0.691 ,0.231, 0.793, 0.519, 0.392, 0.418]

class SampleUtilitiesTests(unittest.TestCase):
    """Class for unit testing SampleUtilities"""

    def test_estimateMean_whenCalled(self):
        """Tests the value of estimateMean when called with legal arguments"""
        self.assertEqual(SampleUtilities.estimateMean(TEST_VALUES), 0.45644444444444443)

    def test_estimateMean_valuesNull(self):
        """Tests that estimateMean raises an error when called with null values"""
        self.assertRaises(ValueError, SampleUtilities.estimateMean, None)

    def test_estimateMean_valuesEmpty(self):
        """Tests that estimateMean raises an error when called with empty values"""
        self.assertRaises(ValueError, SampleUtilities.estimateMean, [])

    def test_estimateStdDev_whenCalled(self):
        """Tests the value of estimateStdDev when called with legal arguments"""
        self.assertEqual(SampleUtilities.estimateStdDev(TEST_VALUES), 0.21284390472310402)

    def test_estimateStdDev_valuesNull(self):
        """Tests that estimateStdDev raises an error when called with null values"""
        self.assertRaises(ValueError, SampleUtilities.estimateStdDev, None)

    def test_estimateStdDev_valuesEmpty(self):
        """Tests that estimateStdDev raises an error when called with empty values"""
        self.assertRaises(ValueError, SampleUtilities.estimateStdDev, [])

    def test_estimateVariance_whenCalled(self):
        """Tests the value of estimateVariance when called with legal arguments"""
        self.assertEqual(SampleUtilities.estimateVariance(TEST_VALUES), 0.04530252777777778)

    def test_estimateVariance_valuesNull(self):
        """Tests that estimateVariance raises an error when called with null values"""
        self.assertRaises(ValueError, SampleUtilities.estimateVariance, None)

    def test_estimateVariance_valuesEmpty(self):
        """Tests that estimateVariance raises an error when called with empty values"""
        self.assertRaises(ValueError, SampleUtilities.estimateVariance, [])

    def test_bootstrap_whenCalled(self):
        """Tests the value of bootstrap when called with legal arguments"""
        random.seed(1)
        self.assertEqual(SampleUtilities.bootstrap(TEST_VALUES), [0.142, 0.392, 0.519, 0.329, 0.231, 0.231, 0.793, 0.392, 0.593])

    def test_bootstrap_valuesNull(self):
        """Tests that bootstrap raises an error when called with null values"""
        self.assertRaises(ValueError, SampleUtilities.bootstrap, None)

    def test_bootstrap_valuesEmpty(self):
        """Tests that bootstrap raises an error when called with empty values"""
        self.assertRaises(ValueError, SampleUtilities.bootstrap, [])
