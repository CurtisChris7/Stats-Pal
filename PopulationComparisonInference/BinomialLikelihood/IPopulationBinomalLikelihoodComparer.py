from abc import ABC, abstractmethod

class IPopulationBinomialLikelihoodComparer(ABC):
    """Interface for potential central population value comparer"""

    @abstractmethod
    def getStandardError(self) -> float:
        """
        Description
        ----------
        Returns the standard error of the population sample

        Returns
        -------
        float
            The standard error of the population sample
        """
        pass

    @abstractmethod
    def getConfidenceInterval(self, confidenceLevel: float) -> tuple:
        """
        Description
        ----------
        Contructs a confidence interval of the difference in population means

        Parameters
        ----------
        confidenceLevel : float
            The likelihood of the true value falling in this interval

        Returns
        -------
        tuple
            The bounds of the interval
        """
        pass

    @abstractmethod
    def getTestStatistic(self, testDelta: float) -> float:
        """
        Description
        ----------
        Gets the test statistic 

        Parameters
        ----------
        testDelta : float
            The mean value tested against in the null hypothesis

        Returns
        -------
        float
            the value of the test statistic
        """
        pass


    @abstractmethod
    def population1LikelihoodGreaterTest(self, type1Confidence: float) -> bool:
        """
        Description
        ----------
        Performs a significance test to determine if the first population
        has greater likelihood

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
    def population1LikelihoodLesserTest(self, type1Confidence: float) -> bool:
        """
        Description
        ----------
        Performs a significance test to determine if the first population
        has lesser likelihood

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
    def population1LikelihoodUnequalTest(self, type1Confidence: float) -> bool:
        """
        Description
        ----------
        Performs a significance test to determine if the first population
        has equal likelihood

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
