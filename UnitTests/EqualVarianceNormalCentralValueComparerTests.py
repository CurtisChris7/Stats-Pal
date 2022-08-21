import unittest
from PopulationComparisonInference.CentralValue.EqualVarianceNormalCentralValueComparer import EqualVarianceNormalCentralValueComparer

class EqualVarianceNormalCentralValueComparerTests(unittest.TestCase):
    """Unit testing class for the EqualVarianceNormalCentralValueComparer"""

    def test_constructor_sample1None(self):
        """Tests that the constructor raises an error with null sample1"""
        self.assertRaises(ValueError, EqualVarianceNormalCentralValueComparer, sample1=None, sample2 = [1, 2])

    def test_constructor_sample1Empty(self):
        """Tests that the constructor raises an error with empty sample1"""
        self.assertRaises(ValueError, EqualVarianceNormalCentralValueComparer, sample1=[], sample2 = [1, 2])

    def test_constructor_sample2None(self):
        """Tests that the constructor raises an error with null sample2"""
        self.assertRaises(ValueError, EqualVarianceNormalCentralValueComparer, sample1 = [1, 2], sample2=None)

    def test_constructor_sample2Empty(self):
        """Tests that the constructor raises an error with empty sample2"""
        self.assertRaises(ValueError, EqualVarianceNormalCentralValueComparer, sample1 = [1, 2], sample2=[])

    def test_constructor_tDistNone(self):
        """Tests that the constructor raises an error with null tDist"""
        self.assertRaises(ValueError, EqualVarianceNormalCentralValueComparer, sample1 = [1, 2], sample2 = [1, 2], tDist=None)

    def test_getConfidenceInterval_whenCalled(self):
        """Tests the value of getConfidenceInterval when called"""
        comparer: EqualVarianceNormalCentralValueComparer = EqualVarianceNormalCentralValueComparer([1, 2], [1, 2])
        # We set specific values for our test
        comparer.mean1 = 10.37
        comparer.n1 = 10
        comparer.stdDev1 = 0.324
        comparer.var1 = comparer.stdDev1 ** 2
        comparer.mean2 = 9.83
        comparer.n2 = 10
        comparer.stdDev2 = 0.2406
        comparer.var2 = comparer.stdDev2 ** 2
        comparer.df = 18
        comparer.sp = 0.285
        interval: tuple = comparer.getConfidenceInterval(0.95)
        self.assertAlmostEqual(interval[0], 0.27222514364783806)
        self.assertAlmostEqual(interval[1], 0.8077748563521603)

    def test_getConfidenceInterval_confidenceLevelNone(self):
        """Tests that getConfidenceInterval raises an error when given a null confidence level"""
        comparer: EqualVarianceNormalCentralValueComparer = EqualVarianceNormalCentralValueComparer([1, 2], [1, 2])
        self.assertRaises(ValueError, comparer.getConfidenceInterval, None)

    def test_getConfidenceInterval_confidenceLevelNegative(self):
        """Tests that getConfidenceInterval raises an error when given a negative confidence level"""
        comparer: EqualVarianceNormalCentralValueComparer = EqualVarianceNormalCentralValueComparer([1, 2], [1, 2])
        self.assertRaises(ValueError, comparer.getConfidenceInterval, -1)

    def test_getConfidenceInterval_confidenceLevelTooLarge(self):
        """Tests that getConfidenceInterval raises an error when given a confidence level that is over 1"""
        comparer: EqualVarianceNormalCentralValueComparer = EqualVarianceNormalCentralValueComparer([1, 2], [1, 2])
        self.assertRaises(ValueError, comparer.getConfidenceInterval, 2)

    def test_getTestStatistic_whenCalled(self):
        """Tests the value of getTestStatistic when called"""
        comparer: EqualVarianceNormalCentralValueComparer = EqualVarianceNormalCentralValueComparer([1, 2], [1, 2])
        # We set specific values for our test
        comparer.mean1 = 39.67
        comparer.n1 = 12
        comparer.stdDev1 = 13.86
        comparer.var1 = comparer.stdDev1 ** 2
        comparer.mean2 = 26.58
        comparer.n2 = 12
        comparer.stdDev2 = 14.36
        comparer.var2 = comparer.stdDev2 ** 2
        comparer.df = 22
        comparer.sp = 14.11
        self.assertAlmostEqual(comparer.getTestStatistic(5), 1.4044204124107666)

    def test_getTestStatistic_testDetlaNone(self):
        """Tests that getTestStatistic raises an error when given a null testDelta"""
        comparer: EqualVarianceNormalCentralValueComparer = EqualVarianceNormalCentralValueComparer([1, 2], [1, 2])
        self.assertRaises(ValueError, comparer.getTestStatistic, None)

    def test_rightTailDeltaSignificanceTest_whenCalled(self):
        """Tests the value of rightTailDeltaSignificanceTest when called"""
        comparer: EqualVarianceNormalCentralValueComparer = EqualVarianceNormalCentralValueComparer([1, 2], [1, 2])
        # We set specific values for our test
        comparer.mean1 = 39.67
        comparer.n1 = 12
        comparer.stdDev1 = 13.86
        comparer.var1 = comparer.stdDev1 ** 2
        comparer.mean2 = 26.58
        comparer.n2 = 12
        comparer.stdDev2 = 14.36
        comparer.var2 = comparer.stdDev2 ** 2
        comparer.df = 22
        comparer.sp = 14.11
        self.assertFalse(comparer.rightTailDeltaSignificanceTest(5, 0.95))

    def test_rightTailDeltaSignificanceTest_type1ConfidenceNone(self):
        """Tests that rightTailDeltaSignificanceTest raises an error when given a null type1Confidence"""
        analyzer: EqualVarianceNormalCentralValueComparer = EqualVarianceNormalCentralValueComparer([1, 2], [1, 2])
        self.assertRaises(ValueError,analyzer.rightTailDeltaSignificanceTest, delta=0.3, type1Confidence=None)

    def test_rightTailDeltaSignificanceTest_type1ConfidenceNegative(self):
        """Tests that rightTailDeltaSignificanceTest raises an error when given a negative type1Confidence"""
        analyzer: EqualVarianceNormalCentralValueComparer = EqualVarianceNormalCentralValueComparer([1, 2], [1, 2])
        self.assertRaises(ValueError,analyzer.rightTailDeltaSignificanceTest, delta=0.3, type1Confidence=-1)

    def test_rightTailDeltaSignificanceTest_type1ConfidenceTooLarge(self):
        """Tests that rightTailDeltaSignificanceTest raises an error when given a type1Confidence over 1"""
        analyzer: EqualVarianceNormalCentralValueComparer = EqualVarianceNormalCentralValueComparer([1, 2], [1, 2])
        self.assertRaises(ValueError,analyzer.rightTailDeltaSignificanceTest, delta=0.3, type1Confidence=2)

    def test_rightTailDeltaSignificanceTest_deltaNone(self):
        """Tests that rightTailDeltaSignificanceTest raises an error when given a null delta"""
        analyzer: EqualVarianceNormalCentralValueComparer = EqualVarianceNormalCentralValueComparer([1, 2], [1, 2])
        self.assertRaises(ValueError,analyzer.rightTailDeltaSignificanceTest, delta=None, type1Confidence=0.95)

    def test_leftTailDeltaSignificanceTest_whenCalled(self):
        """Tests the value of leftTailDeltaSignificanceTest when called"""
        comparer: EqualVarianceNormalCentralValueComparer = EqualVarianceNormalCentralValueComparer([1, 2], [1, 2])
        # We set specific values for our test
        comparer.mean1 = 39.67
        comparer.n1 = 12
        comparer.stdDev1 = 13.86
        comparer.var1 = comparer.stdDev1 ** 2
        comparer.mean2 = 26.58
        comparer.n2 = 12
        comparer.stdDev2 = 14.36
        comparer.var2 = comparer.stdDev2 ** 2
        comparer.df = 22
        comparer.sp = 14.11
        self.assertFalse(comparer.leftTailDeltaSignificanceTest(0, 0.95))

    def test_leftTailDeltaSignificanceTest_type1ConfidenceNone(self):
        """Tests that leftTailDeltaSignificanceTest raises an error when given a null type1Confidence"""
        analyzer: EqualVarianceNormalCentralValueComparer = EqualVarianceNormalCentralValueComparer([1, 2], [1, 2])
        self.assertRaises(ValueError,analyzer.leftTailDeltaSignificanceTest, delta=0.3, type1Confidence=None)

    def test_leftTailDeltaSignificanceTest_type1ConfidenceNegative(self):
        """Tests that leftTailDeltaSignificanceTest raises an error when given a negative type1Confidence"""
        analyzer: EqualVarianceNormalCentralValueComparer = EqualVarianceNormalCentralValueComparer([1, 2], [1, 2])
        self.assertRaises(ValueError,analyzer.leftTailDeltaSignificanceTest, delta=0.3, type1Confidence=-1)

    def test_leftTailDeltaSignificanceTest_type1ConfidenceTooLarge(self):
        """Tests that leftTailDeltaSignificanceTest raises an error when given a type1Confidence over 1"""
        analyzer: EqualVarianceNormalCentralValueComparer = EqualVarianceNormalCentralValueComparer([1, 2], [1, 2])
        self.assertRaises(ValueError,analyzer.leftTailDeltaSignificanceTest, delta=0.3, type1Confidence=2)

    def test_leftTailDeltaSignificanceTest_deltaNone(self):
        """Tests that leftTailDeltaSignificanceTest raises an error when given a null delta"""
        analyzer: EqualVarianceNormalCentralValueComparer = EqualVarianceNormalCentralValueComparer([1, 2], [1, 2])
        self.assertRaises(ValueError,analyzer.leftTailDeltaSignificanceTest, delta=None, type1Confidence=0.95)

    def test_twinTailDeltaSignificanceTest_whenCalled(self):
        """Tests the value of twinTailDeltaSignificanceTest when called"""
        comparer: EqualVarianceNormalCentralValueComparer = EqualVarianceNormalCentralValueComparer([1, 2], [1, 2])
        # We set specific values for our test
        comparer.mean1 = 39.67
        comparer.n1 = 12
        comparer.stdDev1 = 13.86
        comparer.var1 = comparer.stdDev1 ** 2
        comparer.mean2 = 26.58
        comparer.n2 = 12
        comparer.stdDev2 = 14.36
        comparer.var2 = comparer.stdDev2 ** 2
        comparer.df = 22
        comparer.sp = 14.11
        self.assertFalse(comparer.twinTailDeltaSignificanceTest(5, 0.95))

    def test_twinTailDeltaSignificanceTest_type1ConfidenceNone(self):
        """Tests that twinTailDeltaSignificanceTest raises an error when given a null type1Confidence"""
        analyzer: EqualVarianceNormalCentralValueComparer = EqualVarianceNormalCentralValueComparer([1, 2], [1, 2])
        self.assertRaises(ValueError,analyzer.twinTailDeltaSignificanceTest, delta=0.3, type1Confidence=None)

    def test_twinTailDeltaSignificanceTest_type1ConfidenceNegative(self):
        """Tests that twinTailDeltaSignificanceTest raises an error when given a negative type1Confidence"""
        analyzer: EqualVarianceNormalCentralValueComparer = EqualVarianceNormalCentralValueComparer([1, 2], [1, 2])
        self.assertRaises(ValueError,analyzer.twinTailDeltaSignificanceTest, delta=0.3, type1Confidence=-1)

    def test_twinTailDeltaSignificanceTest_type1ConfidenceTooLarge(self):
        """Tests that twinTailDeltaSignificanceTest raises an error when given a type1Confidence over 1"""
        analyzer: EqualVarianceNormalCentralValueComparer = EqualVarianceNormalCentralValueComparer([1, 2], [1, 2])
        self.assertRaises(ValueError,analyzer.twinTailDeltaSignificanceTest, delta=0.3, type1Confidence=2)

    def test_twinTailDeltaSignificanceTest_deltaNone(self):
        """Tests that twinTailDeltaSignificanceTest raises an error when given a null delta"""
        analyzer: EqualVarianceNormalCentralValueComparer = EqualVarianceNormalCentralValueComparer([1, 2], [1, 2])
        self.assertRaises(ValueError,analyzer.twinTailDeltaSignificanceTest, delta=None, type1Confidence=0.95)
