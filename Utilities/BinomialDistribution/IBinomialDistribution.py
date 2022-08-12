from abc import ABC, abstractmethod

class IBinomialDistribution(ABC):
    """Interface for Binomial distribution"""

    @abstractmethod
    def pmf(self, successes: int, trials: int, likelihood: float) -> float:
        """
        Description
        ----------
        Finds the probablty of the binomial result given the number of trials, 
        successes and likelihood of success

        Parameters
        ----------
        successes: int
            The number of successful trials

        trials: int
            The number of total trials

        likelihood: float
            The likelihood of a given trial succeeding

        Returns
        -------
        float
            The likelihood of the result
        """
        pass

    @abstractmethod
    def getLeftTailArea(self, successes: int, trials: int, likelihood: float) -> float:
        """
        Description
        ----------
        Finds the left tail area value given the number of trials, successes and 
        likelihood of success

        Parameters
        ----------
        successes: int
            The number of successful trials

        trials: int
            The number of total trials

        likelihood: float
            The likelihood of a given trial succeeding

        Returns
        -------
        float
            The approximate area under the curve
        """
        pass
