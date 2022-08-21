from abc import ABC, abstractmethod

class IPopulationVarianceComparer(ABC):
    """Interface for a potential population variance comparer"""

    @abstractmethod
    def getConfidenceInterval(self, confidenceLevel: float) -> tuple:
        """
        Description
        ----------
        Contructs a confidence interval of the population mean

        Parameters
        ----------
        confidenceLevel : float
            The likelihood of the true mean falling in this interval

        Returns
        -------
        tuple
            The bounds of the interval
        """
        pass

    @abstractmethod
    def getTestStatistic(self) -> float:
        """
        Description
        ----------
        Gets the test statistic 

        Returns
        -------
        float
            the value of the test statistic
        """
        pass

    @abstractmethod
    def population1HasGreaterVarianceTest(self, type1Confidence: float) -> bool:
        """
        Description
        ----------
        Performs a significance test to determine if the first population
        has greater variance

        Parameters
        ----------
        confidenceLevel : float
            The confidence level of the test

        Returns
        -------
        bool
            true if the research hypotheses is accepted, false if rejected
        """
        pass

    @abstractmethod
    def populationsHaveUnequalVarianceTest(self, type1Confidence: float) -> bool:
        """
        Description
        ----------
        Performs a significance test to determine if the two populations 
        have equal variance

        Parameters
        ----------
        confidenceLevel : float
            The confidence level of the test

        Returns
        -------
        bool
            true if the research hypotheses is accepted, false if rejected
        """
        pass
