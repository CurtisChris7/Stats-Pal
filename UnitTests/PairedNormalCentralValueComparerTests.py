import unittest
from PopulationComparisonInference.CentralValue.PairedNormalCentralValueComparer import PairedNormalCentralValueComparer

SAMPLEA = [17.6, 20.2, 19.5, 11.3, 13.0, 16.3, 15.3, 16.2, 12.2, 14.8, 21.3, 22.1, 16.9, 17.6, 18.4]
SAMPLEB = [17.3, 19.1, 18.4, 11.5, 12.7, 15.8, 14.9, 15.3, 12.0, 14.2, 21.0, 21.0, 16.1, 16.7, 17.5]

class PairedNormalCentralValueComparerTests(unittest.TestCase):
    """Unit testing class for the PairedNormalCentralValueComparer"""

    def test_constructor_sample1None(self):
        """Tests that the constructor raises an error with null sample1"""
        self.assertRaises(ValueError, PairedNormalCentralValueComparer, sample1=None, sample2 = SAMPLEB)

    def test_constructor_sample1Empty(self):
        """Tests that the constructor raises an error with empty sample1"""
        self.assertRaises(ValueError, PairedNormalCentralValueComparer, sample1=[], sample2 = SAMPLEB)

    def test_constructor_sample2None(self):
        """Tests that the constructor raises an error with null sample2"""
        self.assertRaises(ValueError, PairedNormalCentralValueComparer, sample1 = SAMPLEA, sample2=None)

    def test_constructor_sample2Empty(self):
        """Tests that the constructor raises an error with empty sample2"""
        self.assertRaises(ValueError, PairedNormalCentralValueComparer, sample1 = SAMPLEA, sample2=[])

    def test_constructor_tDistNone(self):
        """Tests that the constructor raises an error with null tDist"""
        self.assertRaises(ValueError, PairedNormalCentralValueComparer, sample1 = SAMPLEA, sample2 = SAMPLEB, tDist=None)

    def test_getConfidenceInterval_whenCalled(self):
        """Tests the value of getConfidenceInterval when called"""
        comparer: PairedNormalCentralValueComparer = PairedNormalCentralValueComparer(SAMPLEA, SAMPLEB)
        interval: tuple = comparer.getConfidenceInterval(0.95)
        self.assertAlmostEqual(interval[0], 0.39494123616578886)
        self.assertAlmostEqual(interval[1], 0.8317254305008779)

    def test_getConfidenceInterval_confidenceLevelNone(self):
        """Tests that getConfidenceInterval raises an error when given a null confidence level"""
        comparer: PairedNormalCentralValueComparer = PairedNormalCentralValueComparer(SAMPLEA, SAMPLEB)
        self.assertRaises(ValueError, comparer.getConfidenceInterval, None)

    def test_getConfidenceInterval_confidenceLevelNegative(self):
        """Tests that getConfidenceInterval raises an error when given a negative confidence level"""
        comparer: PairedNormalCentralValueComparer = PairedNormalCentralValueComparer(SAMPLEA, SAMPLEB)
        self.assertRaises(ValueError, comparer.getConfidenceInterval, -1)

    def test_getConfidenceInterval_confidenceLevelTooLarge(self):
        """Tests that getConfidenceInterval raises an error when given a confidence level that is over 1"""
        comparer: PairedNormalCentralValueComparer = PairedNormalCentralValueComparer(SAMPLEA, SAMPLEB)
        self.assertRaises(ValueError, comparer.getConfidenceInterval, 2)

    def test_getTestStatistic_whenCalled(self):
        """Tests the value of getTestStatistic when called"""
        comparer: PairedNormalCentralValueComparer = PairedNormalCentralValueComparer(SAMPLEA, SAMPLEB)
        self.assertAlmostEqual(comparer.getTestStatistic(0), 6.0234284374303915)

    def test_getTestStatistic_testDetlaNone(self):
        """Tests that getTestStatistic raises an error when given a null testDelta"""
        comparer: PairedNormalCentralValueComparer = PairedNormalCentralValueComparer(SAMPLEA, SAMPLEB)
        self.assertRaises(ValueError, comparer.getTestStatistic, None)

    def test_rightTailDeltaSignificanceTest_whenCalled(self):
        """Tests the value of rightTailDeltaSignificanceTest when called"""
        comparer: PairedNormalCentralValueComparer = PairedNormalCentralValueComparer(SAMPLEA, SAMPLEB)
        self.assertTrue(comparer.rightTailDeltaSignificanceTest(0, 0.95))

    def test_rightTailDeltaSignificanceTest_type1ConfidenceNone(self):
        """Tests that rightTailDeltaSignificanceTest raises an error when given a null type1Confidence"""
        analyzer: PairedNormalCentralValueComparer = PairedNormalCentralValueComparer(SAMPLEA, SAMPLEB)
        self.assertRaises(ValueError,analyzer.rightTailDeltaSignificanceTest, delta=0.3, type1Confidence=None)

    def test_rightTailDeltaSignificanceTest_type1ConfidenceNegative(self):
        """Tests that rightTailDeltaSignificanceTest raises an error when given a negative type1Confidence"""
        analyzer: PairedNormalCentralValueComparer = PairedNormalCentralValueComparer(SAMPLEA, SAMPLEB)
        self.assertRaises(ValueError,analyzer.rightTailDeltaSignificanceTest, delta=0.3, type1Confidence=-1)

    def test_rightTailDeltaSignificanceTest_type1ConfidenceTooLarge(self):
        """Tests that rightTailDeltaSignificanceTest raises an error when given a type1Confidence over 1"""
        analyzer: PairedNormalCentralValueComparer = PairedNormalCentralValueComparer(SAMPLEA, SAMPLEB)
        self.assertRaises(ValueError,analyzer.rightTailDeltaSignificanceTest, delta=0.3, type1Confidence=2)

    def test_rightTailDeltaSignificanceTest_deltaNone(self):
        """Tests that rightTailDeltaSignificanceTest raises an error when given a null delta"""
        analyzer: PairedNormalCentralValueComparer = PairedNormalCentralValueComparer(SAMPLEA, SAMPLEB)
        self.assertRaises(ValueError,analyzer.rightTailDeltaSignificanceTest, delta=None, type1Confidence=0.95)

    def test_leftTailDeltaSignificanceTest_whenCalled(self):
        """Tests the value of leftTailDeltaSignificanceTest when called"""
        comparer: PairedNormalCentralValueComparer = PairedNormalCentralValueComparer(SAMPLEA, SAMPLEB)
        self.assertFalse(comparer.leftTailDeltaSignificanceTest(0, 0.95))

    def test_leftTailDeltaSignificanceTest_whenCalled(self):
        comparer: PairedNormalCentralValueComparer = PairedNormalCentralValueComparer(SAMPLEA, SAMPLEB)
        self.assertRaises(ValueError, comparer.getTestStatistic, None)

    def test_leftTailDeltaSignificanceTest_type1ConfidenceNone(self):
        """Tests that leftTailDeltaSignificanceTest raises an error when given a null type1Confidence"""
        analyzer: PairedNormalCentralValueComparer = PairedNormalCentralValueComparer(SAMPLEA, SAMPLEB)
        self.assertRaises(ValueError,analyzer.leftTailDeltaSignificanceTest, delta=0.3, type1Confidence=None)

    def test_leftTailDeltaSignificanceTest_type1ConfidenceNegative(self):
        """Tests that leftTailDeltaSignificanceTest raises an error when given a negative type1Confidence"""
        analyzer: PairedNormalCentralValueComparer = PairedNormalCentralValueComparer(SAMPLEA, SAMPLEB)
        self.assertRaises(ValueError,analyzer.leftTailDeltaSignificanceTest, delta=0.3, type1Confidence=-1)

    def test_leftTailDeltaSignificanceTest_type1ConfidenceTooLarge(self):
        """Tests that leftTailDeltaSignificanceTest raises an error when given a type1Confidence over 1"""
        analyzer: PairedNormalCentralValueComparer = PairedNormalCentralValueComparer(SAMPLEA, SAMPLEB)
        self.assertRaises(ValueError,analyzer.leftTailDeltaSignificanceTest, delta=0.3, type1Confidence=2)

    def test_leftTailDeltaSignificanceTest_deltaNone(self):
        """Tests that leftTailDeltaSignificanceTest raises an error when given a null delta"""
        analyzer: PairedNormalCentralValueComparer = PairedNormalCentralValueComparer(SAMPLEA, SAMPLEB)
        self.assertRaises(ValueError,analyzer.leftTailDeltaSignificanceTest, delta=None, type1Confidence=0.95)

    def test_twinTailDeltaSignificanceTest_whenCalled(self):
        """Tests the value of twinTailDeltaSignificanceTest when called"""
        comparer: PairedNormalCentralValueComparer = PairedNormalCentralValueComparer(SAMPLEA, SAMPLEB)
        self.assertTrue(comparer.twinTailDeltaSignificanceTest(0, 0.95))

    def test_twinTailDeltaSignificanceTest_type1ConfidenceNone(self):
        """Tests that twinTailDeltaSignificanceTest raises an error when given a null type1Confidence"""
        analyzer: PairedNormalCentralValueComparer = PairedNormalCentralValueComparer(SAMPLEA, SAMPLEB)
        self.assertRaises(ValueError,analyzer.twinTailDeltaSignificanceTest, delta=0.3, type1Confidence=None)

    def test_twinTailDeltaSignificanceTest_type1ConfidenceNegative(self):
        """Tests that twinTailDeltaSignificanceTest raises an error when given a negative type1Confidence"""
        analyzer: PairedNormalCentralValueComparer = PairedNormalCentralValueComparer(SAMPLEA, SAMPLEB)
        self.assertRaises(ValueError,analyzer.twinTailDeltaSignificanceTest, delta=0.3, type1Confidence=-1)

    def test_twinTailDeltaSignificanceTest_type1ConfidenceTooLarge(self):
        """Tests that twinTailDeltaSignificanceTest raises an error when given a type1Confidence over 1"""
        analyzer: PairedNormalCentralValueComparer = PairedNormalCentralValueComparer(SAMPLEA, SAMPLEB)
        self.assertRaises(ValueError,analyzer.twinTailDeltaSignificanceTest, delta=0.3, type1Confidence=2)

    def test_twinTailDeltaSignificanceTest_deltaNone(self):
        """Tests that twinTailDeltaSignificanceTest raises an error when given a null delta"""
        analyzer: PairedNormalCentralValueComparer = PairedNormalCentralValueComparer(SAMPLEA, SAMPLEB)
        self.assertRaises(ValueError,analyzer.twinTailDeltaSignificanceTest, delta=None, type1Confidence=0.95)
