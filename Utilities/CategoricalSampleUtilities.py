import math

class CategoricalSampleUtilities:
    """Class for reusable sample measurement methods"""

    @staticmethod
    def estimateLikelihood(values: list) -> float:
        """
        Description
        ----------
        Estimates the likelihood of a positive class occuring

        Parameters
        ----------
        values : list
            A population sample of 1's and 0's with 1's denoting the positive class

        Returns
        -------
        float
            The number of 1's over the total
        """
        return sum(values) / len(values)

    @staticmethod
    def estimateStandardError(values: list) -> float:
        """
        Description
        ----------
        Estimates the standard error of the likelihood of positive classes occuring

        Parameters
        ----------
        values : list
            A population sample of 1's and 0's with 1's denoting the positive class

        Returns
        -------
        float
            The variance of the provided values
        """
        likelihood: float = CategoricalSampleUtilities.estimateLikelihood(values)
        return math.sqrt( (likelihood * (1 - likelihood)) / len(values) )