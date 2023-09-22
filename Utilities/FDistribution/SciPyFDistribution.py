from scipy.stats import f

from Utilities.FDistribution.IFDistribution import IFDistribution

class SciPyFDistribution(IFDistribution):
    """Class implementing the IFDistribution interface using scipy"""

    def getFPercentileValue(self, percentile: float, df1: int, df2: int) -> float:
        if percentile == None or percentile < 0:
            raise ValueError("Cannot pass a negative or null percentile")
        if percentile > 1:
            raise ValueError("Cannot pass a percentile greater than 1")
        if df1 == None or df1 < 0:
            raise ValueError("Cannot pass a negative or null df1 value")
        if df2 == None or df2 < 0:
            raise ValueError("Cannot pass a negative or null df2 value")

        return f.ppf(percentile, df1, df2)

    def getFLowerValue(self, confidenceLevel: float, df1: int, df2: int) -> float:
        if confidenceLevel == None or confidenceLevel < 0:
            raise ValueError("Cannot pass a negative or null confidenceLevel")
        if confidenceLevel > 1:
            raise ValueError("Cannot pass a confidenceLevel greater than 1")
        if df1 == None or df1 < 0:
            raise ValueError("Cannot pass a negative or null df1 value")
        if df2 == None or df2 < 0:
            raise ValueError("Cannot pass a negative or null df2 value")
        percentile = (1 - confidenceLevel) / 2
        return f.ppf(percentile, df1, df2)

    def getFUpperValue(self, confidenceLevel: float, df1: int, df2: int) -> float:
        if confidenceLevel == None or confidenceLevel < 0:
            raise ValueError("Cannot pass a negative or null confidenceLevel")
        if confidenceLevel > 1:
            raise ValueError("Cannot pass a confidenceLevel greater than 1")
        if df1 == None or df1 < 0:
            raise ValueError("Cannot pass a negative or null df1 value")
        if df2 == None or df2 < 0:
            raise ValueError("Cannot pass a negative or null df2 value")
        percentile = 1 - ((1 - confidenceLevel) / 2)
        return f.ppf(percentile, df1, df2)
