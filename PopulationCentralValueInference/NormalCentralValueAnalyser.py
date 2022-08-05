import math
from IPopulationCentralValueAnalyser import IPopulationCentralValueAnalyser
from ..Utilities.SampleUtilities import SampleUtilities
from ..Utilities.ApproximateNormalTable import ApproximateNormalTable

class NormalCentralValueAnalyzer(IPopulationCentralValueAnalyser):
    """Class representing an analyzer for single dimensional, normally distributed populations"""

    def __init__(self, values: list) -> None:
        self.sample: list = values
        self.mean: float = SampleUtilities.estimateMean(values)
        self.stdDev: float = SampleUtilities.estimateStdDev(values)
        self.n: int = len(values)
        self.normalTable: ApproximateNormalTable = ApproximateNormalTable()

    def getMean(self) -> float:
        return self.mean

    def getConfidenceInterval(self, confidenceLevel: float) -> tuple:
        zVal: float = self.normalTable.getZValue(1 - ((1-confidenceLevel)/2))
        width: float = zVal * self.stdDev / math.sqrt(self.n)
        return (self.mean - width, self.mean + width)

    def sampleSizeForTesting(self, type1Confidence: float, type2Confidence: float, delta: float) -> float:
        type1ZVal: float = self.normalTable.getZValue(1 - ((1-type1Confidence)/2))
        type2ZVal: float = self.normalTable.getZValue(1 - (1 - type2Confidence))
        return self.n * (self.stdDev ** 2) * ((type1ZVal + type2ZVal) ** 2) / (delta ** 2)

    def sampleSizeForConfidenceInterval(self, confidenceLevel: float, width: float) -> float:
        zVal: float = self.normalTable.getZValue(1 - ((1-confidenceLevel)/2))
        e: float = width / 2
        return self.n * (zVal**2) * (self.stdDev**2) / (e**2)

    """TESTING METHODS FOR RESEARCH HYPOTHESIS"""

    def __getTestStatistic(self, testMean: float) -> float:
        return math.sqrt(self.n) * (self.mean - testMean) / self.stdDev

    def rightTailMeanSignificanceTest(self, mean: float, type1Confidence: float) -> bool:
        zVal: float = self.__getTestStatistic(mean)
        pVal: float = 1 - self.normalTable.getRightTailArea(zVal)
        return pVal <= type1Confidence

    def leftTailMeanSignificanceTest(self, mean: float, type1Confidence: float) -> bool:
        zVal: float = self.__getTestStatistic(mean)
        pVal: float = self.normalTable.getRightTailArea(zVal)
        return pVal <= type1Confidence

    def twinTailMeanSignificanceTest(self, mean: float, type1Confidence: float) -> bool:
        zVal: float = self.__getTestStatistic(mean)
        pVal: float = 2 * (1 - abs(self.normalTable.getRightTailArea(zVal)))
        return pVal <= type1Confidence

    """TESTING METHODS FOR BOTH THE NULL AND RESEARCH HYPOTHESIS"""

    def __getTestPower(self, nullMean: float, confidenceLevel: float) -> float:
        zVal: float = self.normalTable.getZValue(confidenceLevel)
        betaVal: float = zVal - ( math.sqrt(self.n) * abs(nullMean - self.mean) / self.stdDev)
        return 1 - betaVal

    def rightTailMeanSignificanceTest(self, mean: float, type1Confidence: float, type2Confidence: float) -> tuple:
        rejectNull: bool = self.rightTailMeanSignificanceTest(mean, type1Confidence)
        if (rejectNull):
            return (False, True)
        else:
            return (True if self.__getTestPower(mean, type1Confidence) >= type2Confidence else False, False )

    def leftTailMeanSignificanceTest(self, mean: float, type1Confidence: float, type2Confidence: float) -> tuple:
        rejectNull: bool = self.leftTailMeanSignificanceTest(mean, type1Confidence)
        if (rejectNull):
            return (False, True)
        else:
            return (True if self.__getTestPower(mean, type1Confidence) >= type2Confidence else False, False )

    def twinTailMeanSignificanceTest(self, mean: float, type1Confidence: float, type2Confidence: float) -> tuple:
        rejectNull: bool = self.twinTailMeanSignificanceTest(mean, type1Confidence)
        if (rejectNull):
            return (False, True)
        else:
            return (True if self.__getTestPower(mean, type1Confidence + ((1 - type1Confidence)/2)) >= type2Confidence else False, False )
