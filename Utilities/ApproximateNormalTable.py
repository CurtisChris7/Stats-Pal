import math

from Utilities.INormalDistribution import INormalDistribution

class ApproximateNormalTable(INormalDistribution):
    """Class which creates an approximated standard normal table"""

    def __init__(self, 
        step: float = 0.001, 
        precision: int = 3, 
        lowerbound: float = -5.0, 
        upperbound: float = 5.0) -> None:
        """
        Description
        ----------
        Constructor for the ApproximateNormalTable

        Parameters
        ----------
        step: float
            The step size when discretizing the distribution

        precision: int
            The number of decimal places to round to for the values of Z
            NOTE: THIS SHOULD BE CONISTENT WITH THE STEP SIZE

        lowerbound: float
            The left most value of the approximated standard normal distribution

        upperbound: float
            The right most value of the approximated standard normal distribution

        """

        self.step: float = step
        self.precision: int = precision
        self.lowerbound: float = lowerbound
        self.uppperbound: float = upperbound
        self.table: dict = self.__approximateCdf()
        
    @staticmethod
    def pdf(x : float):
        """
        Description
        ----------
        The probability density function applied at a specified value

        Parameters
        ----------
        x : float
            A given point to be evaluated along a standard normal distribution

        Returns
        -------
        float
            The value of the probability density function for that point
        """
        return math.exp(-(x**2) / 2) / (math.sqrt(2) * math.pi)

    def __approximateCdf(self) -> dict:
        """
        Description
        ----------
        Approximates the behaviour of the cumulative density function represented as
        a dictionary

        Returns
        -------
        dict
            The a dictionary of values of z and their right tail cdf value
        """
        lowerbound: float = self.lowerbound
        upperbound: float = self.uppperbound
        step: float = self.step
        cursor: float = lowerbound
        sum: float = 0

        rightTailCdf: dict = {}

        while cursor <= upperbound:
            pdfVal: float = ApproximateNormalTable.pdf(cursor)
            sum += pdfVal

            rightTailCdf[cursor] = sum
            cursor += step
            cursor = round(cursor, self.precision)

        for key in rightTailCdf:
            rightTailCdf[key] /= sum

        return rightTailCdf

    def getRightTailArea(self, val: float) -> float:
        val = round(val, self.precision)
        if val < self.lowerbound:
            return 0
        elif val > self.uppperbound:
            return 1

        return self.table[val]

    def getZValue(self, targetArea: float) -> float:
        if targetArea < self.table[self.lowerbound]:
            return self.lowerbound

        for key in self.table:
            val = self.table[key]
            if val >= targetArea:
                return key

        return self.uppperbound
    