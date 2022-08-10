from abc import ABC, abstractmethod

class INormalDistribution(ABC):
    """Interface for normal distribution utilities"""

    @abstractmethod
    def getRightTailArea(self, val: float) -> float:
        """
        Description
        ----------
        Finds the right tail area value of a given z value

        Parameters
        ----------
        val : float
            A candidate z value

        Returns
        -------
        float
            The approximate area under the standard normal curve
        """
        pass

    @abstractmethod
    def getZValue(self, targetArea: float) -> float:
        """
        Description
        ----------
        Finds the smallest value of z in the approximated distribution which has
        atleast the target area under the curve

        Parameters
        ----------
        targetArea : float
            The desired area under the standard normal curve

        Returns
        -------
        float
            The corresponding z value for that area under the approximated curves
        """
        pass