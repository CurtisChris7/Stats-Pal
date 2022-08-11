import unittest
from Utilities.BinomialDistribution.BinomialDistribution import BinomialDistribution

class BinomialDistributionTests(unittest.TestCase):
    """Unit testing class for the BinomialDistribution"""

    def test_getLeftTailArea_whenCalled(self):
        """Tests the value of getLeftTailArea when called in normal bounds"""
        dist: BinomialDistribution = BinomialDistribution()
        self.assertAlmostEqual(dist.getLeftTailArea(3, 15, .2),  0.6481621045739525)

    def test_getLeftTailArea_NegativeSuccesses(self):
        """Tests the value of getLeftTailArea when called in normal bounds"""
        dist: BinomialDistribution = BinomialDistribution()
        self.assertRaises(ValueError, dist.getLeftTailArea, -1, 5, 0.5)

    def test_getLeftTailArea_NullSuccesses(self):
        """Tests that getLeftTailArea throws an exception with a null success count"""
        dist: BinomialDistribution = BinomialDistribution()
        self.assertRaises(ValueError, dist.getLeftTailArea, None, 5, 0.5)

    def test_getLeftTailArea_NegativeTrials(self):
        """Tests that getLeftTailArea throws an exception with a negative success count"""
        dist: BinomialDistribution = BinomialDistribution()
        self.assertRaises(ValueError, dist.getLeftTailArea, 4, -1, 0.5)

    def test_getLeftTailArea_NullTrials(self):
        """Tests that getLeftTailArea throws an exception with a null trial count"""
        dist: BinomialDistribution = BinomialDistribution()
        self.assertRaises(ValueError, dist.getLeftTailArea, 4, None, 0.5)

    def test_getLeftTailArea_NegativeTrials(self):
        """Tests that getLeftTailArea throws an exception with a negative success count"""
        dist: BinomialDistribution = BinomialDistribution()
        self.assertRaises(ValueError, dist.getLeftTailArea, 4, -1, 0.5)

    def test_getLeftTailArea_NullLikelihood(self):
        """Tests that getLeftTailArea throws an exception with a null likelihood"""
        dist: BinomialDistribution = BinomialDistribution()
        self.assertRaises(ValueError, dist.getLeftTailArea, 4, 5, None)

    def test_getLeftTailArea_NegativeLikelihood(self):
        """Tests that getLeftTailArea throws an exception with a negative likelihood"""
        dist: BinomialDistribution = BinomialDistribution()
        self.assertRaises(ValueError, dist.getLeftTailArea, 4, 5, -1)

    def test_getLeftTailArea_TooLargeLikelihood(self):
        """Tests that getLeftTailArea throws an exception with a likelihood that is over 1"""
        dist: BinomialDistribution = BinomialDistribution()
        self.assertRaises(ValueError, dist.getLeftTailArea, 4, 5, -1)

    def test_getLeftTailArea_MoreSuccessesThanTrials(self):
        """Tests that getLeftTailArea throws an exception when there are more successes than trials"""
        dist: BinomialDistribution = BinomialDistribution()
        self.assertRaises(ValueError, dist.getLeftTailArea, 6, 5, 0.5)

    def test_pmf_whenCalled(self):
        """Tests the value of pmf when called in normal bounds"""
        dist: BinomialDistribution = BinomialDistribution()
        self.assertAlmostEqual(dist.pmf(3, 15, .2),  0.2501388953190402)

    def test_pmf_NegativeSuccesses(self):
        """Tests the value of pmf when called in normal bounds"""
        dist: BinomialDistribution = BinomialDistribution()
        self.assertRaises(ValueError, dist.pmf, -1, 5, 0.5)

    def test_pmf_NullSuccesses(self):
        """Tests that pmf throws an exception with a null success count"""
        dist: BinomialDistribution = BinomialDistribution()
        self.assertRaises(ValueError, dist.pmf, None, 5, 0.5)

    def test_pmf_NegativeTrials(self):
        """Tests that pmf throws an exception with a negative success count"""
        dist: BinomialDistribution = BinomialDistribution()
        self.assertRaises(ValueError, dist.pmf, 4, -1, 0.5)

    def test_pmf_NullTrials(self):
        """Tests that pmf throws an exception with a null trial count"""
        dist: BinomialDistribution = BinomialDistribution()
        self.assertRaises(ValueError, dist.pmf, 4, None, 0.5)

    def test_pmf_NegativeTrials(self):
        """Tests that pmf throws an exception with a negative success count"""
        dist: BinomialDistribution = BinomialDistribution()
        self.assertRaises(ValueError, dist.pmf, 4, -1, 0.5)

    def test_pmf_NullLikelihood(self):
        """Tests that pmf throws an exception with a null likelihood"""
        dist: BinomialDistribution = BinomialDistribution()
        self.assertRaises(ValueError, dist.pmf, 4, 5, None)

    def test_pmf_NegativeLikelihood(self):
        """Tests that pmf throws an exception with a negative likelihood"""
        dist: BinomialDistribution = BinomialDistribution()
        self.assertRaises(ValueError, dist.pmf, 4, 5, -1)

    def test_pmf_TooLargeLikelihood(self):
        """Tests that pmf throws an exception with a likelihood that is over 1"""
        dist: BinomialDistribution = BinomialDistribution()
        self.assertRaises(ValueError, dist.pmf, 4, 5, -1)

    def test_pmf_MoreSuccessesThanTrials(self):
        """Tests that pmf throws an exception when there are more successes than trials"""
        dist: BinomialDistribution = BinomialDistribution()
        self.assertRaises(ValueError, dist.pmf, 6, 5, 0.5)
