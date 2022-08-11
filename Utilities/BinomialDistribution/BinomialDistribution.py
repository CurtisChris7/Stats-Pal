import math
from Utilities.BinomialDistribution.IBinomialDistribution import IBinomialDistribution

class BinomialDistribution(IBinomialDistribution):
    """Class which approximates a discrete binomial distribution"""

    def __choose(self, total: int, chosen: int) -> float:
        return math.factorial(total) / (math.factorial(chosen) * math.factorial(total-chosen))

    def pmf(self, successes: int, trials: int, likelihood: float) -> float:
        if successes == None or successes < 0:
            raise ValueError("Cannot have negative or null successes")
        if trials == None or trials < 0:
            raise ValueError("Cannot have negative or null trials")
        if likelihood == None or likelihood < 0:
            raise ValueError("Cannot have negative or null likelihood")
        if likelihood > 1:
            raise ValueError("Cannot have likelihood greater than 1")
        if successes > trials:
            raise ValueError("Cannot have more successes than trials")
        return self.__choose(trials, successes) * (likelihood ** successes) * ((1 - likelihood) ** (trials - successes))

    def getLeftTailArea(self, successes: int, trials: int, likelihood: float) -> float:
        if successes == None or successes < 0:
            raise ValueError("Cannot have negative or null successes")
        if trials == None or trials < 0:
            raise ValueError("Cannot have negative or null trials")
        if likelihood == None or likelihood < 0:
            raise ValueError("Cannot have negative or null likelihood")
        if likelihood > 1:
            raise ValueError("Cannot have likelihood greater than 1")
        if successes > trials:
            raise ValueError("Cannot have more successes than trials")
        sum: float = 0
        for i in range(successes + 1):
            sum += self.pmf(i, trials, likelihood)
        return sum
