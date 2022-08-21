from math import sqrt
from Utilities.SampleUtilities import SampleUtilities
from Utilities.TDistribution.ITDistribution import ITDistribution
from Utilities.TDistribution.SciPyTDistribution import SciPyTDistribution
from PopulationComparisonInference.CentralValue.IPopulationCentralValueComparer import IPopulationCentralValueComparer

class PairedNormalCentralValueComparer(IPopulationCentralValueComparer):
    """Class for comparing the central values of two paired single dimensional, normally distributed populations"""

    def __init__(self, sample1: list, sample2: list, tDist: ITDistribution = SciPyTDistribution()) -> None:
        """
        Description
        ----------
        Constructor for the PairedNormalCentralValueComparer

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
        if len(sample1) != len(sample2):
            raise ValueError("Both samples must have equal size")
        if tDist == None:
            raise ValueError("Cannot have null tDist")

        self.values = PairedNormalCentralValueComparer.__getDifferenceList(sample1, sample2)
        self.mean = SampleUtilities.estimateMean(self.values)
        self.stdDev = SampleUtilities.estimateStdDev(self.values)
        self.n = len(sample1)
        self.df = self.n - 1
        self.tDist = tDist

    def __getDifferenceList(sample1: list, sample2: list) -> list:
        differencesList: list = []
        for i in range(len(sample1)):
            differencesList.append(sample1[i] - sample2[i])
        return differencesList

    def getConfidenceInterval(self, confidenceLevel: float) -> tuple:
        if confidenceLevel == None or confidenceLevel < 0:
            raise ValueError("Cannot have negative or null confidenceLevel")
        if confidenceLevel > 1:
            raise ValueError("Cannot have a confidenceLevel over 1")
        alpha: float = (1 - confidenceLevel)/2
        width: float = self.tDist.getTPercentileValue(1-alpha, self.df) * self.stdDev / sqrt(self.n)
        return (self.mean - width, self.mean + width)

    def getTestStatistic(self, testDelta: float) -> float:
        if testDelta == None:
            raise ValueError("Cannot have a null testDelta")
        return (self.mean - testDelta) * sqrt(self.n) / self.stdDev

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
        return abs(testStat) >= -tVal
