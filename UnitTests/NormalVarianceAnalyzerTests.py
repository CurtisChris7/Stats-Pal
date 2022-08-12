import unittest
from PopulationVarianceInference.NormalVarianceAnalyzer import NormalVarianceAnalyzer

TEST_VALUES_A: list = [501.4, 498.0, 498.6, 499.2, 495.2, 501.4, 509.5, 494.9, 498.6, 497.6, 505.5, 505.1, 499.8, 502.4, 497.0, 504.3, 499.7, 497.9, 496.5, 498.9, 504.9, 503.2, 503.0, 502.6, 496.8, 498.2, 500.1, 497.9, 502.2, 503.2]
TEST_VALUES_B: list = [203.1, 184.5, 206.8, 211.0, 218.3, 174.2, 193.2, 201.9, 199.9, 194.3, 199.4, 193.6, 194.6, 187.2, 197.8, 184.3, 196.1, 196.4, 197.5, 187.9]

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
        self.assertRaises(ValueError, NormalVarianceAnalyzer, values = TEST_VALUES_A, chisquare=None)

    def test_getSampleVariance_whenCalled(self):
        """Tests the value of getSampleVariance when called"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES_A)
        self.assertAlmostEqual(analyzer.getSampleVariance(), 11.788781609195413)

    def test_getConfidenceInterval_whenCalled(self):
        """Tests the value of getConfidenceInterval when called with legal arguments"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES_A)
        interval: tuple = analyzer.getConfidenceInterval(0.99)
        self.assertAlmostEqual(interval[0], 2.555846590214804)
        self.assertAlmostEqual(interval[1], 5.104433242623351)

    def test_getConfidenceInterval_confidenceLevelNone(self):
        """Tests that getConfidenceInterval raises an error when given a null confidence level"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES_A)
        self.assertRaises(ValueError, analyzer.getConfidenceInterval, None)

    def test_getConfidenceInterval_confidenceLevelNegative(self):
        """Tests that getConfidenceInterval raises an error when given a negative confidence level"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES_A)
        self.assertRaises(ValueError, analyzer.getConfidenceInterval, -1)

    def test_getConfidenceInterval_confidenceLevelTooLarge(self):
        """Tests that getConfidenceInterval raises an error when given a confidence level that is over 1"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES_A)
        self.assertRaises(ValueError, analyzer.getConfidenceInterval, 2)

    def test_getTestStatistic_whenCalled(self):
        """Tests the value of getTestStatistic when called with legal arguments"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES_B)
        self.assertAlmostEqual(analyzer.getTestStatistic(25), 74.49040000000005)

    def test_getTestStatistic_meanNull(self):
        """Tests that getConfidenceInterval raises an error when given a null mean"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES_A)
        self.assertRaises(ValueError, analyzer.getTestStatistic, None)

    def test_getTestStatistic_meanZero(self):
        """Tests that getConfidenceInterval raises an error when given a zerp mean"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES_A)
        self.assertRaises(ValueError, analyzer.getTestStatistic, 0)

    def test_rightTailVarianceSignificanceTest_whenCalled(self):
        """Tests the value of rightTailVarianceSignificanceTest when called with legal arguments"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES_B)
        self.assertTrue(analyzer.rightTailVarianceSignificanceTest(25, 0.95))
        self.assertFalse(analyzer.rightTailVarianceSignificanceTest(120, 0.95))

    def test_rightTailVarianceSignificanceTest_type1ConfidenceNone(self):
        """Tests that rightTailVarianceSignificanceTest raises an error when given a null type1Confidence"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES_B)
        self.assertRaises(ValueError,analyzer.rightTailVarianceSignificanceTest, variance=0.3, type1Confidence=None)

    def test_rightTailVarianceSignificanceTest_type1ConfidenceNegative(self):
        """Tests that rightTailVarianceSignificanceTest raises an error when given a negative type1Confidence"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES_B)
        self.assertRaises(ValueError,analyzer.rightTailVarianceSignificanceTest, variance=0.3, type1Confidence=-1)

    def test_rightTailVarianceSignificanceTest_type1ConfidenceTooLarge(self):
        """Tests that rightTailVarianceSignificanceTest raises an error when given a type1Confidence over 1"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES_B)
        self.assertRaises(ValueError,analyzer.rightTailVarianceSignificanceTest, variance=0.3, type1Confidence=2)

    def test_rightTailVarianceSignificanceTest_varianceNone(self):
        """Tests that rightTailVarianceSignificanceTest raises an error when given a null variance"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES_B)
        self.assertRaises(ValueError,analyzer.rightTailVarianceSignificanceTest, variance=None, type1Confidence=0.95)

    def test_leftTailVarianceSignificanceTest_whenCalled(self):
        """Tests the value of leftTailVarianceSignificanceTest when called with legal arguments"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES_B)
        self.assertTrue(analyzer.leftTailVarianceSignificanceTest(250, 0.95))
        self.assertFalse(analyzer.leftTailVarianceSignificanceTest(70, 0.95))

    def test_leftTailVarianceSignificanceTest_type1ConfidenceNone(self):
        """Tests that leftTailVarianceSignificanceTest raises an error when given a null type1Confidence"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES_B)
        self.assertRaises(ValueError,analyzer.leftTailVarianceSignificanceTest, variance=0.3, type1Confidence=None)

    def test_leftTailVarianceSignificanceTest_type1ConfidenceNegative(self):
        """Tests that leftTailVarianceSignificanceTest raises an error when given a negative type1Confidence"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES_B)
        self.assertRaises(ValueError,analyzer.leftTailVarianceSignificanceTest, variance=0.3, type1Confidence=-1)

    def test_leftTailVarianceSignificanceTest_type1ConfidenceTooLarge(self):
        """Tests that leftTailVarianceSignificanceTest raises an error when given a type1Confidence over 1"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES_B)
        self.assertRaises(ValueError,analyzer.leftTailVarianceSignificanceTest, variance=0.3, type1Confidence=2)

    def test_leftTailVarianceSignificanceTest_varianceNone(self):
        """Tests that leftTailVarianceSignificanceTest raises an error when given a null variance"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES_B)
        self.assertRaises(ValueError,analyzer.leftTailVarianceSignificanceTest, variance=None, type1Confidence=0.95)

    def test_twinTailVarianceSignificanceTest_whenCalled(self):
        """Tests the value of twinTailVarianceSignificanceTest when called with legal arguments"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES_B)
        self.assertFalse(analyzer.twinTailVarianceSignificanceTest(100, 0.95))
        self.assertTrue(analyzer.twinTailVarianceSignificanceTest(50, 0.95))
        self.assertTrue(analyzer.twinTailVarianceSignificanceTest(250, 0.95))
        
    def test_twinTailVarianceSignificanceTest_type1ConfidenceNone(self):
        """Tests that leftTailvarianceSignificanceTest raises an error when given a null type1Confidence"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES_B)
        self.assertRaises(ValueError,analyzer.twinTailVarianceSignificanceTest, variance=0.3, type1Confidence=None)

    def test_twinTailVarianceSignificanceTest_type1ConfidenceNegative(self):
        """Tests that leftTailvarianceSignificanceTest raises an error when given a negative type1Confidence"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES_B)
        self.assertRaises(ValueError,analyzer.twinTailVarianceSignificanceTest, variance=0.3, type1Confidence=-1)

    def test_twinTailVarianceSignificanceTest_type1ConfidenceTooLarge(self):
        """Tests that leftTailvarianceSignificanceTest raises an error when given a type1Confidence over 1"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES_B)
        self.assertRaises(ValueError,analyzer.twinTailVarianceSignificanceTest, variance=0.3, type1Confidence=2)

    def test_twinTailVarianceSignificanceTest_varianceNone(self):
        """Tests that leftTailvarianceSignificanceTest raises an error when given a null variance"""
        analyzer: NormalVarianceAnalyzer = NormalVarianceAnalyzer(TEST_VALUES_B)
        self.assertRaises(ValueError,analyzer.twinTailVarianceSignificanceTest, variance=None, type1Confidence=0.95)
