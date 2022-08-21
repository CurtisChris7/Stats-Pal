import unittest
from PopulationComparisonInference.CentralValue.NormalCentralValueComparer import NormalCentralValueComparer

class NormalCentralValueComparerTests(unittest.TestCase):
    """Unit testing class for the NormalCentralValueComparer"""

    def test_constructor_sample1None(self):
        """Tests that the constructor raises an error with null sample1"""
        self.assertRaises(ValueError, NormalCentralValueComparer, sample1=None, sample2 = [1, 2])

    def test_constructor_sample1Empty(self):
        """Tests that the constructor raises an error with empty sample1"""
        self.assertRaises(ValueError, NormalCentralValueComparer, sample1=[], sample2 = [1, 2])

    def test_constructor_sample2None(self):
        """Tests that the constructor raises an error with null sample2"""
        self.assertRaises(ValueError, NormalCentralValueComparer, sample1 = [1, 2], sample2=None)

    def test_constructor_sample2Empty(self):
        """Tests that the constructor raises an error with empty sample2"""
        self.assertRaises(ValueError, NormalCentralValueComparer, sample1 = [1, 2], sample2=[])

    def test_constructor_tDistNone(self):
        """Tests that the constructor raises an error with null tDist"""
        self.assertRaises(ValueError, NormalCentralValueComparer, sample1 = [1, 2], sample2 = [1, 2], tDist=None)

    def test_getConfidenceInterval_whenCalled(self):
        """Tests the value of getConfidenceInterval when called"""
        comparer: NormalCentralValueComparer = NormalCentralValueComparer([1, 2], [1, 2])
        # We set specific values for our test
        comparer.mean1 = 25.2
        comparer.n1 = 33
        comparer.stdDev1 = 8.6
        comparer.var1 = comparer.stdDev1 ** 2
        comparer.mean2 = 33.9
        comparer.n2 = 12
        comparer.stdDev2 = 17.4
        comparer.var2 = comparer.stdDev2 ** 2
        comparer.df = 13
        interval: tuple = comparer.getConfidenceInterval(0.95)
        self.assertAlmostEqual(interval[0], -20.023137442704808)
        self.assertAlmostEqual(interval[1], 2.6231374427048095)

    def test_getConfidenceInterval_confidenceLevelNone(self):
        """Tests that getConfidenceInterval raises an error when given a null confidence level"""
        comparer: NormalCentralValueComparer = NormalCentralValueComparer([1, 2], [1, 2])
        self.assertRaises(ValueError, comparer.getConfidenceInterval, None)

    def test_getConfidenceInterval_confidenceLevelNegative(self):
        """Tests that getConfidenceInterval raises an error when given a negative confidence level"""
        comparer: NormalCentralValueComparer = NormalCentralValueComparer([1, 2], [1, 2])
        self.assertRaises(ValueError, comparer.getConfidenceInterval, -1)

    def test_getConfidenceInterval_confidenceLevelTooLarge(self):
        """Tests that getConfidenceInterval raises an error when given a confidence level that is over 1"""
        comparer: NormalCentralValueComparer = NormalCentralValueComparer([1, 2], [1, 2])
        self.assertRaises(ValueError, comparer.getConfidenceInterval, 2)

    def test_getTestStatistic_whenCalled(self):
        """Tests the value of getTestStatistic when called"""
        comparer: NormalCentralValueComparer = NormalCentralValueComparer([1, 2], [1, 2])
        # We set specific values for our test
        comparer.mean1 = 25.2
        comparer.n1 = 33
        comparer.stdDev1 = 8.6
        comparer.var1 = comparer.stdDev1 ** 2
        comparer.mean2 = 33.9
        comparer.n2 = 12
        comparer.stdDev2 = 17.4
        comparer.var2 = comparer.stdDev2 ** 2
        comparer.df = 13
        self.assertAlmostEqual(comparer.getTestStatistic(0), -1.6598939477962489)

    def test_getTestStatistic_testDetlaNone(self):
        """Tests that getTestStatistic raises an error when given a null testDelta"""
        comparer: NormalCentralValueComparer = NormalCentralValueComparer([1, 2], [1, 2])
        self.assertRaises(ValueError, comparer.getTestStatistic, None)

    def test_rightTailDeltaSignificanceTest_whenCalled(self):
        """Tests the value of rightTailDeltaSignificanceTest when called"""
        comparer: NormalCentralValueComparer = NormalCentralValueComparer([1, 2], [1, 2])
        # We set specific values for our test
        comparer.mean1 = 25.2
        comparer.n1 = 33
        comparer.stdDev1 = 8.6
        comparer.var1 = comparer.stdDev1 ** 2
        comparer.mean2 = 33.9
        comparer.n2 = 12
        comparer.stdDev2 = 17.4
        comparer.var2 = comparer.stdDev2 ** 2
        comparer.df = 13
        self.assertFalse(comparer.rightTailDeltaSignificanceTest(0, 0.95))

    def test_rightTailDeltaSignificanceTest_whenCalled(self):
        comparer: NormalCentralValueComparer = NormalCentralValueComparer([1, 2], [1, 2])
        self.assertRaises(ValueError, comparer.getTestStatistic, None)

    def test_rightTailDeltaSignificanceTest_type1ConfidenceNone(self):
        """Tests that rightTailDeltaSignificanceTest raises an error when given a null type1Confidence"""
        analyzer: NormalCentralValueComparer = NormalCentralValueComparer([1, 2], [1, 2])
        self.assertRaises(ValueError,analyzer.rightTailDeltaSignificanceTest, delta=0.3, type1Confidence=None)

    def test_rightTailDeltaSignificanceTest_type1ConfidenceNegative(self):
        """Tests that rightTailDeltaSignificanceTest raises an error when given a negative type1Confidence"""
        analyzer: NormalCentralValueComparer = NormalCentralValueComparer([1, 2], [1, 2])
        self.assertRaises(ValueError,analyzer.rightTailDeltaSignificanceTest, delta=0.3, type1Confidence=-1)

    def test_rightTailDeltaSignificanceTest_type1ConfidenceTooLarge(self):
        """Tests that rightTailDeltaSignificanceTest raises an error when given a type1Confidence over 1"""
        analyzer: NormalCentralValueComparer = NormalCentralValueComparer([1, 2], [1, 2])
        self.assertRaises(ValueError,analyzer.rightTailDeltaSignificanceTest, delta=0.3, type1Confidence=2)

    def test_rightTailDeltaSignificanceTest_deltaNone(self):
        """Tests that rightTailDeltaSignificanceTest raises an error when given a null delta"""
        analyzer: NormalCentralValueComparer = NormalCentralValueComparer([1, 2], [1, 2])
        self.assertRaises(ValueError,analyzer.rightTailDeltaSignificanceTest, delta=None, type1Confidence=0.95)

    def test_leftTailDeltaSignificanceTest_whenCalled(self):
        """Tests the value of leftTailDeltaSignificanceTest when called"""
        comparer: NormalCentralValueComparer = NormalCentralValueComparer([1, 2], [1, 2])
        # We set specific values for our test
        comparer.mean1 = 25.2
        comparer.n1 = 33
        comparer.stdDev1 = 8.6
        comparer.var1 = comparer.stdDev1 ** 2
        comparer.mean2 = 33.9
        comparer.n2 = 12
        comparer.stdDev2 = 17.4
        comparer.var2 = comparer.stdDev2 ** 2
        comparer.df = 13
        self.assertFalse(comparer.leftTailDeltaSignificanceTest(0, 0.95))

    def test_leftTailDeltaSignificanceTest_whenCalled(self):
        comparer: NormalCentralValueComparer = NormalCentralValueComparer([1, 2], [1, 2])
        self.assertRaises(ValueError, comparer.getTestStatistic, None)

    def test_leftTailDeltaSignificanceTest_type1ConfidenceNone(self):
        """Tests that leftTailDeltaSignificanceTest raises an error when given a null type1Confidence"""
        analyzer: NormalCentralValueComparer = NormalCentralValueComparer([1, 2], [1, 2])
        self.assertRaises(ValueError,analyzer.leftTailDeltaSignificanceTest, delta=0.3, type1Confidence=None)

    def test_leftTailDeltaSignificanceTest_type1ConfidenceNegative(self):
        """Tests that leftTailDeltaSignificanceTest raises an error when given a negative type1Confidence"""
        analyzer: NormalCentralValueComparer = NormalCentralValueComparer([1, 2], [1, 2])
        self.assertRaises(ValueError,analyzer.leftTailDeltaSignificanceTest, delta=0.3, type1Confidence=-1)

    def test_leftTailDeltaSignificanceTest_type1ConfidenceTooLarge(self):
        """Tests that leftTailDeltaSignificanceTest raises an error when given a type1Confidence over 1"""
        analyzer: NormalCentralValueComparer = NormalCentralValueComparer([1, 2], [1, 2])
        self.assertRaises(ValueError,analyzer.leftTailDeltaSignificanceTest, delta=0.3, type1Confidence=2)

    def test_leftTailDeltaSignificanceTest_deltaNone(self):
        """Tests that leftTailDeltaSignificanceTest raises an error when given a null delta"""
        analyzer: NormalCentralValueComparer = NormalCentralValueComparer([1, 2], [1, 2])
        self.assertRaises(ValueError,analyzer.leftTailDeltaSignificanceTest, delta=None, type1Confidence=0.95)

    def test_twinTailDeltaSignificanceTest_whenCalled(self):
        """Tests the value of twinTailDeltaSignificanceTest when called"""
        comparer: NormalCentralValueComparer = NormalCentralValueComparer([1, 2], [1, 2])
        # We set specific values for our test
        comparer.mean1 = 25.2
        comparer.n1 = 33
        comparer.stdDev1 = 8.6
        comparer.var1 = comparer.stdDev1 ** 2
        comparer.mean2 = 33.9
        comparer.n2 = 12
        comparer.stdDev2 = 17.4
        comparer.var2 = comparer.stdDev2 ** 2
        comparer.df = 13
        self.assertTrue(comparer.twinTailDeltaSignificanceTest(0, 0.95))

    def test_twinTailDeltaSignificanceTest_type1ConfidenceNone(self):
        """Tests that twinTailDeltaSignificanceTest raises an error when given a null type1Confidence"""
        analyzer: NormalCentralValueComparer = NormalCentralValueComparer([1, 2], [1, 2])
        self.assertRaises(ValueError,analyzer.twinTailDeltaSignificanceTest, delta=0.3, type1Confidence=None)

    def test_twinTailDeltaSignificanceTest_type1ConfidenceNegative(self):
        """Tests that twinTailDeltaSignificanceTest raises an error when given a negative type1Confidence"""
        analyzer: NormalCentralValueComparer = NormalCentralValueComparer([1, 2], [1, 2])
        self.assertRaises(ValueError,analyzer.twinTailDeltaSignificanceTest, delta=0.3, type1Confidence=-1)

    def test_twinTailDeltaSignificanceTest_type1ConfidenceTooLarge(self):
        """Tests that twinTailDeltaSignificanceTest raises an error when given a type1Confidence over 1"""
        analyzer: NormalCentralValueComparer = NormalCentralValueComparer([1, 2], [1, 2])
        self.assertRaises(ValueError,analyzer.twinTailDeltaSignificanceTest, delta=0.3, type1Confidence=2)

    def test_twinTailDeltaSignificanceTest_deltaNone(self):
        """Tests that twinTailDeltaSignificanceTest raises an error when given a null delta"""
        analyzer: NormalCentralValueComparer = NormalCentralValueComparer([1, 2], [1, 2])
        self.assertRaises(ValueError,analyzer.twinTailDeltaSignificanceTest, delta=None, type1Confidence=0.95)
