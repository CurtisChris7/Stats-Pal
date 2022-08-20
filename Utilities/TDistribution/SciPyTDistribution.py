from scipy.stats import t

from Utilities.TDistribution.ITDistribution import ITDistribution

class SciPyTDistribution(ITDistribution):
    """Class implementing the ITDistribution interface using scipy"""

    def getLeftTailArea(self, val: float, df: int) -> float:
        if val == None:
            raise ValueError("Cannot pass a null t value")
        if df == None or df < 0:
            raise ValueError("Cannot pass a negative or null df value")
        
        return t.cdf(val, df)

    def getTPercentileValue(self, percentile: float, df: int) -> float:
        if percentile == None or percentile < 0:
            raise ValueError("Cannot pass a negative or null percentile")
        if df == None or df < 0:
            raise ValueError("Cannot pass a negative or null df value")
        if percentile > 1:
            raise ValueError("Target area cannot be greater than one")

        return t.ppf(percentile, df)
