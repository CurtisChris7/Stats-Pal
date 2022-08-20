import unittest
from Utilities.FDistribution.SciPyFDistribution import SciPyFDistribution

class SciPyFDistributionTests(unittest.TestCase):
    """Unit testing class for the SciPyFDistribution"""

    def test_getFPercentileValue_whenCalled(self):
        """
        Tests the value of getTValue when the given arguments within range of the bounds
        """
        fDist: SciPyFDistribution = SciPyFDistribution()
        self.assertAlmostEqual(fDist.getFPercentileValue(0.975, 10, 7), 4.761116434996814)

    def test_getFPercentileValue_whenD1FNegative(self):    
        """
        Tests that the getFPercentileValue function raises a value exception when given a negative df argument
        """
        fDist: SciPyFDistribution = SciPyFDistribution()
        self.assertRaises(ValueError, fDist.getFPercentileValue, 0.975, -10, 7)

    def test_getFPercentileValue_whenDF1None(self):    
        """
        Tests that the getFPercentileValue function raises a value exception when given a null df argument
        """
        fDist: SciPyFDistribution = SciPyFDistribution()
        self.assertRaises(ValueError, fDist.getFPercentileValue, 0.975, None, 7)

    def test_getFPercentileValue_whenD2FNegative(self):    
        """
        Tests that the getFPercentileValue function raises a value exception when given a negative df argument
        """
        fDist: SciPyFDistribution = SciPyFDistribution()
        self.assertRaises(ValueError, fDist.getFPercentileValue, 0.975, 10, -7)

    def test_getFPercentileValue_whenDF2None(self):    
        """
        Tests that the getFPercentileValue function raises a value exception when given a null df argument
        """
        fDist: SciPyFDistribution = SciPyFDistribution()
        self.assertRaises(ValueError, fDist.getFPercentileValue, 0.975, 10, None)

    def test_getFPercentileValue_whenPercentileNegative(self):    
        """
        Tests that the getFPercentileValue function raises a value exception when given a negative Percentile argument
        """
        fDist: SciPyFDistribution = SciPyFDistribution()
        self.assertRaises(ValueError, fDist.getFPercentileValue, -0.975, 10, 7)

    def test_getFPercentileValue_whenPercentileOverOne(self):    
        """
        Tests that the getFPercentileValue function raises a value exception when given a too large Percentile argument
        """
        fDist: SciPyFDistribution = SciPyFDistribution()
        self.assertRaises(ValueError, fDist.getFPercentileValue, 2, 10, 7)

    def test_getFPercentileValue_whenPercentileNone(self):    
        """
        Tests that the getFPercentileValue function raises a value exception when given a null Percentile argument
        """
        fDist: SciPyFDistribution = SciPyFDistribution()
        self.assertRaises(ValueError, fDist.getFPercentileValue, None, 10, 7)


    def test_getFLowerValue_whenCalled(self):
        """
        Tests the value of getFPercentileValue when the given arguments within range of the bounds
        """
        fDist: SciPyFDistribution = SciPyFDistribution()
        self.assertAlmostEqual(fDist.getFLowerValue(0.95, 39, 39), 0.5288993273080331)

    def test_getFLowerValue_whenD1FNegative(self):    
        """
        Tests that the getFLowerValue function raises a value exception when given a negative df argument
        """
        fDist: SciPyFDistribution = SciPyFDistribution()
        self.assertRaises(ValueError, fDist.getFLowerValue, 0.975, -10, 7)

    def test_getFLowerValue_whenDF1None(self):    
        """
        Tests that the getFLowerValue function raises a value exception when given a null df argument
        """
        fDist: SciPyFDistribution = SciPyFDistribution()
        self.assertRaises(ValueError, fDist.getFLowerValue, 0.975, None, 7)

    def test_getFLowerValue_whenD2FNegative(self):    
        """
        Tests that the getFLowerValue function raises a value exception when given a negative df argument
        """
        fDist: SciPyFDistribution = SciPyFDistribution()
        self.assertRaises(ValueError, fDist.getFLowerValue, 0.975, 10, -7)

    def test_getFLowerValue_whenDF2None(self):    
        """
        Tests that the getFLowerValue function raises a value exception when given a null df argument
        """
        fDist: SciPyFDistribution = SciPyFDistribution()
        self.assertRaises(ValueError, fDist.getFLowerValue, 0.975, 10, None)

    def test_getFLowerValue_whenPercentileNegative(self):    
        """
        Tests that the getFLowerValue function raises a value exception when given a negative Percentile argument
        """
        fDist: SciPyFDistribution = SciPyFDistribution()
        self.assertRaises(ValueError, fDist.getFLowerValue, -0.975, 10, 7)

    def test_getFLowerValue_whenPercentileOverOne(self):    
        """
        Tests that the getFLowerValue function raises a value exception when given a too large Percentile argument
        """
        fDist: SciPyFDistribution = SciPyFDistribution()
        self.assertRaises(ValueError, fDist.getFLowerValue, 2, 10, 7)

    def test_getFLowerValue_whenPercentileNone(self):    
        """
        Tests that the getFLowerValue function raises a value exception when given a null Percentile argument
        """
        fDist: SciPyFDistribution = SciPyFDistribution()
        self.assertRaises(ValueError, fDist.getFLowerValue, None, 10, 7)


    def test_getFUpperValue_whenCalled(self):
        """
        Tests the value of getFPercentileValue when the given arguments within range of the bounds
        """
        fDist: SciPyFDistribution = SciPyFDistribution()
        self.assertAlmostEqual(fDist.getFUpperValue(0.95, 39, 39), 1.8907189863329057)

    def test_getFUpperValue_whenD1FNegative(self):    
        """
        Tests that the getFUpperValue function raises a value exception when given a negative df argument
        """
        fDist: SciPyFDistribution = SciPyFDistribution()
        self.assertRaises(ValueError, fDist.getFUpperValue, 0.975, -10, 7)

    def test_getFUpperValue_whenDF1None(self):    
        """
        Tests that the getFUpperValue function raises a value exception when given a null df argument
        """
        fDist: SciPyFDistribution = SciPyFDistribution()
        self.assertRaises(ValueError, fDist.getFUpperValue, 0.975, None, 7)

    def test_getFUpperValue_whenD2FNegative(self):    
        """
        Tests that the getFUpperValue function raises a value exception when given a negative df argument
        """
        fDist: SciPyFDistribution = SciPyFDistribution()
        self.assertRaises(ValueError, fDist.getFUpperValue, 0.975, 10, -7)

    def test_getFUpperValue_whenDF2None(self):    
        """
        Tests that the getFUpperValue function raises a value exception when given a null df argument
        """
        fDist: SciPyFDistribution = SciPyFDistribution()
        self.assertRaises(ValueError, fDist.getFUpperValue, 0.975, 10, None)

    def test_getFUpperValue_whenPercentileNegative(self):    
        """
        Tests that the getFUpperValue function raises a value exception when given a negative Percentile argument
        """
        fDist: SciPyFDistribution = SciPyFDistribution()
        self.assertRaises(ValueError, fDist.getFUpperValue, -0.975, 10, 7)

    def test_getFUpperValue_whenPercentileOverOne(self):    
        """
        Tests that the getFUpperValue function raises a value exception when given a too large Percentile argument
        """
        fDist: SciPyFDistribution = SciPyFDistribution()
        self.assertRaises(ValueError, fDist.getFUpperValue, 2, 10, 7)

    def test_getFUpperValue_whenPercentileNone(self):    
        """
        Tests that the getFUpperValue function raises a value exception when given a null Percentile argument
        """
        fDist: SciPyFDistribution = SciPyFDistribution()
        self.assertRaises(ValueError, fDist.getFUpperValue, None, 10, 7)