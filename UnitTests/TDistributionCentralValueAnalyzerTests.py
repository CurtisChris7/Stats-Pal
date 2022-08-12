import unittest
from PopulationCentralValueInference.TDistributionCentralValueAnalyzer import TDistributionCentralValueAnalyzer

TEST_VALUES: list = [0.593, 0.142 ,0.329 ,0.691 ,0.231, 0.793, 0.519, 0.392, 0.418]

class TDistributionCentralValueAnalyzerTests(unittest.TestCase):
    """Unit testing class for the TDistributionCentralValueAnalyzer"""
    
    def test_constructor_valuesNone(self):
        """Tests that the constructor raises an error with null values"""
        self.assertRaises(ValueError, TDistributionCentralValueAnalyzer, values=None)

    def test_constructor_valuesEmpty(self):
        """Tests that the constructor raises an error with empty values"""
        self.assertRaises(ValueError, TDistributionCentralValueAnalyzer, values=[])

    def test_constructor_tDistNone(self):
        """Tests that the constructor raises an error with null tDist"""
        self.assertRaises(ValueError, TDistributionCentralValueAnalyzer, values = TEST_VALUES, tDist=None)

    def test_getMean_whenCalled(self):
        """Tests the value of getMean when called"""
        analyzer: TDistributionCentralValueAnalyzer = TDistributionCentralValueAnalyzer(TEST_VALUES)
        self.assertAlmostEqual(analyzer.getMean(), 0.45644444444444443)

    def test_getConfidenceInterval_whenCalled(self):
        """Tests the value of getConfidenceInterval when called with legal arguments"""
        analyzer: TDistributionCentralValueAnalyzer = TDistributionCentralValueAnalyzer([2.7, 2.4, 1.9, 2.6, 2.4, 1.9, 2.3, 2.2, 2.5, 2.3, 1.8, 2.5, 2.0, 2.2])
        analyzer.n = 50
        analyzer.mean = 2.8
        analyzer.stdDev = 0.6
        interval: tuple = analyzer.getConfidenceInterval(0.95)
        self.assertAlmostEqual(interval[0], 2.6166866407784255)
        self.assertAlmostEqual(interval[1], 2.983313359221574)

    def test_getConfidenceInterval_confidenceLevelNone(self):
        """Tests that getConfidenceInterval raises an error when given a null confidence level"""
        analyzer: TDistributionCentralValueAnalyzer = TDistributionCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.getConfidenceInterval, None)

    def test_getConfidenceInterval_confidenceLevelNegative(self):
        """Tests that getConfidenceInterval raises an error when given a negative confidence level"""
        analyzer: TDistributionCentralValueAnalyzer = TDistributionCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.getConfidenceInterval, -1)

    def test_getConfidenceInterval_confidenceLevelTooLarge(self):
        """Tests that getConfidenceInterval raises an error when given a confidence level that is over 1"""
        analyzer: TDistributionCentralValueAnalyzer = TDistributionCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.getConfidenceInterval, 2)

    def test_sampleSizeForConfidenceInterval_whenCalled(self):
        """Tests the value of sampleSizeForConfidenceInterval when called with legal arguments"""
        analyzer: TDistributionCentralValueAnalyzer = TDistributionCentralValueAnalyzer([2.7, 2.4, 1.9, 2.6, 2.4, 1.9, 2.3, 2.2, 2.5, 2.3, 1.8, 2.5, 2.0, 2.2])
        self.assertIsNone(analyzer.sampleSizeForConfidenceInterval(0.95, 0.6))

    def test_sampleSizeForTesting_whenCalled(self):
        """Tests the value of getTestStatistic when called with legal arguments"""
        analyzer: TDistributionCentralValueAnalyzer = TDistributionCentralValueAnalyzer(TEST_VALUES)
        self.assertAlmostEqual(analyzer.sampleSizeForTesting(type1Confidence=0.95, type2Confidence=0.75, delta=0.3), None)

    def test_getTestStatistic_whenCalled(self):
        """Tests the value of getTestStatistic when called with legal arguments"""
        analyzer: TDistributionCentralValueAnalyzer = TDistributionCentralValueAnalyzer(TEST_VALUES)
        self.assertAlmostEqual(analyzer.getTestStatistic(0.3), 2.2050588385131595)

    def test_getTestStatistic_meanNull(self):
        """Tests that getConfidenceInterval raises an error when given a null mean"""
        analyzer: TDistributionCentralValueAnalyzer = TDistributionCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.getTestStatistic, None)

    def test_rightTailMeanSignificanceTest_whenCalled(self):
        """Tests the value of rightTailMeanSignificanceTest when called with legal arguments"""
        analyzer: TDistributionCentralValueAnalyzer = TDistributionCentralValueAnalyzer(TEST_VALUES)
        self.assertTrue(analyzer.rightTailMeanSignificanceTest(0.3, 0.96))
        self.assertFalse(analyzer.rightTailMeanSignificanceTest(0.3, 0.99))

    def test_rightTailMeanSignificanceTest_type1ConfidenceNone(self):
        """Tests that rightTailMeanSignificanceTest raises an error when given a null type1Confidence"""
        analyzer: TDistributionCentralValueAnalyzer = TDistributionCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.rightTailMeanSignificanceTest, mean=0.3, type1Confidence=None)

    def test_rightTailMeanSignificanceTest_type1ConfidenceNegative(self):
        """Tests that rightTailMeanSignificanceTest raises an error when given a negative type1Confidence"""
        analyzer: TDistributionCentralValueAnalyzer = TDistributionCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.rightTailMeanSignificanceTest, mean=0.3, type1Confidence=-1)

    def test_rightTailMeanSignificanceTest_type1ConfidenceTooLarge(self):
        """Tests that rightTailMeanSignificanceTest raises an error when given a type1Confidence over 1"""
        analyzer: TDistributionCentralValueAnalyzer = TDistributionCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.rightTailMeanSignificanceTest, mean=0.3, type1Confidence=2)

    def test_rightTailMeanSignificanceTest_meanNone(self):
        """Tests that rightTailMeanSignificanceTest raises an error when given a null mean"""
        analyzer: TDistributionCentralValueAnalyzer = TDistributionCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.rightTailMeanSignificanceTest, mean=None, type1Confidence=0.95)

    def test_leftTailMeanSignificanceTest_whenCalled(self):
        """Tests the value of leftTailMeanSignificanceTest when called with legal arguments"""
        analyzer: TDistributionCentralValueAnalyzer = TDistributionCentralValueAnalyzer(TEST_VALUES)
        self.assertTrue(analyzer.leftTailMeanSignificanceTest(1, 0.95))
        self.assertFalse(analyzer.leftTailMeanSignificanceTest(0.3, 0.99))

    def test_leftTailMeanSignificanceTest_type1ConfidenceNone(self):
        """Tests that leftTailMeanSignificanceTest raises an error when given a null type1Confidence"""
        analyzer: TDistributionCentralValueAnalyzer = TDistributionCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.leftTailMeanSignificanceTest, mean=0.3, type1Confidence=None)

    def test_leftTailMeanSignificanceTest_type1ConfidenceNegative(self):
        """Tests that leftTailMeanSignificanceTest raises an error when given a negative type1Confidence"""
        analyzer: TDistributionCentralValueAnalyzer = TDistributionCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.leftTailMeanSignificanceTest, mean=0.3, type1Confidence=-1)

    def test_leftTailMeanSignificanceTest_type1ConfidenceTooLarge(self):
        """Tests that leftTailMeanSignificanceTest raises an error when given a type1Confidence over 1"""
        analyzer: TDistributionCentralValueAnalyzer = TDistributionCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.leftTailMeanSignificanceTest, mean=0.3, type1Confidence=2)

    def test_leftTailMeanSignificanceTest_meanNone(self):
        """Tests that leftTailMeanSignificanceTest raises an error when given a null mean"""
        analyzer: TDistributionCentralValueAnalyzer = TDistributionCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.leftTailMeanSignificanceTest, mean=None, type1Confidence=0.95)

    def test_twinTailMeanSignificanceTest_whenCalled(self):
        """Tests the value of twinTailMeanSignificanceTest when called with legal arguments"""
        analyzer: TDistributionCentralValueAnalyzer = TDistributionCentralValueAnalyzer(TEST_VALUES)
        self.assertTrue(analyzer.twinTailMeanSignificanceTest(0.2, 0.95))
        self.assertFalse(analyzer.twinTailMeanSignificanceTest(0.3, 0.99))

    def test_twinTailMeanSignificanceTest_type1ConfidenceNone(self):
        """Tests that leftTailMeanSignificanceTest raises an error when given a null type1Confidence"""
        analyzer: TDistributionCentralValueAnalyzer = TDistributionCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.twinTailMeanSignificanceTest, mean=0.3, type1Confidence=None)

    def test_twinTailMeanSignificanceTest_type1ConfidenceNegative(self):
        """Tests that leftTailMeanSignificanceTest raises an error when given a negative type1Confidence"""
        analyzer: TDistributionCentralValueAnalyzer = TDistributionCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.twinTailMeanSignificanceTest, mean=0.3, type1Confidence=-1)

    def test_twinTailMeanSignificanceTest_type1ConfidenceTooLarge(self):
        """Tests that leftTailMeanSignificanceTest raises an error when given a type1Confidence over 1"""
        analyzer: TDistributionCentralValueAnalyzer = TDistributionCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.twinTailMeanSignificanceTest, mean=0.3, type1Confidence=2)

    def test_twinTailMeanSignificanceTest_meanNone(self):
        """Tests that leftTailMeanSignificanceTest raises an error when given a null mean"""
        analyzer: TDistributionCentralValueAnalyzer = TDistributionCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.twinTailMeanSignificanceTest, mean=None, type1Confidence=0.95)
