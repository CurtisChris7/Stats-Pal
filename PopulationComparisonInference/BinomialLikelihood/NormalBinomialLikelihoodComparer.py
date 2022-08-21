from math import sqrt
from Utilities.CategoricalSampleUtilities import CategoricalSampleUtilities
from Utilities.NormalDistriution.ApproximateNormalTable import ApproximateNormalTable
from Utilities.NormalDistriution.INormalDistribution import INormalDistribution
from PopulationComparisonInference.BinomialLikelihood.IPopulationBinomalLikelihoodComparer import IPopulationBinomialLikelihoodComparer


class NormalBinomialLikelihoodComparer(IPopulationBinomialLikelihoodComparer):
    """Class for comparing the likelihoods of two independent single dimensional, normally distributed populations with binary data"""

    def __init__(self, sample1: list, sample2: list, normDist: INormalDistribution = ApproximateNormalTable()) -> None:
        """
        Description
        ----------
        Constructor for the BinomialLikelihoodAnalyzer

        Parameters
        ----------
        sample1: list
            The list of floats representing a sample from the population distribution 1

        sample2: list
            The list of floats representing a sample from the population distribution 2

        normDist: INormalDistribution
            normal distribution utility
        """
        if sample1 == None or len(sample1) == 0:
            raise ValueError("Cannot have empty or null sample1")
        if sample2 == None or len(sample2) == 0:
            raise ValueError("Cannot have empty or null sample2")
        if normDist == None:
            raise ValueError("Cannot have null normDist")

        self.sample1: list = sample1
        self.likelihood1: float = CategoricalSampleUtilities.estimateLikelihood(sample1)
        self.n1: int = len(sample1)

        self.sample2: list = sample2
        self.likelihood2: float = CategoricalSampleUtilities.estimateLikelihood(sample2)
        self.n2: int = len(sample2)


        self.stdError: float = self.getStandardError()
        self.normDist: INormalDistribution = normDist

    def getStandardError(self) -> float:
        return sqrt( (self.likelihood1 * (1 - self.likelihood1) / self.n1) + (self.likelihood2 * (1 - self.likelihood2) / self.n2) )

    def getConfidenceInterval(self, confidenceLevel: float) -> tuple:
        if confidenceLevel == None or confidenceLevel < 0:
            raise ValueError("Cannot have negative or null confidenceLevel")
        if confidenceLevel > 1:
            raise ValueError("Cannot have a confidenceLevel over 1")
        sampleDiff: float = self.likelihood1 - self.likelihood2
        alpha: float = (1 - confidenceLevel)/2
        width: float = self.normDist.getZPercentileValue(1-alpha) * self.stdError
        return (sampleDiff - width, sampleDiff + width)

    def getTestStatistic(self) -> float:
        return (self.likelihood1 - self.likelihood2) / self.stdError

    def population1LikelihoodGreaterTest(self, type1Confidence: float) -> bool:
        if type1Confidence == None or type1Confidence < 0:
            raise ValueError("Cannot have negative or null type1Confidence")
        if type1Confidence > 1:
            raise ValueError("Cannot have a type1Confidence over 1")
        testStat: float = self.getTestStatistic()
        zVal: float = self.normDist.getZPercentileValue(type1Confidence)
        return testStat >= zVal

    def population1LikelihoodLesserTest(self, type1Confidence: float) -> bool:
        if type1Confidence == None or type1Confidence < 0:
            raise ValueError("Cannot have negative or null type1Confidence")
        if type1Confidence > 1:
            raise ValueError("Cannot have a type1Confidence over 1")
        testStat: float = self.getTestStatistic()
        zVal: float = self.normDist.getZPercentileValue(type1Confidence)
        return testStat <= -zVal

    def population1LikelihoodUnequalTest(self, type1Confidence: float) -> bool:
        if type1Confidence == None or type1Confidence < 0:
            raise ValueError("Cannot have negative or null type1Confidence")
        if type1Confidence > 1:
            raise ValueError("Cannot have a type1Confidence over 1")
        testStat: float = self.getTestStatistic()
        alpha: float = (1 - type1Confidence)/2
        zVal: float = self.normDist.getZPercentileValue(1-alpha)
        print(testStat, zVal)
        return abs(testStat) >= zVal
