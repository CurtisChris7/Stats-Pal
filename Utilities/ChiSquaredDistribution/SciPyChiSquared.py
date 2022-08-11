import math

from scipy.stats import chi
from Utilities.ChiSquaredDistribution.IChiSquaredDistribution import IChiSquaredDistribution

class SciPyChiSquared(IChiSquaredDistribution):
    """Class implementing the IChiSquaredDistribution interface using scipy"""

    def getLeftTailArea(self, chiVal: float, df: int):
        return chi.cdf(math.sqrt(chiVal), df)

    def getChiSquaredVal(self, targetArea: float, df: int) -> float:
        return chi.ppf(targetArea, df)**2

    def getChiSquaredUpperVal(self, confidenceLevel: float, df: int) -> float:
        alpha: float = (1 - confidenceLevel)/2
        return self.getChiSquaredVal(1 - alpha, df)

    def getChiSquaredLowerVal(self, confidenceLevel: float, df: int) -> float:
        alpha: float = (1 - confidenceLevel)/2
        return self.getChiSquaredVal(alpha, df)
