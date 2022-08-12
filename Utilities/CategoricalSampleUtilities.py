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
        if values == None or len(values) == 0:
            raise ValueError("Cannot have empty or null sample")
        cntr: int = 0
        for item in values:
            if item != 0 and item != 1:
                raise ValueError("All elements must be either 0 or 1")
            cntr += item
        
        return cntr / len(values)

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
        if values == None or len(values) == 0:
            raise ValueError("Cannot have empty or null sample")
        likelihood: float = CategoricalSampleUtilities.estimateLikelihood(values)
        return math.sqrt( (likelihood * (1 - likelihood)) / len(values) )