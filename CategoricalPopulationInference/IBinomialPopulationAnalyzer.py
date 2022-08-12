from abc import ABC, abstractmethod

class IBinomialPopulationAnalyzer(ABC):
    """Interface for Binomial distribution"""

    @abstractmethod
    def getSampleLikelihood(self) -> float:
        """
        Description
        ----------
        Returns the likelihood of the population sample

        Returns
        -------
        float
            The likelihood of the population sample
        """
        pass

    @abstractmethod
    def getSampleStandardError(self) -> float:
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
        Contructs a confidence interval of the population likelihood

        Parameters
        ----------
        confidenceLevel : float
            The likelihood of the true likelihood falling in this interval

        Returns
        -------
        tuple
            The bounds of the interval
        """
        return

    @abstractmethod
    def sampleSizeForConfidenceInterval(self, confidenceLevel: float, width: float) -> int:
        """
        Description
        ----------
        Finds the required sample size of constructing a CI with the provided
        level of confidence

        Parameters
        ----------
        confidenceLevel : float
            The likelihood of the true likelihood falling in this interval

        width : float
            Maximum absolute width of the interval

        Returns
        -------
        float
            The required sample size unrounded
        """
        return

    @abstractmethod
    def getTestStatistic(self, testLikelihood: float) -> float:
        """
        Description
        ----------
        Gets the test statistic 

        Parameters
        ----------
        testLikelihood : float
            The likelihood value tested against in the null hypothesis

        Returns
        -------
        float
            the value of the test statistic
        """
        pass


    @abstractmethod
    def rightTailtLikelihoodSignificanceTest(self, testLikelihood: float, confidenceLevel: float) -> bool:
        """
        Description
        ----------
        Performs a right tail level of significance test to determine if the research
        hypotheses is accepted or not

        Parameters
        ----------
        testLikelihood : float
            The testLikelihood value tested against in the null hypothesis

        confidenceLevel : float
            The confidence level of the test

        Returns
        -------
        bool
            true if the research hypotheses is accepted, false if rejected
        """
        pass

    @abstractmethod
    def leftTailLikelihoodSignificanceTest(self, testLikelihood: float, confidenceLevel: float) -> bool:
        """
        Description
        ----------
        Performs a left tail level of significance test to determine if the research
        hypotheses is accepted or not

        Parameters
        ----------
        mean : float
            The mean value tested against in the null hypothesis

        confidenceLevel : float
            The confidence level of the test

        Returns
        -------
        bool
            true if the research hypotheses is accepted, false if rejected
        """
        pass

    @abstractmethod
    def twinTailLikelihoodSignificanceTest(self, testLikelihood: float, confidenceLevel: float) -> bool:
        """
        Description
        ----------
        Performs a twin tail level of significance test to determine if the research
        hypotheses is accepted or not

        Parameters
        ----------
        testLikelihood : float
            The mean value tested against in the null hypothesis

        confidenceLevel : float
            The confidence level of the test

        Returns
        -------
        bool
            true if the research hypotheses is accepted, false if rejected
        """
        pass
