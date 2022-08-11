from abc import ABC, abstractmethod

class IPopulationVarianceAnalyzer(ABC):
    """Interface for potential population variance analyser"""

    @abstractmethod
    def getSampleVariance(self) -> float:
        """
        Description
        ----------
        Returns the variance of the population

        Returns
        -------
        float
            The variance of the population
        """
        pass

    @abstractmethod
    def getConfidenceInterval(self, confidenceLevel: float) -> tuple:
        """
        Description
        ----------
        Contructs a confidence interval of the population variance

        Parameters
        ----------
        confidenceLevel : float
            The likelihood of the true variance falling in this interval

        Returns
        -------
        tuple
            The bounds of the interval
        """
        pass

    @abstractmethod
    def getTestStatistic(self, testVariance: float) -> float:
        """
        Description
        ----------
        Gets the test statistic 

        Parameters
        ----------
        testVariance : float
            The variance value tested against in the null hypothesis

        Returns
        -------
        float
            the value of the test statistic
        """
        pass

    @abstractmethod
    def rightTailVarianceSignificanceTest(self, variance: float, confidenceLevel: float) -> bool:
        """
        Description
        ----------
        Performs a right tail level of significance test to determine if the research
        hypotheses is accepted or not

        Parameters
        ----------
        variance : float
            The variance value tested against in the null hypothesis

        confidenceLevel : float
            The confidence level of the test

        Returns
        -------
        bool
            true if the research hypotheses is accepted, false if rejected
        """
        pass

    @abstractmethod
    def leftTailVarianceSignificanceTest(self, variance: float, confidenceLevel: float) -> bool:
        """
        Description
        ----------
        Performs a left tail level of significance test to determine if the research
        hypotheses is accepted or not

        Parameters
        ----------
        variance : float
            The variance value tested against in the null hypothesis

        confidenceLevel : float
            The confidence level of the test

        Returns
        -------
        bool
            true if the research hypotheses is accepted, false if rejected
        """
        pass

    @abstractmethod
    def twinTailVarianceSignificanceTest(self, variance: float, confidenceLevel: float) -> bool:
        """
        Description
        ----------
        Performs a twin tail level of significance test to determine if the research
        hypotheses is accepted or not

        Parameters
        ----------
        variance : float
            The variance value tested against in the null hypothesis

        confidenceLevel : float
            The confidence level of the test

        Returns
        -------
        bool
            true if the research hypotheses is accepted, false if rejected
        """
        pass
