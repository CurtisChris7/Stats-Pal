from scipy.stats import t
from PopulationCentralValueInference.IPopulationCentralValueAnalyzer import IPopulationCentralValueAnalyzer

class TDistributionCentralValueAnalyzer(IPopulationCentralValueAnalyzer):
     def __init__(self) -> None:
          super().__init__()
