import math
from termios import VLNEXT

class SampleUtilities:
    """Class for reusable sample measurement methods"""

    @staticmethod
    def estimateMean(values: list) -> float:
        """
        Description
        ----------
        Estimates the mean by taking the average of a list of values

        Parameters
        ----------
        values : list
            A population sample of floating point numbers

        Returns
        -------
        float
            The average of the provided values
        """
        return sum(values) / len(values)

    @staticmethod
    def estimateStdDev(values: list) -> float:
        """
        Description
        ----------
        Estimates the standard deviation of a list of values

        Parameters
        ----------
        values : list
            A population sample of floating point numbers

        Returns
        -------
        float
            The standard deviation of the provided values
        """
        mean: float = SampleUtilities.estimateMean(values)
        n: int = len(list)

        sum = 0
        for item in values:
            sum += (item - mean) ** 2

        return math.sqrt(sum / (n-1))