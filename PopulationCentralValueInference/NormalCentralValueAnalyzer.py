import math
from PopulationCentralValueInference.IPopulationCentralValueAnalyzer import IPopulationCentralValueAnalyzer
from Utilities.NormalDistriution.INormalDistribution import INormalDistribution
from Utilities.SampleUtilities import SampleUtilities
from Utilities.NormalDistriution.ApproximateNormalTable import ApproximateNormalTable

class NormalCentralValueAnalyzer(IPopulationCentralValueAnalyzer):
    """Class representing an analyzer for single dimensional, normally distributed populations"""

    def __init__(self, values: list, normalDist: INormalDistribution = ApproximateNormalTable())  -> None:
        """
        Description
        ----------
        Constructor for the NormalCentralValueAnalyzer

        Parameters
        ----------
        values: list
            The list of floats representing a sample from the population distribution

        normalDist: INormalDistribution
            Normal distribution utility
        """
        if values == None or len(values) == 0:
            raise ValueError("Cannot have empty or null values")
        if normalDist == None:
            raise ValueError("Cannot have null normalDist")

        self.sample: list = values
        self.mean: float = SampleUtilities.estimateMean(values)
        self.stdDev: float = SampleUtilities.estimateStdDev(values)
        self.n: int = len(values)
        self.normalTable: INormalDistribution = normalDist

    def getMean(self) -> float:
        return self.mean

    def getConfidenceInterval(self, confidenceLevel: float) -> tuple:
        if confidenceLevel == None or confidenceLevel < 0:
            raise ValueError("Cannot have negative or null confidenceLevel")
        if confidenceLevel > 1:
            raise ValueError("Cannot have a confidenceLevel over 1")

        zVal: float = self.normalTable.getZValue(1 - ((1-confidenceLevel)/2))
        width: float = zVal * self.stdDev / math.sqrt(self.n)
        return (self.mean - width, self.mean + width)

    def sampleSizeForTesting(self, type1Confidence: float, type2Confidence: float, delta: float) -> float:
        if type1Confidence == None or type1Confidence < 0:
            raise ValueError("Cannot have negative or null type1Confidence")
        if type1Confidence > 1:
            raise ValueError("Cannot have a type1Confidence over 1")
        if type2Confidence == None or type2Confidence < 0:
            raise ValueError("Cannot have negative or null type2Confidence")
        if type2Confidence > 1:
            raise ValueError("Cannot have a type2Confidence over 1")
        if delta == None:
            raise ValueError("Cannot have null delta")

        type1ZVal: float = self.normalTable.getZValue(1 - ((1-type1Confidence)/2))
        type2ZVal: float = self.normalTable.getZValue(1 - (1 - type2Confidence))
        return self.n * (self.stdDev ** 2) * ((type1ZVal + type2ZVal) ** 2) / (delta ** 2)

    def sampleSizeForConfidenceInterval(self, confidenceLevel: float, width: float) -> float:
        if confidenceLevel == None or confidenceLevel < 0:
            raise ValueError("Cannot have negative or null confidenceLevel")
        if confidenceLevel > 1:
            raise ValueError("Cannot have a confidenceLevel over 1")
        if width == None or width < 0:
            raise ValueError("Cannot have negative or null width")

        zVal: float = self.normalTable.getZValue(1 - ((1-confidenceLevel)/2))
        e: float = width / 2
        return self.n * (zVal**2) * (self.stdDev**2) / (e**2)

    """TESTING METHODS FOR RESEARCH HYPOTHESIS"""

    def getTestStatistic(self, testMean: float) -> float:
        if testMean == None:
            raise ValueError("Cannot have a null test mean")
        return math.sqrt(self.n) * (self.mean - testMean) / self.stdDev

    def rightTailMeanSignificanceTest(self, mean: float, type1Confidence: float) -> bool:
        if type1Confidence == None or type1Confidence < 0:
            raise ValueError("Cannot have negative or null type1Confidence")
        if type1Confidence > 1:
            raise ValueError("Cannot have a type1Confidence over 1")
        if mean == None:
            raise ValueError("Cannot a null test mean")

        zVal: float = self.getTestStatistic(mean)
        pVal: float = 1 - self.normalTable.getLeftTailArea(zVal)
        return pVal <= (1-type1Confidence)

    def leftTailMeanSignificanceTest(self, mean: float, type1Confidence: float) -> bool:
        if type1Confidence == None or type1Confidence < 0:
            raise ValueError("Cannot have negative or null type1Confidence")
        if type1Confidence > 1:
            raise ValueError("Cannot have a type1Confidence over 1")
        if mean == None:
            raise ValueError("Cannot a null test mean")

        zVal: float = self.getTestStatistic(mean)
        pVal: float = self.normalTable.getLeftTailArea(zVal)
        return pVal <= (1-type1Confidence)

    def twinTailMeanSignificanceTest(self, mean: float, type1Confidence: float) -> bool:
        if type1Confidence == None or type1Confidence < 0:
            raise ValueError("Cannot have negative or null type1Confidence")
        if type1Confidence > 1:
            raise ValueError("Cannot have a type1Confidence over 1")
        if mean == None:
            raise ValueError("Cannot a null test mean")

        zVal: float = abs(self.getTestStatistic(mean))
        pVal: float = 2 * (1 - self.normalTable.getLeftTailArea(zVal))
        return pVal <= (1-type1Confidence)

    """TESTING METHODS FOR BOTH THE NULL AND RESEARCH HYPOTHESIS"""

    def getTestPower(self, mean: float, type1Confidence: float) -> float:
        if type1Confidence == None or type1Confidence < 0:
            raise ValueError("Cannot have negative or null type1Confidence")
        if type1Confidence > 1:
            raise ValueError("Cannot have a type1Confidence over 1")
        if mean == None:
            raise ValueError("Cannot a null test mean")

        zVal: float = self.normalTable.getZValue(type1Confidence)
        betaVal: float = zVal - ( math.sqrt(self.n) * abs(mean - self.mean) / self.stdDev)
        return 1 - self.normalTable.getLeftTailArea(betaVal)

    def rightTailMeanSignificanceAndPowerTest(self, mean: float, type1Confidence: float, type2Confidence: float) -> tuple:
        if type1Confidence == None or type1Confidence < 0:
            raise ValueError("Cannot have negative or null type1Confidence")
        if type1Confidence > 1:
            raise ValueError("Cannot have a type1Confidence over 1")
        if type2Confidence == None or type2Confidence < 0:
            raise ValueError("Cannot have negative or null type2Confidence")
        if type2Confidence > 1:
            raise ValueError("Cannot have a type2Confidence over 1")
        if mean == None:
            raise ValueError("Cannot a null test mean")

        rejectNull: bool = self.rightTailMeanSignificanceTest(mean, type1Confidence)
        if (rejectNull):
            return (False, True)
        else:
            return (True if self.getTestPower(mean, type1Confidence) >= type2Confidence else False, False )

    def leftTailMeanSignificanceAndPowerTest(self, mean: float, type1Confidence: float, type2Confidence: float) -> tuple:
        if type1Confidence == None or type1Confidence < 0:
            raise ValueError("Cannot have negative or null type1Confidence")
        if type1Confidence > 1:
            raise ValueError("Cannot have a type1Confidence over 1")
        if type2Confidence == None or type2Confidence < 0:
            raise ValueError("Cannot have negative or null type2Confidence")
        if type2Confidence > 1:
            raise ValueError("Cannot have a type2Confidence over 1")
        if mean == None:
            raise ValueError("Cannot a null test mean")

        rejectNull: bool = self.leftTailMeanSignificanceTest(mean, type1Confidence)
        if (rejectNull):
            return (False, True)
        else:
            return (True if self.getTestPower(mean, type1Confidence) >= type2Confidence else False, False )

    def twinTailMeanSignificanceAndPowerTest(self, mean: float, type1Confidence: float, type2Confidence: float) -> tuple:
        if type1Confidence == None or type1Confidence < 0:
            raise ValueError("Cannot have negative or null type1Confidence")
        if type1Confidence > 1:
            raise ValueError("Cannot have a type1Confidence over 1")
        if type2Confidence == None or type2Confidence < 0:
            raise ValueError("Cannot have negative or null type2Confidence")
        if type2Confidence > 1:
            raise ValueError("Cannot have a type2Confidence over 1")
        if mean == None:
            raise ValueError("Cannot a null test mean")

        rejectNull: bool = self.twinTailMeanSignificanceTest(mean, type1Confidence)
        if (rejectNull):
            return (False, True)
        else:
            return (True if self.getTestPower(mean, type1Confidence + ((1 - type1Confidence)/2)) >= type2Confidence else False, False )
