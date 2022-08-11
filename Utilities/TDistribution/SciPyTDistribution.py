from scipy.stats import t

from Utilities.TDistribution.ITDistribution import ITDistribution

class SciPyTDistribution(ITDistribution):
    """Class implementing the ITDistribution interface using scipy"""

    def getLeftTailArea(self, val: float, df: int) -> float:
        return t.cdf(val, df)

    def getTValue(self, targetArea: float, df: int) -> float:
        return t.ppf(targetArea, df)
