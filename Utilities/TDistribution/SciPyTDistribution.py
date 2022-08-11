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

    def getTValue(self, targetArea: float, df: int) -> float:
        if targetArea == None or targetArea < 0:
            raise ValueError("Cannot pass a negative or null area value")
        if df == None or df < 0:
            raise ValueError("Cannot pass a negative or null df value")
        if targetArea > 1:
            raise ValueError("Target area cannot be greater than one")

        return t.ppf(targetArea, df)
