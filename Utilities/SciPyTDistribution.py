from scipy.stats import t

from Utilities.ITDistribution import ITDistribution

class SciPyTDistribution(ITDistribution):
    """Class implementing the ITDistribution interface using scipy"""

    def getRightTailArea(self, val: float, df: int) -> float:
        return t.cdf(val, df)

    def getTValue(self, targetArea: float, df: int) -> float:
        return t.ppf(targetArea, df)