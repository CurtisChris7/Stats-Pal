from math import sqrt
from Utilities.SampleUtilities import SampleUtilities
from PopulationComparisonInference.Variance.IPopulationVarianceComparer import IPopulationVarianceComparer
from Utilities.FDistribution.IFDistribution import IFDistribution
from Utilities.FDistribution.SciPyFDistribution import SciPyFDistribution

class NormalVarianceComparer(IPopulationVarianceComparer):
    """Class for comparing the central values of two independent single dimensional, normally distributed populations with unequal variances"""

    def __init__(self, sample1: list, sample2: list, fDist: IFDistribution = SciPyFDistribution()) -> None:
        """
        Description
        ----------
        Constructor for the NormalVarianceAnalyzer

        Parameters
        ----------
        sample1: list
            The list of floats representing a sample from the population distribution 1

        sample2: list
            The list of floats representing a sample from the population distribution 2

        fDist: IFDistribution
            f distribution utility
        """
        if sample1 == None or len(sample1) == 0:
            raise ValueError("Cannot have empty or null sample1")
        if sample2 == None or len(sample2) == 0:
            raise ValueError("Cannot have empty or null sample2")
        if fDist == None:
            raise ValueError("Cannot have null fDist")

        self.sample1: list = sample1
        self.var1: float = SampleUtilities.estimateVariance(sample1)
        self.n1: int = len(sample1)
        self.df1: int = self.n1 - 1

        self.sample2: list = sample2
        self.var2: float = SampleUtilities.estimateVariance(sample2)
        self.n2: int = len(sample2)
        self.df2: int = self.n2 - 1

        self.fDist: IFDistribution = fDist

    def getConfidenceInterval(self, confidenceLevel: float) -> tuple:
        if confidenceLevel == None or confidenceLevel < 0:
            raise ValueError("Cannot have negative or null confidenceLevel")
        if confidenceLevel > 1:
            raise ValueError("Cannot have a confidenceLevel over 1")
        testStat: float = self.getTestStatistic()
        fLower: float = self.fDist.getFLowerValue(confidenceLevel, self.df1, self.df2)
        fUpper: float = self.fDist.getFUpperValue(confidenceLevel, self.df1, self.df2)
        return (testStat * fLower, testStat * fUpper)

    def getTestStatistic(self) -> float:
        return self.var1 / self.var2

    def population1HasGreaterVarianceTest(self, type1Confidence: float) -> bool:
        if type1Confidence == None or type1Confidence < 0:
            raise ValueError("Cannot have negative or null type1Confidence")
        if type1Confidence > 1:
            raise ValueError("Cannot have a type1Confidence over 1")
        testStat: float = self.getTestStatistic()
        fVal: float = self.fDist.getFPercentileValue(type1Confidence, self.df1, self.df2)
        return testStat >= fVal

    def populationsHaveUnequalVarianceTest(self, type1Confidence: float) -> bool:
        if type1Confidence == None or type1Confidence < 0:
            raise ValueError("Cannot have negative or null type1Confidence")
        if type1Confidence > 1:
            raise ValueError("Cannot have a type1Confidence over 1")
        testStat: float = self.getTestStatistic()
        fLower: float = self.fDist.getFLowerValue(type1Confidence, self.df1, self.df2)
        fUpper: float = self.fDist.getFUpperValue(type1Confidence, self.df1, self.df2)
        return testStat <= fLower or testStat >= fUpper
