import math
from Utilities.BinomialDistribution.IBinomialDistribution import IBinomialDistribution

class BinomialDistribution(IBinomialDistribution):
    """Class which approximates a discrete binomial distribution"""

    def __choose(self, total: int, chosen: int) -> float:
        return math.factorial(total) / (math.factorial(chosen) * math.factorial(total-chosen))

    def pmf(self, successes: int, trials: int, likelihood: float) -> float:
        return self.__choose(trials, successes) * (likelihood ** successes) * ((1 - likelihood) ** (trials - successes))

    def getLeftTailArea(self, successes: int, trials: int, likelihood: float) -> float:
        sum: float = 0
        for i in range(successes + 1):
            sum += self.pmf(i, trials, likelihood)
        return sum
