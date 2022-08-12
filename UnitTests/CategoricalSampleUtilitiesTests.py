import unittest
from Utilities.CategoricalSampleUtilities import CategoricalSampleUtilities

TEST_VALUES = [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

class CategoricalSampleUtilitiesTests(unittest.TestCase):
    """Class for unit testing CategoricalSampleUtilities"""

    def test_estimateLikelihood_whenCalled(self):
        """Tests the value of estimateLikelihood when called with legal arguments"""
        self.assertEqual(CategoricalSampleUtilities.estimateLikelihood(TEST_VALUES), 4/15)

    def test_estimateLikelihood_valuesNull(self):
        """Tests that estimateLikelihood raises an error when called with null values"""
        self.assertRaises(ValueError, CategoricalSampleUtilities.estimateLikelihood, None)

    def test_estimateLikelihood_valuesEmpty(self):
        """Tests that estimateLikelihood raises an error when called with empty values"""
        self.assertRaises(ValueError, CategoricalSampleUtilities.estimateLikelihood, [])

    def test_estimateLikelihood_valuesEmpty(self):
        """Tests that estimateLikelihood raises an error when called with illegal values"""
        self.assertRaises(ValueError, CategoricalSampleUtilities.estimateLikelihood, [1, 3, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_estimateStandardError_whenCalled(self):
        """Tests the value of estimateStandardError when called with legal arguments"""
        self.assertEqual(CategoricalSampleUtilities.estimateStandardError(TEST_VALUES), 0.11417984514369003)

    def test_estimateStandardError_valuesNull(self):
        """Tests that estimateStandardError raises an error when called with null values"""
        self.assertRaises(ValueError, CategoricalSampleUtilities.estimateStandardError, None)

    def test_estimateStandardError_valuesEmpty(self):
        """Tests that estimateStandardError raises an error when called with empty values"""
        self.assertRaises(ValueError, CategoricalSampleUtilities.estimateStandardError, [])
