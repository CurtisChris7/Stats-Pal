import unittest
from PopulationVarianceInference.NormalVarianceAnalyzer import NormalVarianceAnalyzer

TEST_VALUES: list = [501.4, 498.0, 498.6, 499.2, 495.2, 501.4, 509.5, 494.9, 498.6, 497.6, 505.5, 505.1, 499.8, 502.4, 497.0, 504.3, 499.7, 497.9, 496.5, 498.9, 504.9, 503.2, 503.0, 502.6, 496.8, 498.2, 500.1, 497.9, 502.2, 503.2]

class NormalVarianceAnalyzerTests(unittest.TestCase):
    """Unit testing class for the NormalVarianceAnalyzer"""
    
    def test_constructor_valuesNone(self):
        """Tests that the constructor raises an error with null values"""
        self.assertRaises(ValueError, NormalVarianceAnalyzer, values=None)

    def test_constructor_valuesEmpty(self):
        """Tests that the constructor raises an error with empty values"""
        self.assertRaises(ValueError, NormalVarianceAnalyzer, values=[])

    def test_constructor_chisquareNone(self):
        """Tests that the constructor raises an error with null chisquare"""
        self.assertRaises(ValueError, NormalVarianceAnalyzer, values = TEST_VALUES, chisquare=None)

    def test_getSampleVariance_whenCalled(self):
        """Tests the value of getSampleVariance when called"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES)
        self.assertAlmostEqual(analyzer.getSampleVariance(), 0.45644444444444443)

    def test_getConfidenceInterval_whenCalled(self):
        """Tests the value of getConfidenceInterval when called with legal arguments"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES)
        interval: tuple = analyzer.getConfidenceInterval(0.95)
        self.assertAlmostEqual(interval[0], 2.6166866407784255)
        self.assertAlmostEqual(interval[1], 2.983313359221574)

    def test_getConfidenceInterval_confidenceLevelNone(self):
        """Tests that getConfidenceInterval raises an error when given a null confidence level"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.getConfidenceInterval, None)

    def test_getConfidenceInterval_confidenceLevelNegative(self):
        """Tests that getConfidenceInterval raises an error when given a negative confidence level"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.getConfidenceInterval, -1)

    def test_getConfidenceInterval_confidenceLevelTooLarge(self):
        """Tests that getConfidenceInterval raises an error when given a confidence level that is over 1"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.getConfidenceInterval, 2)

    def test_sampleSizeForConfidenceInterval_whenCalled(self):
        """Tests the value of sampleSizeForConfidenceInterval when called with legal arguments"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer([2.7, 2.4, 1.9, 2.6, 2.4, 1.9, 2.3, 2.2, 2.5, 2.3, 1.8, 2.5, 2.0, 2.2])
        self.assertIsNone(analyzer.sampleSizeForConfidenceInterval(0.95, 0.6))

    def test_sampleSizeForTesting_whenCalled(self):
        """Tests the value of getTestStatistic when called with legal arguments"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES)
        self.assertAlmostEqual(analyzer.sampleSizeForTesting(type1Confidence=0.95, type2Confidence=0.75, delta=0.3), None)

    def test_getTestStatistic_whenCalled(self):
        """Tests the value of getTestStatistic when called with legal arguments"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES)
        self.assertAlmostEqual(analyzer.getTestStatistic(0.3), 2.2050588385131595)

    def test_getTestStatistic_meanNull(self):
        """Tests that getConfidenceInterval raises an error when given a null mean"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.getTestStatistic, None)

    def test_rightTailVarianceSignificanceTest_whenCalled(self):
        """Tests the value of rightTailVarianceSignificanceTest when called with legal arguments"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES)
        self.assertTrue(analyzer.rightTailVarianceSignificanceTest(0.3, 0.96))
        self.assertFalse(analyzer.rightTailVarianceSignificanceTest(0.3, 0.99))

    def test_rightTailVarianceSignificanceTest_type1ConfidenceNone(self):
        """Tests that rightTailVarianceSignificanceTest raises an error when given a null type1Confidence"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.rightTailVarianceSignificanceTest, mean=0.3, type1Confidence=None)

    def test_rightTailVarianceSignificanceTest_type1ConfidenceNegative(self):
        """Tests that rightTailVarianceSignificanceTest raises an error when given a negative type1Confidence"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.rightTailVarianceSignificanceTest, mean=0.3, type1Confidence=-1)

    def test_rightTailVarianceSignificanceTest_type1ConfidenceTooLarge(self):
        """Tests that rightTailVarianceSignificanceTest raises an error when given a type1Confidence over 1"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.rightTailVarianceSignificanceTest, mean=0.3, type1Confidence=2)

    def test_rightTailVarianceSignificanceTest_meanNone(self):
        """Tests that rightTailVarianceSignificanceTest raises an error when given a null mean"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.rightTailVarianceSignificanceTest, mean=None, type1Confidence=0.95)

    def test_leftTailVarianceSignificanceTest_whenCalled(self):
        """Tests the value of leftTailVarianceSignificanceTest when called with legal arguments"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES)
        self.assertTrue(analyzer.leftTailVarianceSignificanceTest(1, 0.95))
        self.assertFalse(analyzer.leftTailVarianceSignificanceTest(0.3, 0.99))

    def test_leftTailVarianceSignificanceTest_type1ConfidenceNone(self):
        """Tests that leftTailVarianceSignificanceTest raises an error when given a null type1Confidence"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.leftTailVarianceSignificanceTest, mean=0.3, type1Confidence=None)

    def test_leftTailVarianceSignificanceTest_type1ConfidenceNegative(self):
        """Tests that leftTailVarianceSignificanceTest raises an error when given a negative type1Confidence"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.leftTailVarianceSignificanceTest, mean=0.3, type1Confidence=-1)

    def test_leftTailVarianceSignificanceTest_type1ConfidenceTooLarge(self):
        """Tests that leftTailVarianceSignificanceTest raises an error when given a type1Confidence over 1"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.leftTailVarianceSignificanceTest, mean=0.3, type1Confidence=2)

    def test_leftTailVarianceSignificanceTest_meanNone(self):
        """Tests that leftTailVarianceSignificanceTest raises an error when given a null mean"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.leftTailVarianceSignificanceTest, mean=None, type1Confidence=0.95)

    def test_twinTailVarianceSignificanceTest_whenCalled(self):
        """Tests the value of twinTailVarianceSignificanceTest when called with legal arguments"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES)
        self.assertTrue(analyzer.twinTailVarianceSignificanceTest(0.2, 0.95))
        self.assertFalse(analyzer.twinTailVarianceSignificanceTest(0.3, 0.99))

    def test_twinTailVarianceSignificanceTest_type1ConfidenceNone(self):
        """Tests that leftTailMeanSignificanceTest raises an error when given a null type1Confidence"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.twinTailVarianceSignificanceTest, mean=0.3, type1Confidence=None)

    def test_twinTailVarianceSignificanceTest_type1ConfidenceNegative(self):
        """Tests that leftTailMeanSignificanceTest raises an error when given a negative type1Confidence"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.twinTailVarianceSignificanceTest, mean=0.3, type1Confidence=-1)

    def test_twinTailVarianceSignificanceTest_type1ConfidenceTooLarge(self):
        """Tests that leftTailMeanSignificanceTest raises an error when given a type1Confidence over 1"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.twinTailVarianceSignificanceTest, mean=0.3, type1Confidence=2)

    def test_twinTailVarianceSignificanceTest_meanNone(self):
        """Tests that leftTailMeanSignificanceTest raises an error when given a null mean"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.twinTailVarianceSignificanceTest, mean=None, type1Confidence=0.95)
