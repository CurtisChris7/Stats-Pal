from abc import ABC, abstractmethod

class IChiSquaredDistribution(ABC):
    """Interface for Chi Squared distribution"""

    @abstractmethod
    def getChiSquaredPercentileVal(self, percentile: float, df: int) -> float:
        """
        Description
        ----------
        Finds the corresponding value of chi squared in the approximated 
        distribution which has the target area under the curve

        Parameters
        ----------
        percentile : float
            The desired area under the curve

        df: int
            The number of degrees of freedom

        Returns
        -------
        float
            The corresponding chi squared value for that area under the approximated curve
        """
        pass

    @abstractmethod
    def getChiSquaredUpperVal(self, confidenceLevel: float, df: int) -> float:
        """
        Description
        ----------
        Finds the corresponding value of chi squared in the approximated distribution 
        which corresponds to the upper value chi squared test statistic

        Parameters
        ----------
        confidenceLevel : float
            The desired confidence level 

        df: int
            The number of degrees of freedom

        Returns
        -------
        float
            The corresponding chi squared value statistic
        """
        pass

    @abstractmethod
    def getChiSquaredLowerVal(self, confidenceLevel: float, df: int) -> float:
        """
        Description
        ----------
        Finds the corresponding value of chi squared in the approximated distribution 
        which corresponds to the lower value chi squared test statistic

        Parameters
        ----------
        confidenceLevel : float
            The desired confidence level 

        df: int
            The number of degrees of freedom

        Returns
        -------
        float
            The corresponding chi squared value statistic
        """
        pass

    @abstractmethod
    def getLeftTailArea(self, val: float, df: int) -> float:
        """
        Description
        ----------
        Finds the left tail area value of a given chi squared value and degrees of freedom

        Parameters
        ----------
        val : float
            A candidate chi-squared value

        df: int
            The number of degrees of freedom

        Returns
        -------
        float
            The approximate area under the appropriate t distribution
        """
        pass
