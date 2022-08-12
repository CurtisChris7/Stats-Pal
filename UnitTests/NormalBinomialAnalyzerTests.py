import unittest
from CategoricalPopulationInference.NormalBinomialAnalyzer import NormalBinomialAnalyzer
from UnitTests.NormalCentralValueAnalyzerTests import TEST_VALUES

TEST_VALUES = [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

class NormalBinomialAnalyzerTests(unittest.TestCase):
    """Unit testing class for the NormalBinomialAnalyzer"""

    def test_constructor_valuesNone(self):
        """Tests that the constructor raises an error with null values"""
        self.assertRaises(ValueError, NormalBinomialAnalyzer, values=None)

    def test_constructor_valuesEmpty(self):
        """Tests that the constructor raises an error with empty values"""
        self.assertRaises(ValueError, NormalBinomialAnalyzer, values=[])

    def test_constructor_normalDistNone(self):
        """Tests that the constructor raises an error with null values"""
        self.assertRaises(ValueError, NormalBinomialAnalyzer, values=TEST_VALUES, normalDist=None)

    def test_constructor_biomnialDist(self):
        """Tests that the constructor raises an error with null values"""
        self.assertRaises(ValueError, NormalBinomialAnalyzer, values=TEST_VALUES, binomialDist=None)

    def test_getSampleLikelihood_whenCalled(self):
        """Tests the valye of getSampleLikelihood when called"""
        analyzer: NormalBinomialAnalyzer = NormalBinomialAnalyzer(TEST_VALUES)
        self.assertAlmostEqual(analyzer.getSampleLikelihood(), 4/15)

    def test_getSampleStandardError_whenCalled(self):
        """Tests the valye of getSampleStandardError when called"""
        analyzer: NormalBinomialAnalyzer = NormalBinomialAnalyzer(TEST_VALUES)
        self.assertAlmostEqual(analyzer.getSampleStandardError(), 0.11417984514369003)

    def test_getConfidenceInterval_whenCalled(self):
        """Tests the value of getConfidenceInterval when called with legal arguments"""
        analyzer: NormalBinomialAnalyzer = NormalBinomialAnalyzer(TEST_VALUES)
        interval: tuple = analyzer.getConfidenceInterval(0.95)
        self.assertAlmostEqual(interval[0], 0.10462971795951073)
        self.assertAlmostEqual(interval[1], 0.523851939649185)

    def test_getConfidenceInterval_likelihoodZero(self):
        """Tests the value of getConfidenceInterval when called with legal arguments"""
        analyzer: NormalBinomialAnalyzer = NormalBinomialAnalyzer([0, 0, 0, 0, 0])
        interval: tuple = analyzer.getConfidenceInterval(0.95)
        self.assertAlmostEqual(interval[0], 0)
        self.assertAlmostEqual(interval[1], 0.5837233962990633)

    def test_getConfidenceInterval_likelihoodOne(self):
        """Tests the value of getConfidenceInterval when called with legal arguments"""
        analyzer: NormalBinomialAnalyzer = NormalBinomialAnalyzer([1, 1, 1, 1, 1])
        interval: tuple = analyzer.getConfidenceInterval(0.95)
        self.assertAlmostEqual(interval[0], 0.4162766037009366)
        self.assertAlmostEqual(interval[1], 1)

    def test_getConfidenceInterval_confidenceLevelNone(self):
        """Tests that getConfidenceInterval raises an error when given a null confidence level"""
        analyzer: NormalBinomialAnalyzer = NormalBinomialAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.getConfidenceInterval, None)

    def test_getConfidenceInterval_confidenceLevelNegative(self):
        """Tests that getConfidenceInterval raises an error when given a negative confidence level"""
        analyzer: NormalBinomialAnalyzer = NormalBinomialAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.getConfidenceInterval, -1)

    def test_getConfidenceInterval_confidenceLevelTooLarge(self):
        """Tests that getConfidenceInterval raises an error when given a confidence level that is over 1"""
        analyzer: NormalBinomialAnalyzer = NormalBinomialAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.getConfidenceInterval, 2)

    def test_sampleSizeForConfidenceInterval_whenCalled(self):
        """Tests the valye of sampleSizeForConfidenceInterval when called"""
        analyzer: NormalBinomialAnalyzer = NormalBinomialAnalyzer(TEST_VALUES)
        self.assertAlmostEqual(analyzer.sampleSizeForConfidenceInterval(0.95, 0.05), 300.49848888888886)

    def test_sampleSizeForConfidenceInterval_confidenceLevelNone(self):
        """Tests that sampleSizeForConfidenceInterval raises an error when given a null confidence level"""
        analyzer: NormalBinomialAnalyzer = NormalBinomialAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.sampleSizeForConfidenceInterval, None, 0.3)

    def test_sampleSizeForConfidenceInterval_confidenceLevelNegative(self):
        """Tests that sampleSizeForConfidenceInterval raises an error when given a negative confidence level"""
        analyzer: NormalBinomialAnalyzer = NormalBinomialAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.sampleSizeForConfidenceInterval, -1, 0.3)

    def test_sampleSizeForConfidenceInterval_confidenceLevelTooLarge(self):
        """Tests that sampleSizeForConfidenceInterval raises an error when given a confidence level that is over 1"""
        analyzer: NormalBinomialAnalyzer = NormalBinomialAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.sampleSizeForConfidenceInterval, 2, 0.3)

    def test_sampleSizeForConfidenceInterval_widthNone(self):
        """Tests that sampleSizeForConfidenceInterval raises an error when given a null confidence level"""
        analyzer: NormalBinomialAnalyzer = NormalBinomialAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.sampleSizeForConfidenceInterval, 0.95, None)

    def test_sampleSizeForConfidenceInterval_widthNegative(self):
        """Tests that sampleSizeForConfidenceInterval raises an error when given a negative confidence level"""
        analyzer: NormalBinomialAnalyzer = NormalBinomialAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.sampleSizeForConfidenceInterval, 0.95, -1)

    def test_getTestStatistic_whenCalled(self):
        """Tests the value of getTestStatistic when called with legal arguments"""
        analyzer: NormalBinomialAnalyzer = NormalBinomialAnalyzer(TEST_VALUES)
        self.assertAlmostEqual(analyzer.getTestStatistic(0.3), -0.29193710406057105)

    def test_getTestStatistic_likelihoodNull(self):
        """Tests that getConfidenceInterval raises an error when given a null likelihood"""
        analyzer: NormalBinomialAnalyzer = NormalBinomialAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.getTestStatistic, None)

    def test_getTestStatistic_likelihoodnegative(self):
        """Tests that getConfidenceInterval raises an error when given a negative likelihood"""
        analyzer: NormalBinomialAnalyzer = NormalBinomialAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.getTestStatistic, -1)

    def test_getTestStatistic_likelihoodTooLarge(self):
        """Tests that getConfidenceInterval raises an error when given a likelihood over one"""
        analyzer: NormalBinomialAnalyzer = NormalBinomialAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.getTestStatistic, 2)

    def test_rightTailtLikelihoodSignificanceTest_whenCalled(self):
        """Tests the value of rightTailtLikelihoodSignificanceTest when called with legal arguments"""
        analyzer: NormalBinomialAnalyzer = NormalBinomialAnalyzer(TEST_VALUES)
        self.assertFalse(analyzer.rightTailtLikelihoodSignificanceTest(0.20, 0.95))

    def test_rightTailtLikelihoodSignificanceTest_likelihoodNone(self):
        """Tests that rightTailtLikelihoodSignificanceTest raises an error when given a null confidence level"""
        analyzer: NormalBinomialAnalyzer = NormalBinomialAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.rightTailtLikelihoodSignificanceTest, None, 0.95)

    def test_rightTailtLikelihoodSignificanceTest_likelihoodNegative(self):
        """Tests that rightTailtLikelihoodSignificanceTest raises an error when given a negative confidence level"""
        analyzer: NormalBinomialAnalyzer = NormalBinomialAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.rightTailtLikelihoodSignificanceTest, -1, 0.95)

    def test_rightTailtLikelihoodSignificanceTest_likelihoodTooLarge(self):
        """Tests that rightTailtLikelihoodSignificanceTest raises an error when given a confidence level that is over 1"""
        analyzer: NormalBinomialAnalyzer = NormalBinomialAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.rightTailtLikelihoodSignificanceTest, 2, 0.95)

    def test_rightTailtLikelihoodSignificanceTest_confidenceLevelNone(self):
        """Tests that rightTailtLikelihoodSignificanceTest raises an error when given a null confidence level"""
        analyzer: NormalBinomialAnalyzer = NormalBinomialAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.rightTailtLikelihoodSignificanceTest, None, 0.3)

    def test_rightTailtLikelihoodSignificanceTest_confidenceLevelNegative(self):
        """Tests that rightTailtLikelihoodSignificanceTest raises an error when given a negative confidence level"""
        analyzer: NormalBinomialAnalyzer = NormalBinomialAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.rightTailtLikelihoodSignificanceTest, -1, 0.3)

    def test_rightTailtLikelihoodSignificanceTest_confidenceLevelTooLarge(self):
        """Tests that rightTailtLikelihoodSignificanceTest raises an error when given a confidence level that is over 1"""
        analyzer: NormalBinomialAnalyzer = NormalBinomialAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.rightTailtLikelihoodSignificanceTest, 2, 0.3)

    def test_rightTailtLikelihoodSignificanceTest_whenCalled(self):
        """Tests the value of rightTailtLikelihoodSignificanceTest when called with legal arguments"""
        analyzer: NormalBinomialAnalyzer = NormalBinomialAnalyzer(TEST_VALUES)
        self.assertFalse(analyzer.rightTailtLikelihoodSignificanceTest(0.20, 0.95))

    def test_leftTailLikelihoodSignificanceTest_likelihoodNone(self):
        """Tests that leftTailLikelihoodSignificanceTest raises an error when given a null confidence level"""
        analyzer: NormalBinomialAnalyzer = NormalBinomialAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.leftTailLikelihoodSignificanceTest, None, 0.95)

    def test_leftTailLikelihoodSignificanceTest_likelihoodNegative(self):
        """Tests that leftTailLikelihoodSignificanceTest raises an error when given a negative confidence level"""
        analyzer: NormalBinomialAnalyzer = NormalBinomialAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.leftTailLikelihoodSignificanceTest, -1, 0.95)

    def test_leftTailLikelihoodSignificanceTest_likelihoodTooLarge(self):
        """Tests that leftTailLikelihoodSignificanceTest raises an error when given a confidence level that is over 1"""
        analyzer: NormalBinomialAnalyzer = NormalBinomialAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.leftTailLikelihoodSignificanceTest, 2, 0.95)

    def test_leftTailLikelihoodSignificanceTest_confidenceLevelNone(self):
        """Tests that leftTailLikelihoodSignificanceTest raises an error when given a null confidence level"""
        analyzer: NormalBinomialAnalyzer = NormalBinomialAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.leftTailLikelihoodSignificanceTest, None, 0.3)

    def test_leftTailLikelihoodSignificanceTest_confidenceLevelNegative(self):
        """Tests that leftTailLikelihoodSignificanceTest raises an error when given a negative confidence level"""
        analyzer: NormalBinomialAnalyzer = NormalBinomialAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.leftTailLikelihoodSignificanceTest, -1, 0.3)

    def test_leftTailLikelihoodSignificanceTest_confidenceLevelTooLarge(self):
        """Tests that leftTailLikelihoodSignificanceTest raises an error when given a confidence level that is over 1"""
        analyzer: NormalBinomialAnalyzer = NormalBinomialAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.leftTailLikelihoodSignificanceTest, 2, 0.3)

    def test_twinTailLikelihoodSignificanceTest_likelihoodNone(self):
        """Tests that twinTailLikelihoodSignificanceTest raises an error when given a null confidence level"""
        analyzer: NormalBinomialAnalyzer = NormalBinomialAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.twinTailLikelihoodSignificanceTest, None, 0.95)

    def test_twinTailLikelihoodSignificanceTest_likelihoodNegative(self):
        """Tests that twinTailLikelihoodSignificanceTest raises an error when given a negative confidence level"""
        analyzer: NormalBinomialAnalyzer = NormalBinomialAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.twinTailLikelihoodSignificanceTest, -1, 0.95)

    def test_twinTailLikelihoodSignificanceTest_likelihoodTooLarge(self):
        """Tests that twinTailLikelihoodSignificanceTest raises an error when given a confidence level that is over 1"""
        analyzer: NormalBinomialAnalyzer = NormalBinomialAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.twinTailLikelihoodSignificanceTest, 2, 0.95)

    def test_twinTailLikelihoodSignificanceTest_confidenceLevelNone(self):
        """Tests that twinTailLikelihoodSignificanceTest raises an error when given a null confidence level"""
        analyzer: NormalBinomialAnalyzer = NormalBinomialAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.twinTailLikelihoodSignificanceTest, None, 0.3)

    def test_twinTailLikelihoodSignificanceTest_confidenceLevelNegative(self):
        """Tests that twinTailLikelihoodSignificanceTest raises an error when given a negative confidence level"""
        analyzer: NormalBinomialAnalyzer = NormalBinomialAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.twinTailLikelihoodSignificanceTest, -1, 0.3)

    def test_twinTailLikelihoodSignificanceTest_confidenceLevelTooLarge(self):
        """Tests that twinTailLikelihoodSignificanceTest raises an error when given a confidence level that is over 1"""
        analyzer: NormalBinomialAnalyzer = NormalBinomialAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.twinTailLikelihoodSignificanceTest, 2, 0.3)
