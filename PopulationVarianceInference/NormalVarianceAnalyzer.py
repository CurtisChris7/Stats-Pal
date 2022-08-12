import math

from PopulationVarianceInference.IPopulationVarianceAnalyzer import IPopulationVarianceAnalyzer
from Utilities.ChiSquaredDistribution.IChiSquaredDistribution import IChiSquaredDistribution
from Utilities.ChiSquaredDistribution.SciPyChiSquared import SciPyChiSquared
from Utilities.SampleUtilities import SampleUtilities

class NormalVarianceAnalyzer(IPopulationVarianceAnalyzer):
    """Class representing an analyzer for single dimensional, normally distributed populations"""

    def __init__(self, values: list, chisquare: IChiSquaredDistribution = SciPyChiSquared()) -> None:
        if values == None or len(values) == 0:
            raise ValueError("Cannot have empty or null values")
        if chisquare == None:
            raise ValueError("Cannot have null chisquare")

        self.values: list = values
        self.mean: float = SampleUtilities.estimateMean(values)
        self.variance: float = SampleUtilities.estimateVariance(values)
        self.n: int = len(values)
        self.df: int = self.n - 1
        self.chisquare: IChiSquaredDistribution = chisquare

    def getSampleVariance(self) -> float:
        return self.variance

    def getConfidenceInterval(self, confidenceLevel: float) -> tuple:
        if confidenceLevel == None or confidenceLevel < 0:
            raise ValueError("Cannot have negative or null confidenceLevel")
        if confidenceLevel > 1:
            raise ValueError("Cannot have a confidenceLevel over 1")
        
        chiSquareUpper: float = self.chisquare.getChiSquaredUpperVal(confidenceLevel, self.df)
        chiSquareLower: float = self.chisquare.getChiSquaredLowerVal(confidenceLevel, self.df)
        return (math.sqrt(self.getTestStatistic(chiSquareUpper)), math.sqrt(self.getTestStatistic(chiSquareLower)))

    def getTestStatistic(self, testVariance: float) -> float:
        if testVariance == None:
            raise ValueError("Cannot have a null testVariance")
        return (self.n - 1) * self.variance / testVariance

    def rightTailVarianceSignificanceTest(self, variance: float, confidenceLevel: float) -> bool:
        if confidenceLevel == None or confidenceLevel < 0:
            raise ValueError("Cannot have negative or null confidenceLevel")
        if confidenceLevel > 1:
            raise ValueError("Cannot have a confidenceLevel over 1")
        if variance == None:
            raise ValueError("Cannot a null test variance")
        chiSquareUpper: float = self.chisquare.getChiSquaredUpperVal(confidenceLevel, self.df)
        testStatistic: float = self.getTestStatistic(variance)
        return testStatistic > chiSquareUpper

    def leftTailVarianceSignificanceTest(self, variance: float, confidenceLevel: float) -> bool: 
        if confidenceLevel == None or confidenceLevel < 0:
            raise ValueError("Cannot have negative or null confidenceLevel")
        if confidenceLevel > 1:
            raise ValueError("Cannot have a confidenceLevel over 1")
        if variance == None:
            raise ValueError("Cannot a null test variance")
        chiSquareLower: float = self.chisquare.getChiSquareLowerVal(confidenceLevel, self.df)
        testStatistic: float = self.getTestStatistic(variance)
        return testStatistic < chiSquareLower

    def twinTailVarianceSignificanceTest(self, variance: float, confidenceLevel: float) -> bool:
        if confidenceLevel == None or confidenceLevel < 0:
            raise ValueError("Cannot have negative or null confidenceLevel")
        if confidenceLevel > 1:
            raise ValueError("Cannot have a confidenceLevel over 1")
        if variance == None:
            raise ValueError("Cannot a null test variance")
        chiSquareUpper: float = self.chisquare.getChiSquaredUpperVal(confidenceLevel, self.df)
        chiSquareLower: float = self.chisquare.getChiSquareLowerVal(confidenceLevel, self.df)
        testStatistic: float = self.getTestStatistic(variance)
        return testStatistic > chiSquareUpper or testStatistic < chiSquareLower
