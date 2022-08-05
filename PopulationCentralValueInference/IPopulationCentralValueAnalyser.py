from abc import ABC, abstractmethod

class IPopulationCentralValueAnalyser(ABC):
    """Interface for potential central population value analyser."""

    @abstractmethod
    def getMean(self) -> float:
        """
        Description
        ----------
        Returns the mean of the population

        Returns
        -------
        float
            The mean of the population
        """
        pass

    @abstractmethod
    def getConfidenceInterval(self, confidenceLevel: float) -> tuple:
        """
        Description
        ----------
        Contructs a confidence interval of the population

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
    def sampleSizeForConfidenceInterval(self, confidenceLevel: float, width: float) -> float:
        """
        Description
        ----------
        Finds the required sample size of constructing a CI with the provided
        level of confidence

        Parameters
        ----------
        confidenceLevel : float
            The likelihood of the true mean falling in this interval

        width : float
            Maximum absolute width of the interval

        Returns
        -------
        float
            The required sample size unrounded
        """
        pass


    @abstractmethod
    def sampleSizeForTesting(self, type1Confidence: float, type2Confidence: float, delta: float) -> float:
        """
        Description
        ----------
        Finds the required sample size of constructing a CI with the provided
        confidence levels for both type1 and type2 errors

        Parameters
        ----------
        type1Confidence : float
            The likelihood of the true mean falling in this interval

        type2Confidence : float
            The likelihood of the true mean falling in this interval

        delta : float
            The difference between the mean in the null and research hypothesis

        Returns
        -------
        float
            The required sample size unrounded
        """
        pass

    @abstractmethod
    def rightTailMeanSignificanceTest(self, mean: float, confidenceLevel: float) -> bool:
        """
        Description
        ----------
        Performs a right tail level of significance test to determine if the research
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
    def leftTailMeanSignificanceTest(self, mean: float, confidenceLevel: float) -> bool:
        """
        Description
        ----------
        Performs a right tail level of significance test to determine if the research
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
    def twinTailMeanSignificanceTest(self, mean: float, confidenceLevel: float) -> bool:
        """
        Description
        ----------
        Performs a right tail level of significance test to determine if the research
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
    def rightTailMeanSignificanceTest(self, mean: float, type1Confidence: float, type2Confidence: float) -> tuple:
        """
        Description
        ----------
        Performs a right tail level of significance test to determine which of the null or
        research hypothesis are accepted or rejected

        Parameters
        ----------
        mean : float
            The mean value tested against in the null hypothesis

        type1Confidence : float
            The confidence level of the test

        type2Confidence: float
            The confidence level of the test

        Returns
        -------
        tuple
            A two element tuple of the following form:
                true if the null hypotheses is accepted, false if rejected
                true if the research hypotheses is accepted, false if rejected
        """
        pass

    @abstractmethod
    def leftTailMeanSignificanceTest(self, mean: float, type1Confidence: float, type2Confidence: float) -> tuple:
        """
        Description
        ----------
        Performs a right tail level of significance test to determine which of the null or
        research hypothesis are accepted or rejected

        Parameters
        ----------
        mean : float
            The mean value tested against in the null hypothesis

        type1Confidence : float
            The confidence level of the test

        type2Confidence: float
            The confidence level of the test

        Returns
        -------
        tuple
            A two element tuple of the following form:
                true if the null hypotheses is accepted, false if rejected
                true if the research hypotheses is accepted, false if rejected
        """
        pass

    @abstractmethod
    def twinTailMeanSignificanceTest(self, mean: float, type1Confidence: float, type2Confidence: float) -> tuple:
        """
        Description
        ----------
        Performs a right tail level of significance test to determine which of the null or
        research hypothesis are accepted or rejected

        Parameters
        ----------
        mean : float
            The mean value tested against in the null hypothesis

        type1Confidence : float
            The confidence level of the test

        type2Confidence: float
            The confidence level of the test

        Returns
        -------
        tuple
            A two element tuple of the following form:
                true if the null hypotheses is accepted, false if rejected
                true if the research hypotheses is accepted, false if rejected
        """
        pass

