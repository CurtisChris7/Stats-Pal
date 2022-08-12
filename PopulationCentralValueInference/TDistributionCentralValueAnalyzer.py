import math
from Utilities.TDistribution.ITDistribution import ITDistribution
from Utilities.SampleUtilities import SampleUtilities
from PopulationCentralValueInference.IPopulationCentralValueAnalyzer import IPopulationCentralValueAnalyzer
from Utilities.TDistribution.SciPyTDistribution import SciPyTDistribution

class TDistributionCentralValueAnalyzer(IPopulationCentralValueAnalyzer):
    """Class representing an analyzer for single dimensional population under a student's t distribution"""

    def __init__(self, values: list, tDist: ITDistribution = SciPyTDistribution()) -> None:
        """
        Description
        ----------
        Constructor for the TDistributionCentralValueAnalyzer

        Parameters
        ----------
        values: list
            The list of floats representing a sample from the population distribution

        tDist: ITDistribution
            The t distribution used by the class
        """
        if values == None or len(values) == 0:
            raise ValueError("Cannot have empty or null values")
        if tDist == None:
            raise ValueError("Cannot have null tDist")
        self.values: list = values
        self.mean: float = SampleUtilities.estimateMean(values)
        self.stdDev: float = SampleUtilities.estimateStdDev(values)
        self.n: int = len(values)
        self.df: int = self.n - 1
        self.tDist = tDist

    def getMean(self) -> float:
        return self.mean

    def getConfidenceInterval(self, confidenceLevel: float) -> tuple:
        if confidenceLevel == None or confidenceLevel < 0:
            raise ValueError("Cannot have negative or null confidenceLevel")
        if confidenceLevel > 1:
            raise ValueError("Cannot have a confidenceLevel over 1")

        width: float = self.tDist.getTValue(confidenceLevel + ((1 - confidenceLevel)/2), self.df) * self.stdDev / math.sqrt(self.n)
        return (self.mean - width, self.mean + width)

    def sampleSizeForConfidenceInterval(self, confidenceLevel: float, width: float) -> float:
        return None

    def sampleSizeForTesting(self, type1Confidence: float, type2Confidence: float, delta: float) -> float:
        return None

    """TESTING METHODS FOR RESEARCH HYPOTHESIS"""

    def getTestStatistic(self, nullMean: float) -> float:
        if nullMean == None:
            raise ValueError("Cannot have a null test mean")
        return math.sqrt(self.n) * (self.mean - nullMean) / self.stdDev

    def rightTailMeanSignificanceTest(self, mean: float, type1Confidence: float) -> bool:
        if type1Confidence == None or type1Confidence < 0:
            raise ValueError("Cannot have negative or null type1Confidence")
        if type1Confidence > 1:
            raise ValueError("Cannot have a type1Confidence over 1")
        if mean == None:
            raise ValueError("Cannot a null test mean")

        tVal: float = self.getTestStatistic(mean)
        pVal: float = 1 - self.tDist.getLeftTailArea(tVal, self.df)
        return pVal <= (1-type1Confidence)

    def leftTailMeanSignificanceTest(self, mean: float, type1Confidence: float) -> bool:
        if type1Confidence == None or type1Confidence < 0:
            raise ValueError("Cannot have negative or null type1Confidence")
        if type1Confidence > 1:
            raise ValueError("Cannot have a type1Confidence over 1")
        if mean == None:
            raise ValueError("Cannot a null test mean")

        tVal: float = self.getTestStatistic(mean)
        pVal: float = self.tDist.getLeftTailArea(tVal, self.df)
        return pVal <= (1-type1Confidence)

    def twinTailMeanSignificanceTest(self, mean: float, type1Confidence: float) -> bool:
        if type1Confidence == None or type1Confidence < 0:
            raise ValueError("Cannot have negative or null type1Confidence")
        if type1Confidence > 1:
            raise ValueError("Cannot have a type1Confidence over 1")
        if mean == None:
            raise ValueError("Cannot a null test mean")

        tVal: float = abs(self.getTestStatistic(mean))
        pVal: float = 2 * (1 - self.tDist.getLeftTailArea(tVal, self.df))
        return pVal <= (1-type1Confidence)

    """POWER TESTING METHODS ARE NOT IMPLEMENTED"""

    def getTestPower(self, nullMean: float, confidenceLevel: float) -> float:
        raise NotImplementedError

    def rightTailMeanSignificanceAndPowerTest(self, mean: float, type1Confidence: float, type2Confidence: float) -> tuple:
        raise NotImplementedError

    def leftTailMeanSignificanceAndPowerTest(self, mean: float, type1Confidence: float, type2Confidence: float) -> tuple:
        raise NotImplementedError

    def twinTailMeanSignificanceAndPowerTest(self, mean: float, type1Confidence: float, type2Confidence: float) -> tuple:
        raise NotImplementedError
