import math
from Utilities.SampleUtilities import SampleUtilities
from PopulationCentralValueInference.IPopulationCentralValueAnalyzer import IPopulationCentralValueAnalyzer

class BootstrappedCentralValueAnalyzer(IPopulationCentralValueAnalyzer):
    """Class representing an analyzer for single dimensional population under a student's t distribution"""

    def __init__(self, values: list, resampleCount: int = 10000) -> None:
        """
        Description
        ----------
        Constructor for the TDistributionCentralValueAnalyzer

        Parameters
        ----------
        values: list
            The list of floats representing a sample from the population distribution
        """
        if values == None or len(values) == 0:
            raise ValueError("Cannot have empty or null values")
        if resampleCount == None or resampleCount < 0:
            raise ValueError("Cannot have negative or null resampleCount")
        
        self.values = values
        self.mean: float = SampleUtilities.estimateMean(values)
        self.stdDev: float = SampleUtilities.estimateStdDev(values)
        self.n = len(values)
        self.resampleCount = resampleCount

    def getMean(self) -> float:
        return self.mean

    def __getBootstrapTestStatistic(self, approxMean: float, approxStdDev: float) -> float:
        return math.sqrt(self.n) * (approxMean - self.mean) / approxStdDev

    def __getBootstrapWidth(self, values: list, percentile: float) -> float:
        return values[int(self.resampleCount * percentile)] * self.stdDev / math.sqrt(self.n)

    def __getBoostrapSamples(self) -> list:
        testStatistics: list = []
        for _ in range(self.resampleCount):
            newSample: list = SampleUtilities.bootstrap(self.values)
            newMean: float = SampleUtilities.estimateMean(newSample)
            newStdDev: float = SampleUtilities.estimateStdDev(newSample)
            testStatistics.append(self.__getBootstrapTestStatistic(newMean, newStdDev))
        return testStatistics

    def getConfidenceInterval(self, confidenceLevel: float) -> tuple:
        if confidenceLevel == None or confidenceLevel < 0:
            raise ValueError("Cannot have negative or null confidenceLevel")
        if confidenceLevel > 1:
            raise ValueError("Cannot have a confidenceLevel over 1")
        
        testStatistics: list = self.__getBoostrapSamples()
        testStatistics.sort()

        alpha: float = (1 - confidenceLevel)/2
        return (self.mean - self.__getBootstrapWidth(testStatistics, 1-alpha), self.mean - self.__getBootstrapWidth(testStatistics, alpha))

    def sampleSizeForConfidenceInterval(self, confidenceLevel: float, width: float) -> float:
        return None

    def sampleSizeForTesting(self, type1Confidence: float, type2Confidence: float, delta: float) -> float:
        return None

    """TESTING METHODS FOR RESEARCH HYPOTHESIS"""

    def getTestStatistic(self, nullMean: float) -> float:
        if nullMean == None:
            raise ValueError("Cannot have negative or null nullMean")

        return math.sqrt(self.n) * (self.mean - nullMean) / self.stdDev

    def rightTailMeanSignificanceTest(self, mean: float, type1Confidence: float) -> bool:
        if type1Confidence == None or type1Confidence < 0:
            raise ValueError("Cannot have negative or null type1Confidence")
        if type1Confidence > 1:
            raise ValueError("Cannot have a type1Confidence over 1")
        if mean == None:
            raise ValueError("Cannot a null test mean")

        tVal: float = self.getTestStatistic(mean)
        testStatistics: list = self.__getBoostrapSamples()

        cntr: int = 0
        for val in testStatistics:
            if val >= tVal:
                cntr += 1
        pVal = cntr / self.resampleCount
        return pVal <= (1-type1Confidence)

    def leftTailMeanSignificanceTest(self, mean: float, type1Confidence: float) -> bool:
        if type1Confidence == None or type1Confidence < 0:
            raise ValueError("Cannot have negative or null type1Confidence")
        if type1Confidence > 1:
            raise ValueError("Cannot have a type1Confidence over 1")
        if mean == None:
            raise ValueError("Cannot a null test mean")

        tVal: float = self.getTestStatistic(mean)
        testStatistics: list = self.__getBoostrapSamples()

        cntr: int = 0
        for val in testStatistics:
            if val <= tVal:
                cntr += 1
        pVal = cntr / self.resampleCount
        return pVal <= (1-type1Confidence)

    def twinTailMeanSignificanceTest(self, mean: float, type1Confidence: float) -> bool:
        if type1Confidence == None or type1Confidence < 0:
            raise ValueError("Cannot have negative or null type1Confidence")
        if type1Confidence > 1:
            raise ValueError("Cannot have a type1Confidence over 1")
        if mean == None:
            raise ValueError("Cannot a null test mean")

        tVal: float = self.getTestStatistic(mean)
        testStatistics: list = self.__getBoostrapSamples()

        lowerCntr: int = 0
        greaterCntr: int = 0
        for val in testStatistics:
            if val >= tVal:
                greaterCntr += 1
            elif val <= tVal:
                lowerCntr += 1
        
        pVal = 2 * min(lowerCntr, greaterCntr) / self.resampleCount
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