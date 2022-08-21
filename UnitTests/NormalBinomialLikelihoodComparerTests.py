import unittest
from PopulationComparisonInference.BinomialLikelihood.NormalBinomialLikelihoodComparer import NormalBinomialLikelihoodComparer

class NormalBinomialLikelihoodComparerTests(unittest.TestCase):
    """Unit testing class for the NormalBinomialLikelihoodComparer"""

    def test_constructor_sample1None(self):
        """Tests that the constructor raises an error with null sample1"""
        self.assertRaises(ValueError, NormalBinomialLikelihoodComparer, sample1=None, sample2 = [1, 0])

    def test_constructor_sample1Empty(self):
        """Tests that the constructor raises an error with empty sample1"""
        self.assertRaises(ValueError, NormalBinomialLikelihoodComparer, sample1=[], sample2 = [1, 0])

    def test_constructor_sample2None(self):
        """Tests that the constructor raises an error with null sample2"""
        self.assertRaises(ValueError, NormalBinomialLikelihoodComparer, sample1 = [1, 0], sample2=None)

    def test_constructor_sample2Empty(self):
        """Tests that the constructor raises an error with empty sample2"""
        self.assertRaises(ValueError, NormalBinomialLikelihoodComparer, sample1 = [1, 0], sample2=[])

    def test_constructor_normalDistNone(self):
        """Tests that the constructor raises an error with null normalDist"""
        self.assertRaises(ValueError, NormalBinomialLikelihoodComparer, sample1 = [1, 0], sample2 = [1, 0], normDist=None)

    def test_getStandardError_whenCalled(self):
        """Tests the value of getStandardError when called"""
        comparer: NormalBinomialLikelihoodComparer = NormalBinomialLikelihoodComparer([1, 0], [1, 0])
        # We set specific values for our test
        comparer.likelihood1 = 0.784
        comparer.n1 = 527
        comparer.likelihood2 = 0.645
        comparer.n2 = 608
        self.assertAlmostEqual(comparer.getStandardError(), 0.02641854427856807)

    def test_getConfidenceInterval_whenCalled(self):
        """Tests the value of getConfidenceInterval when called"""
        comparer: NormalBinomialLikelihoodComparer = NormalBinomialLikelihoodComparer([1, 0], [1, 0])
        # We set specific values for our test
        comparer.likelihood1 = 0.784
        comparer.n1 = 527
        comparer.likelihood2 = 0.645
        comparer.n2 = 608
        comparer.stdError = comparer.getStandardError()
        
        interval: tuple = comparer.getConfidenceInterval(0.95)
        self.assertAlmostEqual(interval[0], 0.0872196532140066)
        self.assertAlmostEqual(interval[1], 0.19078034678599343)

    def test_getConfidenceInterval_confidenceLevelNone(self):
        """Tests that getConfidenceInterval raises an error when given a null confidence level"""
        comparer: NormalBinomialLikelihoodComparer = NormalBinomialLikelihoodComparer([1, 0], [1, 0])
        self.assertRaises(ValueError, comparer.getConfidenceInterval, None)

    def test_getConfidenceInterval_confidenceLevelNegative(self):
        """Tests that getConfidenceInterval raises an error when given a negative confidence level"""
        comparer: NormalBinomialLikelihoodComparer = NormalBinomialLikelihoodComparer([1, 0], [1, 0])
        self.assertRaises(ValueError, comparer.getConfidenceInterval, -1)

    def test_getConfidenceInterval_confidenceLevelTooLarge(self):
        """Tests that getConfidenceInterval raises an error when given a confidence level that is over 1"""
        comparer: NormalBinomialLikelihoodComparer = NormalBinomialLikelihoodComparer([1, 0], [1, 0])
        self.assertRaises(ValueError, comparer.getConfidenceInterval, 2)

    def test_getTestStatistic_whenCalled(self):
        """Tests the value of getTestStatistic when called"""
        comparer: NormalBinomialLikelihoodComparer = NormalBinomialLikelihoodComparer([1, 0], [1, 0])
        # We set specific values for our test
        comparer.likelihood1 = 0.752
        comparer.n1 = 125
        comparer.likelihood2 = 0.646
        comparer.n2 = 175
        comparer.stdError = comparer.getStandardError()
        self.assertAlmostEqual(comparer.getTestStatistic(), 2.003664831784244)

    def test_population1LikelihoodGreaterTest_whenCalled(self):
        """Tests the value of population1LikelihoodGreaterTest when called"""
        comparer: NormalBinomialLikelihoodComparer = NormalBinomialLikelihoodComparer([1, 0], [1, 0])
        # We set specific values for our test
        comparer.likelihood1 = 0.752
        comparer.n1 = 125
        comparer.likelihood2 = 0.646
        comparer.n2 = 175
        comparer.stdError = comparer.getStandardError()
        self.assertTrue(comparer.population1LikelihoodGreaterTest(0.95))
    
    def test_population1LikelihoodGreaterTest_type1ConfidenceNone(self):
        """Tests that population1LikelihoodGreaterTest raises an error when given a null type1Confidence"""
        analyzer: NormalBinomialLikelihoodComparer = NormalBinomialLikelihoodComparer([1, 0], [1, 0])
        self.assertRaises(ValueError,analyzer.population1LikelihoodGreaterTest, type1Confidence=None)

    def test_population1LikelihoodGreaterTest_type1ConfidenceNegative(self):
        """Tests that population1LikelihoodGreaterTest raises an error when given a negative type1Confidence"""
        analyzer: NormalBinomialLikelihoodComparer = NormalBinomialLikelihoodComparer([1, 0], [1, 0])
        self.assertRaises(ValueError,analyzer.population1LikelihoodGreaterTest, type1Confidence=-1)

    def test_population1LikelihoodGreaterTest_type1ConfidenceTooLarge(self):
        """Tests that population1LikelihoodGreaterTest raises an error when given a type1Confidence over 1"""
        analyzer: NormalBinomialLikelihoodComparer = NormalBinomialLikelihoodComparer([1, 0], [1, 0])
        self.assertRaises(ValueError,analyzer.population1LikelihoodGreaterTest, type1Confidence=2)

    def test_population1LikelihoodLesserTest_whenCalled(self):
        """Tests the value of population1LikelihoodLesserTest when called"""
        comparer: NormalBinomialLikelihoodComparer = NormalBinomialLikelihoodComparer([1, 0], [1, 0])
        # We set specific values for our test
        comparer.likelihood1 = 0.752
        comparer.n1 = 125
        comparer.likelihood2 = 0.646
        comparer.n2 = 175
        comparer.stdError = comparer.getStandardError()
        self.assertFalse(comparer.population1LikelihoodLesserTest(0.95))

    def test_population1LikelihoodLesserTest_type1ConfidenceNone(self):
        """Tests that population1LikelihoodLesserTest raises an error when given a null type1Confidence"""
        analyzer: NormalBinomialLikelihoodComparer = NormalBinomialLikelihoodComparer([1, 0], [1, 0])
        self.assertRaises(ValueError,analyzer.population1LikelihoodLesserTest, type1Confidence=None)

    def test_population1LikelihoodLesserTest_type1ConfidenceNegative(self):
        """Tests that population1LikelihoodLesserTest raises an error when given a negative type1Confidence"""
        analyzer: NormalBinomialLikelihoodComparer = NormalBinomialLikelihoodComparer([1, 0], [1, 0])
        self.assertRaises(ValueError,analyzer.population1LikelihoodLesserTest, type1Confidence=-1)

    def test_population1LikelihoodLesserTest_type1ConfidenceTooLarge(self):
        """Tests that population1LikelihoodLesserTest raises an error when given a type1Confidence over 1"""
        analyzer: NormalBinomialLikelihoodComparer = NormalBinomialLikelihoodComparer([1, 0], [1, 0])
        self.assertRaises(ValueError,analyzer.population1LikelihoodLesserTest, type1Confidence=2)

    def test_population1LikelihoodUnequalTest_whenCalled(self):
        """Tests the value of population1LikelihoodUnequalTest when called"""
        comparer: NormalBinomialLikelihoodComparer = NormalBinomialLikelihoodComparer([1, 0], [1, 0])
        # We set specific values for our test
        comparer.likelihood1 = 0.752
        comparer.n1 = 125
        comparer.likelihood2 = 0.646
        comparer.n2 = 175
        comparer.stdError = comparer.getStandardError()
        self.assertTrue(comparer.population1LikelihoodUnequalTest(0.95))

    def test_population1LikelihoodUnequalTest_type1ConfidenceNone(self):
        """Tests that population1LikelihoodUnequalTest raises an error when given a null type1Confidence"""
        analyzer: NormalBinomialLikelihoodComparer = NormalBinomialLikelihoodComparer([1, 0], [1, 0])
        self.assertRaises(ValueError,analyzer.population1LikelihoodUnequalTest, type1Confidence=None)

    def test_population1LikelihoodUnequalTest_type1ConfidenceNegative(self):
        """Tests that population1LikelihoodUnequalTest raises an error when given a negative type1Confidence"""
        analyzer: NormalBinomialLikelihoodComparer = NormalBinomialLikelihoodComparer([1, 0], [1, 0])
        self.assertRaises(ValueError,analyzer.population1LikelihoodUnequalTest, type1Confidence=-1)

    def test_population1LikelihoodUnequalTest_type1ConfidenceTooLarge(self):
        """Tests that population1LikelihoodUnequalTest raises an error when given a type1Confidence over 1"""
        analyzer: NormalBinomialLikelihoodComparer = NormalBinomialLikelihoodComparer([1, 0], [1, 0])
        self.assertRaises(ValueError,analyzer.population1LikelihoodUnequalTest, type1Confidence=2)
