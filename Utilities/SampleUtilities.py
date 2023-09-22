import math
import random

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
        if values == None or len(values) == 0:
            raise ValueError("Cannot have empty or null sample")
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
        if values == None or len(values) == 0:
            raise ValueError("Cannot have empty or null sample")
        if len(values) == 1:
            raise ValueError("Cannot calculate standard deviation of 1 element")
        return math.sqrt(SampleUtilities.estimateVariance(values))

    @staticmethod
    def estimateVariance(values: list) -> float:
        """
        Description
        ----------
        Estimates the variance of a list of values

        Parameters
        ----------
        values : list
            A population sample of floating point numbers

        Returns
        -------
        float
            The variance of the provided values
        """
        if values == None or len(values) == 0:
            raise ValueError("Cannot have empty or null sample")
        if len(values) == 1:
            raise ValueError("Cannot calculate variance of 1 element")

        mean: float = SampleUtilities.estimateMean(values)
        n: int = len(values)

        sum: float = 0
        for item in values:
            sum += (item - mean) ** 2

        return sum / (n-1)

    @staticmethod
    def bootstrap(values: list) -> list:
        """
        Description
        ----------
        Performs a single resampling with replacement from a sample

        Parameters
        ----------
        values : list
            A population sample of floating point numbers

        Returns
        -------
        list
            The standard deviation of the provided values
        """
        if values == None or len(values) == 0:
            raise ValueError("Cannot have empty or null sample")
            
        return random.choices(values, k=len(values))
