from PopulationComparisonInference.CentralValue.IPopulationCentralValueComparer import IPopulationCentralValueComparer

class PairedNormalCentralValueComparer(IPopulationCentralValueComparer):
    """"""

    def __init__(self) -> None:
        """
        
        """
        super().__init__()

    def getConfidenceInterval(self, confidenceLevel: float) -> tuple:
        pass

    def sampleSizeForConfidenceInterval(self, confidenceLevel: float, width: float) -> float:
        pass

    def sampleSizeForTesting(self, type1Confidence: float, type2Confidence: float, delta: float) -> float:
        pass

    def getTestStatistic(self, testDelta: float) -> float:
        pass

    def rightTailDeltaSignificanceTest(self, delta: float, confidenceLevel: float) -> bool:
        pass

    def leftTailDeltaSignificanceTest(self, delta: float, confidenceLevel: float) -> bool:
        pass

    def twinTailDeltaSignificanceTest(self, delta: float, confidenceLevel: float) -> bool:
        pass
