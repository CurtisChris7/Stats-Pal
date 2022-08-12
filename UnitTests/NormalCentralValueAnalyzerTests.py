import random
import unittest
from PopulationCentralValueInference.NormalCentralValueAnalyzer import NormalCentralValueAnalyzer

TEST_VALUES: list = [0.593, 0.142 ,0.329 ,0.691 ,0.231, 0.793, 0.519, 0.392, 0.418]

class NormalCentralValueAnalyzerTests(unittest.TestCase):
    """Unit testing class for the NormalCentralValueAnalyzer"""
    
    def test_constructor_valuesNone(self):
        """Tests that the constructor raises an error with null values"""
        self.assertRaises(ValueError, NormalCentralValueAnalyzer, values=None)

    def test_constructor_valuesEmpty(self):
        """Tests that the constructor raises an error with empty values"""
        self.assertRaises(ValueError, NormalCentralValueAnalyzer, values=[])

    def test_constructor_normalDistNone(self):
        """Tests that the constructor raises an error with null normalDist"""
        self.assertRaises(ValueError, NormalCentralValueAnalyzer, values = TEST_VALUES, normalDist=None)

    def test_getMean_whenCalled(self):
        """Tests the value of getMean when called"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertAlmostEqual(analyzer.getMean(), 0.45644444444444443)

    def test_getConfidenceInterval_whenCalled(self):
        """Tests the value of getConfidenceInterval when called with legal arguments"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer([2.7, 2.4, 1.9, 2.6, 2.4, 1.9, 2.3, 2.2, 2.5, 2.3, 1.8, 2.5, 2.0, 2.2])
        analyzer.n = 50
        analyzer.mean = 2.8
        analyzer.stdDev = 0.6
        interval: tuple = analyzer.getConfidenceInterval(0.95)
        self.assertAlmostEqual(interval[0], 2.633688485064924)
        self.assertAlmostEqual(interval[1], 2.9663115149350756)

    def test_getConfidenceInterval_confidenceLevelNone(self):
        """Tests that getConfidenceInterval raises an error when given a null confidence level"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.getConfidenceInterval, None)

    def test_getConfidenceInterval_confidenceLevelNegative(self):
        """Tests that getConfidenceInterval raises an error when given a negative confidence level"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.getConfidenceInterval, -1)

    def test_getConfidenceInterval_confidenceLevelTooLarge(self):
        """Tests that getConfidenceInterval raises an error when given a confidence level that is over 1"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.getConfidenceInterval, 2)

    def test_sampleSizeForConfidenceInterval_whenCalled(self):
        """Tests the value of sampleSizeForConfidenceInterval when called with legal arguments"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer([2.7, 2.4, 1.9, 2.6, 2.4, 1.9, 2.3, 2.2, 2.5, 2.3, 1.8, 2.5, 2.0, 2.2])
        self.assertAlmostEqual(analyzer.sampleSizeForConfidenceInterval(0.95, 0.6), 46.52604444444445)

    def test_sampleSizeForConfidenceInterval_confidenceLevelNone(self):
        """Tests that sampleSizeForConfidenceInterval raises an error when given a null confidence level"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.sampleSizeForConfidenceInterval, None, 0.3)

    def test_sampleSizeForConfidenceInterval_confidenceLevelNegative(self):
        """Tests that sampleSizeForConfidenceInterval raises an error when given a negative confidence level"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.sampleSizeForConfidenceInterval, -1, 0.3)

    def test_sampleSizeForConfidenceInterval_confidenceLevelTooLarge(self):
        """Tests that sampleSizeForConfidenceInterval raises an error when given a confidence level that is over 1"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.sampleSizeForConfidenceInterval, 2, 0.3)

    def test_sampleSizeForConfidenceInterval_widthNone(self):
        """Tests that sampleSizeForConfidenceInterval raises an error when given a null confidence level"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.sampleSizeForConfidenceInterval, 0.95, None)

    def test_sampleSizeForConfidenceInterval_widthNegative(self):
        """Tests that sampleSizeForConfidenceInterval raises an error when given a negative confidence level"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.sampleSizeForConfidenceInterval, 0.95, -1)

    def test_sampleSizeForTesting_whenCalled(self):
        """Tests the value of getTestStatistic when called with legal arguments"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertAlmostEqual(analyzer.sampleSizeForTesting(type1Confidence=0.95, type2Confidence=0.75, delta=0.3), 31.4306944411)

    def test_sampleSizeForTesting_type1ConfidenceNone(self):
        """Tests that getConfidenceInterval raises an error when given a type1Confidence"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.sampleSizeForTesting, type1Confidence=None, type2Confidence=0.75, delta=0.3)

    def test_sampleSizeForTesting_type1ConfidenceNegative(self):
        """Tests that getConfidenceInterval raises an error when given a type1Confidence"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.sampleSizeForTesting, type1Confidence=-1, type2Confidence=0.75, delta=0.3)

    def test_sampleSizeForTesting_type1ConfidenceTooLarge(self):
        """Tests that getConfidenceInterval raises an error when given a type1Confidence"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.sampleSizeForTesting, type1Confidence=2, type2Confidence=0.75, delta=0.3)

    def test_sampleSizeForTesting_type2ConfidenceNone(self):
        """Tests that getConfidenceInterval raises an error when given a type2Confidence"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.sampleSizeForTesting, type1Confidence=0.95, type2Confidence=None, delta=0.3)

    def test_sampleSizeForTesting_type2ConfidenceNegative(self):
        """Tests that getConfidenceInterval raises an error when given a type2Confidence"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.sampleSizeForTesting, type1Confidence=0.95, type2Confidence=-1, delta=0.3)

    def test_sampleSizeForTesting_type2ConfidenceTooLarge(self):
        """Tests that getConfidenceInterval raises an error when given a type2Confidence"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.sampleSizeForTesting, type1Confidence=0.95, type2Confidence=2, delta=0.3)

    def test_sampleSizeForTesting_deltaNone(self):
        """Tests that getConfidenceInterval raises an error when given a null delta"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.sampleSizeForTesting, type1Confidence=0.95, type2Confidence=0.3, delta=None)

    def test_getTestStatistic_whenCalled(self):
        """Tests the value of getTestStatistic when called with legal arguments"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertAlmostEqual(analyzer.getTestStatistic(0.3), 2.2050588385131595)

    def test_getTestStatistic_meanNull(self):
        """Tests that getConfidenceInterval raises an error when given a null mean"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError, analyzer.getTestStatistic, None)

    def test_rightTailMeanSignificanceTest_whenCalled(self):
        """Tests the value of rightTailMeanSignificanceTest when called with legal arguments"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertTrue(analyzer.rightTailMeanSignificanceTest(0.3, 0.96))
        self.assertFalse(analyzer.rightTailMeanSignificanceTest(0.3, 0.99))

    def test_rightTailMeanSignificanceTest_type1ConfidenceNone(self):
        """Tests that rightTailMeanSignificanceTest raises an error when given a null type1Confidence"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.rightTailMeanSignificanceTest, mean=0.3, type1Confidence=None)

    def test_rightTailMeanSignificanceTest_type1ConfidenceNegative(self):
        """Tests that rightTailMeanSignificanceTest raises an error when given a negative type1Confidence"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.rightTailMeanSignificanceTest, mean=0.3, type1Confidence=-1)

    def test_rightTailMeanSignificanceTest_type1ConfidenceTooLarge(self):
        """Tests that rightTailMeanSignificanceTest raises an error when given a type1Confidence over 1"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.rightTailMeanSignificanceTest, mean=0.3, type1Confidence=2)

    def test_rightTailMeanSignificanceTest_meanNone(self):
        """Tests that rightTailMeanSignificanceTest raises an error when given a null mean"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.rightTailMeanSignificanceTest, mean=None, type1Confidence=0.95)

    def test_leftTailMeanSignificanceTest_whenCalled(self):
        """Tests the value of leftTailMeanSignificanceTest when called with legal arguments"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertTrue(analyzer.leftTailMeanSignificanceTest(1, 0.95))
        self.assertFalse(analyzer.leftTailMeanSignificanceTest(0.3, 0.99))

    def test_leftTailMeanSignificanceTest_type1ConfidenceNone(self):
        """Tests that leftTailMeanSignificanceTest raises an error when given a null type1Confidence"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.leftTailMeanSignificanceTest, mean=0.3, type1Confidence=None)

    def test_leftTailMeanSignificanceTest_type1ConfidenceNegative(self):
        """Tests that leftTailMeanSignificanceTest raises an error when given a negative type1Confidence"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.leftTailMeanSignificanceTest, mean=0.3, type1Confidence=-1)

    def test_leftTailMeanSignificanceTest_type1ConfidenceTooLarge(self):
        """Tests that leftTailMeanSignificanceTest raises an error when given a type1Confidence over 1"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.leftTailMeanSignificanceTest, mean=0.3, type1Confidence=2)

    def test_leftTailMeanSignificanceTest_meanNone(self):
        """Tests that leftTailMeanSignificanceTest raises an error when given a null mean"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.leftTailMeanSignificanceTest, mean=None, type1Confidence=0.95)

    def test_twinTailMeanSignificanceTest_whenCalled(self):
        """Tests the value of twinTailMeanSignificanceTest when called with legal arguments"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertTrue(analyzer.twinTailMeanSignificanceTest(0.2, 0.95))
        self.assertFalse(analyzer.twinTailMeanSignificanceTest(0.3, 0.99))

    def test_twinTailMeanSignificanceTest_type1ConfidenceNone(self):
        """Tests that leftTailMeanSignificanceTest raises an error when given a null type1Confidence"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.twinTailMeanSignificanceTest, mean=0.3, type1Confidence=None)

    def test_twinTailMeanSignificanceTest_type1ConfidenceNegative(self):
        """Tests that leftTailMeanSignificanceTest raises an error when given a negative type1Confidence"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.twinTailMeanSignificanceTest, mean=0.3, type1Confidence=-1)

    def test_twinTailMeanSignificanceTest_type1ConfidenceTooLarge(self):
        """Tests that leftTailMeanSignificanceTest raises an error when given a type1Confidence over 1"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.twinTailMeanSignificanceTest, mean=0.3, type1Confidence=2)

    def test_twinTailMeanSignificanceTest_meanNone(self):
        """Tests that leftTailMeanSignificanceTest raises an error when given a null mean"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.twinTailMeanSignificanceTest, mean=None, type1Confidence=0.95)

    def test_getTestPower_whenCalled(self):
        """Tests the value of getTestPower when called with legal arguments"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertAlmostEqual(analyzer.getTestPower(0.3, 0.95), 0.7120898636179198)

    def test_getTestPower_type1ConfidenceNone(self):
        """Tests that leftTailMeanSignificanceTest raises an error when given a null type1Confidence"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.getTestPower, mean=0.3, type1Confidence=None)

    def test_getTestPower_type1ConfidenceNegative(self):
        """Tests that leftTailMeanSignificanceTest raises an error when given a negative type1Confidence"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.getTestPower, mean=0.3, type1Confidence=-1)

    def test_getTestPower_type1ConfidenceTooLarge(self):
        """Tests that leftTailMeanSignificanceTest raises an error when given a type1Confidence over 1"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.getTestPower, mean=0.3, type1Confidence=2)

    def test_getTestPower_meanNone(self):
        """Tests that leftTailMeanSignificanceTest raises an error when given a null mean"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.getTestPower, mean=None, type1Confidence=0.95)

    def test_rightTailMeanSignificanceAndPowerTest_rejectsNullHypothesis(self):
        """Tests the value of rightTailMeanSignificanceAndPowerTest when called with legal arguments"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertEqual(analyzer.rightTailMeanSignificanceAndPowerTest(0.2, 0.95, 0.75), (False, True))

    def test_rightTailMeanSignificanceAndPowerTest_failesToRejectNullHypothesis(self):
        """Tests the value of rightTailMeanSignificanceAndPowerTest when called with legal arguments"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertEqual(analyzer.rightTailMeanSignificanceAndPowerTest(0.3, 0.99, 0.75), (False, False))

    def test_rightTailMeanSignificanceAndPowerTest_type1ConfidenceNone(self):
        """Tests that rightTailMeanSignificanceAndPowerTest raises an error when given a null type1Confidence"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.rightTailMeanSignificanceAndPowerTest, mean=0.3, type1Confidence=None, type2Confidence=0.95)

    def test_rightTailMeanSignificanceAndPowerTest_type1ConfidenceNegative(self):
        """Tests that rightTailMeanSignificanceAndPowerTest raises an error when given a negative type1Confidence"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.rightTailMeanSignificanceAndPowerTest, mean=0.3, type1Confidence=-1, type2Confidence=0.95)

    def test_rightTailMeanSignificanceAndPowerTest_type1ConfidenceTooLarge(self):
        """Tests that rightTailMeanSignificanceAndPowerTest raises an error when given a type1Confidence over 1"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.rightTailMeanSignificanceAndPowerTest, mean=0.3, type1Confidence=2, type2Confidence=0.95)

    def test_rightTailMeanSignificanceAndPowerTest_type2ConfidenceNone(self):
        """Tests that rightTailMeanSignificanceAndPowerTest raises an error when given a null type2Confidence"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.rightTailMeanSignificanceAndPowerTest, mean=0.3, type1Confidence=0.95, type2Confidence=None)

    def test_rightTailMeanSignificanceAndPowerTest_type2ConfidenceNegative(self):
        """Tests that rightTailMeanSignificanceAndPowerTest raises an error when given a negative type2Confidence"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.rightTailMeanSignificanceAndPowerTest, mean=0.3, type1Confidence=0.95, type2Confidence=-1)

    def test_rightTailMeanSignificanceAndPowerTest_type2ConfidenceTooLarge(self):
        """Tests that rightTailMeanSignificanceAndPowerTest raises an error when given a type2Confidence over 1"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.rightTailMeanSignificanceAndPowerTest, mean=0.3, type1Confidence=0.95, type2Confidence=2)

    def test_rightTailMeanSignificanceAndPowerTest_meanNone(self):
        """Tests that rightTailMeanSignificanceAndPowerTest raises an error when given a null mean"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.rightTailMeanSignificanceAndPowerTest, mean=None, type1Confidence=0.95, type2Confidence=0.95)

    def test_leftTailMeanSignificanceAndPowerTest_rejectsNullHypothesis(self):
        """Tests the value of leftTailMeanSignificanceAndPowerTest when called with legal arguments"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertEqual(analyzer.leftTailMeanSignificanceAndPowerTest(1, 0.95, 0.75), (False, True))

    def test_leftTailMeanSignificanceAndPowerTest_failesToRejectNullHypothesis(self):
        """Tests the value of leftTailMeanSignificanceAndPowerTest when called with legal arguments"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertEqual(analyzer.leftTailMeanSignificanceAndPowerTest(0.3, 0.99, 0.75), (False, False))

    def test_leftTailMeanSignificanceAndPowerTest_type1ConfidenceNone(self):
        """Tests that leftTailMeanSignificanceAndPowerTest raises an error when given a null type1Confidence"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.leftTailMeanSignificanceAndPowerTest, mean=0.3, type1Confidence=None, type2Confidence=0.95)

    def test_leftTailMeanSignificanceAndPowerTest_type1ConfidenceNegative(self):
        """Tests that leftTailMeanSignificanceAndPowerTest raises an error when given a negative type1Confidence"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.leftTailMeanSignificanceAndPowerTest, mean=0.3, type1Confidence=-1, type2Confidence=0.95)

    def test_leftTailMeanSignificanceAndPowerTest_type1ConfidenceTooLarge(self):
        """Tests that leftTailMeanSignificanceAndPowerTest raises an error when given a type1Confidence over 1"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.leftTailMeanSignificanceAndPowerTest, mean=0.3, type1Confidence=2, type2Confidence=0.95)

    def test_leftTailMeanSignificanceAndPowerTest_type2ConfidenceNone(self):
        """Tests that leftTailMeanSignificanceAndPowerTest raises an error when given a null type2Confidence"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.leftTailMeanSignificanceAndPowerTest, mean=0.3, type1Confidence=0.95, type2Confidence=None)

    def test_leftTailMeanSignificanceAndPowerTest_type2ConfidenceNegative(self):
        """Tests that leftTailMeanSignificanceAndPowerTest raises an error when given a negative type2Confidence"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.leftTailMeanSignificanceAndPowerTest, mean=0.3, type1Confidence=0.95, type2Confidence=-1)

    def test_leftTailMeanSignificanceAndPowerTest_type2ConfidenceTooLarge(self):
        """Tests that leftTailMeanSignificanceAndPowerTest raises an error when given a type2Confidence over 1"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.leftTailMeanSignificanceAndPowerTest, mean=0.3, type1Confidence=0.95, type2Confidence=2)

    def test_leftTailMeanSignificanceAndPowerTest_meanNone(self):
        """Tests that leftTailMeanSignificanceAndPowerTest raises an error when given a null mean"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.leftTailMeanSignificanceAndPowerTest, mean=None, type1Confidence=0.95, type2Confidence=0.95)

    def test_twinTailMeanSignificanceAndPowerTest_rejectsNullHypothesis(self):
        """Tests the value of twinTailMeanSignificanceAndPowerTest when called with legal arguments"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertEqual(analyzer.twinTailMeanSignificanceAndPowerTest(1, 0.95, 0.75), (False, True))

    def test_twinTailMeanSignificanceAndPowerTest_failesToRejectNullHypothesis(self):
        """Tests the value of twinTailMeanSignificanceAndPowerTest when called with legal arguments"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertEqual(analyzer.twinTailMeanSignificanceAndPowerTest(0.3, 0.99, 0.75), (False, False))

    def test_twinTailMeanSignificanceAndPowerTest_type1ConfidenceNone(self):
        """Tests that twinTailMeanSignificanceAndPowerTest raises an error when given a null type1Confidence"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.twinTailMeanSignificanceAndPowerTest, mean=0.3, type1Confidence=None, type2Confidence=0.95)

    def test_twinTailMeanSignificanceAndPowerTest_type1ConfidenceNegative(self):
        """Tests that twinTailMeanSignificanceAndPowerTest raises an error when given a negative type1Confidence"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.twinTailMeanSignificanceAndPowerTest, mean=0.3, type1Confidence=-1, type2Confidence=0.95)

    def test_twinTailMeanSignificanceAndPowerTest_type1ConfidenceTooLarge(self):
        """Tests that twinTailMeanSignificanceAndPowerTest raises an error when given a type1Confidence over 1"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.twinTailMeanSignificanceAndPowerTest, mean=0.3, type1Confidence=2, type2Confidence=0.95)

    def test_twinTailMeanSignificanceAndPowerTest_type2ConfidenceNone(self):
        """Tests that twinTailMeanSignificanceAndPowerTest raises an error when given a null type2Confidence"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.twinTailMeanSignificanceAndPowerTest, mean=0.3, type1Confidence=0.95, type2Confidence=None)

    def test_twinTailMeanSignificanceAndPowerTest_type2ConfidenceNegative(self):
        """Tests that twinTailMeanSignificanceAndPowerTest raises an error when given a negative type2Confidence"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.twinTailMeanSignificanceAndPowerTest, mean=0.3, type1Confidence=0.95, type2Confidence=-1)

    def test_twinTailMeanSignificanceAndPowerTest_type2ConfidenceTooLarge(self):
        """Tests that twinTailMeanSignificanceAndPowerTest raises an error when given a type2Confidence over 1"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.twinTailMeanSignificanceAndPowerTest, mean=0.3, type1Confidence=0.95, type2Confidence=2)

    def test_twinTailMeanSignificanceAndPowerTest_meanNone(self):
        """Tests that twinTailMeanSignificanceAndPowerTest raises an error when given a null mean"""
        analyzer: NormalCentralValueAnalyzer = NormalCentralValueAnalyzer(TEST_VALUES)
        self.assertRaises(ValueError,analyzer.twinTailMeanSignificanceAndPowerTest, mean=None, type1Confidence=0.95, type2Confidence=0.95)
