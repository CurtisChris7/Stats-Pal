import math

from scipy.stats import chi
from Utilities.ChiSquaredDistribution.IChiSquaredDistribution import IChiSquaredDistribution

class SciPyChiSquared(IChiSquaredDistribution):
    """Class implementing the IChiSquaredDistribution interface using scipy"""

    def getLeftTailArea(self, chiVal: float, df: int):
        if chiVal == None:
            raise ValueError("Cannot pass a null t value")
        if df == None or df < 0:
            raise ValueError("Cannot pass a negative or null df value")
        return chi.cdf(math.sqrt(chiVal), df)

    def getChiSquaredPercentileVal(self, percentile: float, df: int) -> float:
        if percentile == None or percentile < 0:
            raise ValueError("Cannot pass a negative or null percentile")
        if df == None or df < 0:
            raise ValueError("Cannot pass a negative or null df value")
        if percentile > 1:
            raise ValueError("Target area cannot be greater than one")
        return chi.ppf(percentile, df)**2

    def getChiSquaredUpperVal(self, confidenceLevel: float, df: int) -> float:
        if df == None or df < 0:
            raise ValueError("Cannot pass a negative or null df value")
        if confidenceLevel == None or confidenceLevel < 0:
            raise ValueError("Cannot have negative or null confidenceLevel")
        if confidenceLevel > 1:
            raise ValueError("Cannot have a confidenceLevel over 1")
        alpha: float = (1 - confidenceLevel)/2
        return self.getChiSquaredPercentileVal(1 - alpha, df)

    def getChiSquaredLowerVal(self, confidenceLevel: float, df: int) -> float:
        if df == None or df < 0:
            raise ValueError("Cannot pass a negative or null df value")
        if confidenceLevel == None or confidenceLevel < 0:
            raise ValueError("Cannot have negative or null confidenceLevel")
        if confidenceLevel > 1:
            raise ValueError("Cannot have a confidenceLevel over 1")
        alpha: float = (1 - confidenceLevel)/2
        return self.getChiSquaredPercentileVal(alpha, df)
