from abc import ABC, abstractmethod

class ITDistribution(ABC):
    """Interface for student's t distribution"""

    @abstractmethod
    def getLeftTailArea(self, val: float, df: float) -> float:
        """
        Description
        ----------
        Finds the left tail area value of a given t value and degrees of freedom

        Parameters
        ----------
        val : float
            A candidate t value

        df: float
            The number of degrees of freedom

        Returns
        -------
        float
            The approximate area under the appropriate t distribution
        """
        pass

    @abstractmethod
    def getTPercentileValue(self, percentile: float, df: float) -> float:
        """
        Description
        ----------
        Finds the corresponding value of t in the approximated distribution which
        has the target area under the curve

        Parameters
        ----------
        percentile : float
            The desired area under the curve

        df: float
            The number of degrees of freedom

        Returns
        -------
        float
            The corresponding t value for that area under the approximated curve
        """
        pass
