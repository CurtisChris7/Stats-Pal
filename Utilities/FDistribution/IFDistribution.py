from abc import ABC, abstractmethod

class IFDistribution(ABC):
    """Interface for F distribution"""

    @abstractmethod
    def getFPercentileValue(self, percentile: float, df1: int, df2: int) -> float:
        """
        Description
        ----------
        Finds the corresponding value of f in the approximated distribution which
        has the target area under the curve

        Parameters
        ----------
        percentile : float
            The desired area under the curve

        df1: int
            The number of degrees of freedom in population 1

        df2: int
            The number of degrees of freedom in population 2

        Returns
        -------
        float
            The corresponding f value for that area under the approximated curve
        """
        pass

    @abstractmethod
    def getFUpperValue(self, confidenceLevel: float, df1: int, df2: int) -> float:
        """
        Description
        ----------
        Finds the corresponding value of F in the approximated distribution 
        which corresponds to the upper value F test statistic

        Parameters
        ----------
        confidenceLevel : float
            The desired confidence level 

        df1: int
            The number of degrees of freedom in population 1

        df2: int
            The number of degrees of freedom in population 2

        Returns
        -------
        float
            The corresponding F value statistic
        """
        pass

    @abstractmethod
    def getFLowerValue(self, confidenceLevel: float, df1: int, df2: int) -> float:
        """
        Description
        ----------
        Finds the corresponding value of F in the approximated distribution 
        which corresponds to the lower value F test statistic

        Parameters
        ----------
        confidenceLevel : float
            The desired confidence level 

        df1: int
            The number of degrees of freedom in population 1

        df2: int
            The number of degrees of freedom in population 2

        Returns
        -------
        float
            The corresponding F value statistic
        """
        pass