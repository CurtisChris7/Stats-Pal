import unittest
from PopulationComparisonInference.Variance.NormalVarianceComparer import NormalVarianceComparer

class NormalVarianceComparerTests(unittest.TestCase):
    """Unit testing class for the NormalVarianceComparer"""

    def test_constructor_sample1None(self):
        """Tests that the constructor raises an error with null sample1"""
        self.assertRaises(ValueError, NormalVarianceComparer, sample1=None, sample2 = [1, 2])

    def test_constructor_sample1Empty(self):
        """Tests that the constructor raises an error with empty sample1"""
        self.assertRaises(ValueError, NormalVarianceComparer, sample1=[], sample2 = [1, 2])

    def test_constructor_sample2None(self):
        """Tests that the constructor raises an error with null sample2"""
        self.assertRaises(ValueError, NormalVarianceComparer, sample1 = [1, 2], sample2=None)

    def test_constructor_sample2Empty(self):
        """Tests that the constructor raises an error with empty sample2"""
        self.assertRaises(ValueError, NormalVarianceComparer, sample1 = [1, 2], sample2=[])

    def test_constructor_fDistNone(self):
        """Tests that the constructor raises an error with null fDist"""
        self.assertRaises(ValueError, NormalVarianceComparer, sample1 = [1, 2], sample2 = [1, 2], fDist=None)

    def test_getConfidenceInterval_whenCalled(self):
        """Tests the value of getConfidenceInterval when called"""
        comparer: NormalVarianceComparer = NormalVarianceComparer([1, 2], [1, 2])
        # We set specific values for our test
        comparer.var1 = 16.37 ** 2
        comparer.n1 = 40
        comparer.df1 = 39

        comparer.var2 = 9.88 ** 2
        comparer.n2 = 40
        comparer.df2 = 39

        interval: tuple = comparer.getConfidenceInterval(0.95)
        self.assertAlmostEqual(interval[0], 1.4519661253267149)
        self.assertAlmostEqual(interval[1], 5.1905150544247)

    def test_getConfidenceInterval_confidenceLevelNone(self):
        """Tests that getConfidenceInterval raises an error when given a null confidence level"""
        comparer: NormalVarianceComparer = NormalVarianceComparer([1, 2], [1, 2])
        self.assertRaises(ValueError, comparer.getConfidenceInterval, None)

    def test_getConfidenceInterval_confidenceLevelNegative(self):
        """Tests that getConfidenceInterval raises an error when given a negative confidence level"""
        comparer: NormalVarianceComparer = NormalVarianceComparer([1, 2], [1, 2])
        self.assertRaises(ValueError, comparer.getConfidenceInterval, -1)

    def test_getConfidenceInterval_confidenceLevelTooLarge(self):
        """Tests that getConfidenceInterval raises an error when given a confidence level that is over 1"""
        comparer: NormalVarianceComparer = NormalVarianceComparer([1, 2], [1, 2])
        self.assertRaises(ValueError, comparer.getConfidenceInterval, 2)

    def test_getTestStatistic_whenCalled(self):
        """Tests the value of getTestStatistic when called"""
        comparer: NormalVarianceComparer = NormalVarianceComparer([1, 2], [1, 2])
        # We set specific values for our test
        comparer.var1 = 16.37 ** 2
        comparer.n1 = 40
        comparer.df1 = 39

        comparer.var2 = 9.88 ** 2
        comparer.n2 = 40
        comparer.df2 = 39
        self.assertAlmostEqual(comparer.getTestStatistic(), 2.7452599206674426)

    def test_population1HasGreaterVarianceTest_whenCalled(self):
        """Tests the value of population1HasGreaterVarianceTest when called"""
        comparer: NormalVarianceComparer = NormalVarianceComparer([1, 2], [1, 2])
        # We set specific values for our test
        comparer.var1 = 16.37 ** 2
        comparer.n1 = 40
        comparer.df1 = 39

        comparer.var2 = 9.88 ** 2
        comparer.n2 = 40
        comparer.df2 = 39
        self.assertTrue(comparer.population1HasGreaterVarianceTest(0.95))

    def test_population1HasGreaterVarianceTest_type1ConfidenceNone(self):
        """Tests that population1HasGreaterVarianceTest raises an error when given a null type1Confidence"""
        analyzer: NormalVarianceComparer = NormalVarianceComparer([1, 2], [1, 2])
        self.assertRaises(ValueError,analyzer.population1HasGreaterVarianceTest, type1Confidence=None)

    def test_population1HasGreaterVarianceTest_type1ConfidenceNegative(self):
        """Tests that population1HasGreaterVarianceTest raises an error when given a negative type1Confidence"""
        analyzer: NormalVarianceComparer = NormalVarianceComparer([1, 2], [1, 2])
        self.assertRaises(ValueError,analyzer.population1HasGreaterVarianceTest, type1Confidence=-1)

    def test_population1HasGreaterVarianceTest_type1ConfidenceTooLarge(self):
        """Tests that population1HasGreaterVarianceTest raises an error when given a type1Confidence over 1"""
        analyzer: NormalVarianceComparer = NormalVarianceComparer([1, 2], [1, 2])
        self.assertRaises(ValueError,analyzer.population1HasGreaterVarianceTest, type1Confidence=2)

    def test_populationsHaveUnequalVarianceTest_whenCalled(self):
        """Tests the value of populationsHaveUnequalVarianceTest when called"""
        comparer: NormalVarianceComparer = NormalVarianceComparer([1, 2], [1, 2])
        # We set specific values for our test
        comparer.var1 = 16.37 ** 2
        comparer.n1 = 40
        comparer.df1 = 39

        comparer.var2 = 9.88 ** 2
        comparer.n2 = 40
        comparer.df2 = 39
        self.assertTrue(comparer.populationsHaveUnequalVarianceTest(0.95))

    def test_populationsHaveUnequalVarianceTest_type1ConfidenceNone(self):
        """Tests that populationsHaveUnequalVarianceTest raises an error when given a null type1Confidence"""
        analyzer: NormalVarianceComparer = NormalVarianceComparer([1, 2], [1, 2])
        self.assertRaises(ValueError,analyzer.populationsHaveUnequalVarianceTest, type1Confidence=None)

    def test_populationsHaveUnequalVarianceTest_type1ConfidenceNegative(self):
        """Tests that populationsHaveUnequalVarianceTest raises an error when given a negative type1Confidence"""
        analyzer: NormalVarianceComparer = NormalVarianceComparer([1, 2], [1, 2])
        self.assertRaises(ValueError,analyzer.populationsHaveUnequalVarianceTest, type1Confidence=-1)

    def test_populationsHaveUnequalVarianceTest_type1ConfidenceTooLarge(self):
        """Tests that populationsHaveUnequalVarianceTest raises an error when given a type1Confidence over 1"""
        analyzer: NormalVarianceComparer = NormalVarianceComparer([1, 2], [1, 2])
        self.assertRaises(ValueError,analyzer.populationsHaveUnequalVarianceTest, type1Confidence=2)
