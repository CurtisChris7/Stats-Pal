from abc import ABC, abstractmethod

class IPopulationCentralValueComparer(ABC):
    """Interface for potential central population value comparer"""

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
    def rightTailDeltaSignificanceTest(self, delta: float, confidenceLevel: float) -> bool:
        """
        Description
        ----------
        Performs a right tail level of significance test to determine if the research
        hypotheses is accepted or not

        Parameters
        ----------
        delta : float
            The delta value tested against in the null hypothesis

        confidenceLevel : float
            The confidence level of the test

        Returns
        -------
        bool
            true if the research hypotheses is accepted, false if rejected
        """
        pass

    @abstractmethod
    def leftTailDeltaSignificanceTest(self, delta: float, confidenceLevel: float) -> bool:
        """
        Description
        ----------
        Performs a left tail level of significance test to determine if the research
        hypotheses is accepted or not

        Parameters
        ----------
        delta : float
            The delta value tested against in the null hypothesis

        confidenceLevel : float
            The confidence level of the test

        Returns
        -------
        bool
            true if the research hypotheses is accepted, false if rejected
        """
        pass

    @abstractmethod
    def twinTailDeltaSignificanceTest(self, delta: float, confidenceLevel: float) -> bool:
        """
        Description
        ----------
        Performs a twin tail level of significance test to determine if the research
        hypotheses is accepted or not

        Parameters
        ----------
        delta : float
            The delta value tested against in the null hypothesis

        confidenceLevel : float
            The confidence level of the test

        Returns
        -------
        bool
            true if the research hypotheses is accepted, false if rejected
        """
        pass
