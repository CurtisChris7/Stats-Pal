import math
from CategoricalPopulationInference.IBinomialPopulationAnalyzer import IBinomialPopulationAnalyzer
from Utilities.BinomialDistribution.BinomialDistribution import BinomialDistribution
from Utilities.BinomialDistribution.IBinomialDistribution import IBinomialDistribution
from Utilities.CategoricalSampleUtilities import CategoricalSampleUtilities
from Utilities.NormalDistriution.ApproximateNormalTable import ApproximateNormalTable
from Utilities.NormalDistriution.INormalDistribution import INormalDistribution

class NormalBinomialAnalyzer(IBinomialPopulationAnalyzer):
    """Class representing an analyzer for normally distribution populations with binary categorical data"""

    def __init__(self, 
        values: list, 
        binomialDist: IBinomialDistribution = BinomialDistribution(),
        normalDist: INormalDistribution = ApproximateNormalTable()) -> None:
        """
        Description
        ----------
        Constructor for the NormalCentralValueAnalyzer

        Parameters
        ----------
        values: list
            The list of floats representing a sample from the population distribution

        binomialDist: IBinomialDistribution
            Binomial distribution utility

        normalDist: INormalDistribution
            Normal distribution utility
        """
        if values == None or len(values) == 0:
            raise ValueError("Cannot have empty or null values")
        if binomialDist == None:
            raise ValueError("Cannot have null binomialDist")
        if normalDist == None:
            raise ValueError("Cannot have null normalDist")
        
        self.values: list = values
        self.binomialDist: IBinomialDistribution = binomialDist
        self.normalDist: INormalDistribution = normalDist
        self.likelihood = CategoricalSampleUtilities.estimateLikelihood(values)
        self.standardError = CategoricalSampleUtilities.estimateStandardError(values)
        self.n = len(values)

    def getSampleLikelihood(self) -> float:
        return self.likelihood

    def getSampleStandardError(self) -> float:
        return self.standardError

    def getConfidenceInterval(self, confidenceLevel: float) -> tuple:
        if confidenceLevel == None or confidenceLevel < 0:
            raise ValueError("Cannot have negative or null confidenceLevel")
        if confidenceLevel > 1:
            raise ValueError("Cannot have a confidenceLevel over 1")

        alpha: float = (1 - confidenceLevel) / 2

        if self.likelihood == 0:
            return (0, 1 - math.pow((alpha/2), 1/self.n))
        if self.likelihood == 1:
            return (math.pow((alpha/2), 1/self.n), 1)

        zSquaredVal: float = (self.normalDist.getZPercentileValue(1 - alpha) ** 2)

        newSuccessCount: float = (self.likelihood * self.n ) + (0.5 * zSquaredVal)
        newN: float = self.n + zSquaredVal
        newLikelihood: float = newSuccessCount / newN

        width: float = math.sqrt(zSquaredVal) * math.sqrt( newLikelihood * (1 - newLikelihood) / newN)

        return (newLikelihood - width, newLikelihood + width)

    def sampleSizeForConfidenceInterval(self, confidenceLevel: float, width: float) -> int:
        if confidenceLevel == None or confidenceLevel < 0:
            raise ValueError("Cannot have negative or null confidenceLevel")
        if confidenceLevel > 1:
            raise ValueError("Cannot have a confidenceLevel over 1")
        if width == None or width < 0:
            raise ValueError("Cannot have negative or null width")

        alpha: float = (1 - confidenceLevel) / 2
        return (self.normalDist.getZPercentileValue(1 - alpha) ** 2) * self.likelihood * (1 - self.likelihood) / (width ** 2)

    def getTestStatistic(self, testLikelihood: float) -> float:
        if testLikelihood == None or testLikelihood < 0:
            raise ValueError("Cannot have negative or null testLikelihood")
        if testLikelihood > 1:
            raise ValueError("Cannot have a testLikelihood over 1")

        return (self.likelihood - testLikelihood) / self.standardError

    def rightTailtLikelihoodSignificanceTest(self, testLikelihood: float, confidenceLevel: float) -> bool:
        if confidenceLevel == None or confidenceLevel < 0:
            raise ValueError("Cannot have negative or null confidenceLevel")
        if confidenceLevel > 1:
            raise ValueError("Cannot have a confidenceLevel over 1")
        if testLikelihood == None or testLikelihood < 0:
            raise ValueError("Cannot have negative or null testLikelihood")
        if testLikelihood > 1:
            raise ValueError("Cannot have a testLikelihood over 1")

        expectedSuccess: int = math.floor(testLikelihood * self.n)
        pVal: float = 1 - self.binomialDist.getLeftTailArea(expectedSuccess, self.n, testLikelihood)
        return pVal <= 1 - confidenceLevel

    def leftTailLikelihoodSignificanceTest(self, testLikelihood: float, confidenceLevel: float) -> bool:
        if confidenceLevel == None or confidenceLevel < 0:
            raise ValueError("Cannot have negative or null confidenceLevel")
        if confidenceLevel > 1:
            raise ValueError("Cannot have a confidenceLevel over 1")
        if testLikelihood == None or testLikelihood < 0:
            raise ValueError("Cannot have negative or null testLikelihood")
        if testLikelihood > 1:
            raise ValueError("Cannot have a testLikelihood over 1")

        expectedSuccess: int = math.floor(testLikelihood * self.n)
        pVal: float = self.binomialDist.getLeftTailArea(expectedSuccess, self.n, testLikelihood)
        return pVal <= 1 - confidenceLevel

    def twinTailLikelihoodSignificanceTest(self, testLikelihood: float, confidenceLevel: float) -> bool:
        if confidenceLevel == None or confidenceLevel < 0:
            raise ValueError("Cannot have negative or null confidenceLevel")
        if confidenceLevel > 1:
            raise ValueError("Cannot have a confidenceLevel over 1")
        if testLikelihood == None or testLikelihood < 0:
            raise ValueError("Cannot have negative or null testLikelihood")
        if testLikelihood > 1:
            raise ValueError("Cannot have a testLikelihood over 1")
            
        expectedSuccess: int = math.floor(testLikelihood * self.n)
        if self.likelihood >= testLikelihood:
            pVal: float = 2 * (1 - self.binomialDist.getLeftTailArea(expectedSuccess, self.n, testLikelihood))
            return pVal <= 1 - confidenceLevel
        else:
            pVal: float = 2 * self.binomialDist.getLeftTailArea(expectedSuccess, self.n, testLikelihood)
            return pVal <= 1 - confidenceLevel
