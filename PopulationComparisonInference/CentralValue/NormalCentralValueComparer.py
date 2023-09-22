from math import sqrt
from Utilities.SampleUtilities import SampleUtilities
from PopulationComparisonInference.CentralValue.IPopulationCentralValueComparer import IPopulationCentralValueComparer
from Utilities.TDistribution.ITDistribution import ITDistribution
from Utilities.TDistribution.SciPyTDistribution import SciPyTDistribution

class NormalCentralValueComparer(IPopulationCentralValueComparer):
    """Class for comparing the central values of two independent single dimensional, normally distributed populations with unequal variances"""

    def __init__(self, sample1: list, sample2: list, tDist: ITDistribution = SciPyTDistribution()) -> None:
        """
        Description
        ----------
        Constructor for the NormalCentralValueAnalyzer

        Parameters
        ----------
        sample1: list
            The list of floats representing a sample from the population distribution 1

        sample2: list
            The list of floats representing a sample from the population distribution 2

        tDist: ITDistribution
            t distribution utility
        """
        if sample1 == None or len(sample1) == 0:
            raise ValueError("Cannot have empty or null sample1")
        if sample2 == None or len(sample2) == 0:
            raise ValueError("Cannot have empty or null sample2")
        if tDist == None:
            raise ValueError("Cannot have null tDist")

        self.sample1: list = sample1
        self.mean1: float = SampleUtilities.estimateMean(sample1)
        self.stdDev1: float = SampleUtilities.estimateStdDev(sample1)
        self.var1: float = self.stdDev1 ** 2
        self.n1: int = len(sample1)
        self.sample2: list = sample2
        self.mean2: float = SampleUtilities.estimateMean(sample2)
        self.stdDev2: float = SampleUtilities.estimateStdDev(sample2)
        self.var2: float = self.stdDev2 ** 2
        self.n2: int = len(sample2)
        self.c: float = self.__getCValue()
        self.df: float = self.__getDf()
        self.tDist: ITDistribution = tDist
    
    def __getCValue(self) -> float:
        return self.var1 / (self.n1 * ((self.var1/self.n1) + (self.var2/self.n2)))

    def __getDf(self) -> float:
        return (self.n1 - 1) * (self.n2 - 1) / ( ((1 - self.c) ** 2) * (self.n1 - 1) + ((self.c ** 2) * (self.n2 - 1)) )

    def getConfidenceInterval(self, confidenceLevel: float) -> tuple:
        if confidenceLevel == None or confidenceLevel < 0:
            raise ValueError("Cannot have negative or null confidenceLevel")
        if confidenceLevel > 1:
            raise ValueError("Cannot have a confidenceLevel over 1")
        sampleDiff: float = self.mean1 - self.mean2
        alpha: float = (1 - confidenceLevel)/2
        width: float = self.tDist.getTPercentileValue(1-alpha, self.df) * sqrt((self.var1/self.n1) + (self.var2/self.n2))
        return (sampleDiff - width, sampleDiff + width)

    def getTestStatistic(self, testDelta: float) -> float:
        if testDelta == None:
            raise ValueError("Cannot have a null testDelta")
        return (self.mean1 - self.mean2 - testDelta) / sqrt((self.var1/self.n1) + (self.var2/self.n2))

    def rightTailDeltaSignificanceTest(self, delta: float, type1Confidence: float) -> bool:
        if type1Confidence == None or type1Confidence < 0:
            raise ValueError("Cannot have negative or null type1Confidence")
        if type1Confidence > 1:
            raise ValueError("Cannot have a type1Confidence over 1")
        if delta == None:
            raise ValueError("Cannot have a null delta")
        testStat: float = self.getTestStatistic(delta)
        tVal: float = self.tDist.getTPercentileValue(type1Confidence, self.df)
        return testStat >= tVal

    def leftTailDeltaSignificanceTest(self, delta: float, type1Confidence: float) -> bool:
        if type1Confidence == None or type1Confidence < 0:
            raise ValueError("Cannot have negative or null type1Confidence")
        if type1Confidence > 1:
            raise ValueError("Cannot have a type1Confidence over 1")
        testStat: float = self.getTestStatistic(delta)
        tVal: float = self.tDist.getTPercentileValue(type1Confidence, self.df)
        return testStat <= -tVal

    def twinTailDeltaSignificanceTest(self, delta: float, type1Confidence: float) -> bool:
        if type1Confidence == None or type1Confidence < 0:
            raise ValueError("Cannot have negative or null type1Confidence")
        if type1Confidence > 1:
            raise ValueError("Cannot have a type1Confidence over 1")
        if delta == None:
            raise ValueError("Cannot have a null delta")
        testStat: float = self.getTestStatistic(delta)
        alpha: float = (1 - type1Confidence)/2
        tVal: float = self.tDist.getTPercentileValue(1-alpha, self.df)
        return abs(testStat) >= tVal
