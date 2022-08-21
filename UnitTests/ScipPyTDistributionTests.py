import unittest
from Utilities.TDistribution.SciPyTDistribution import SciPyTDistribution

class SciPyTDistributionTests(unittest.TestCase):
    """Unit testing class for the SciPyTDistribution"""
    
    def test_getLeftTailArea_whenCalled(self):
        """
        Tests the value of getLeftTailArea when the given t val within range of the bounds
        """
        tDist: SciPyTDistribution = SciPyTDistribution()
        self.assertAlmostEqual(tDist.getLeftTailArea(2.2, 8), 0.9705030460420883)

    def test_getLeftTailArea_whenTValNone(self):
        """
        Tests that the getLeftTailArea function raises a value exception when given a null t val argument
        """
        table: SciPyTDistribution = SciPyTDistribution()
        self.assertRaises(ValueError, table.getLeftTailArea, None, 8)

    def test_getLeftTailArea_whenDFNone(self):    
        """
        Tests that the getLeftTailArea function raises a value exception when given a null df argument
        """
        table: SciPyTDistribution = SciPyTDistribution()
        self.assertRaises(ValueError, table.getLeftTailArea, 1.96, None)

    def test_getLeftTailArea_whenDFNegative(self):    
        """
        Tests that the getLeftTailArea function raises a value exception when given a negative df argument
        """
        table: SciPyTDistribution = SciPyTDistribution()
        self.assertRaises(ValueError, table.getLeftTailArea, 1.96, -1)

    def test_getTValue_whenCalled(self):
        """
        Tests the value of getTValue when the given arguments within range of the bounds
        """
        tDist: SciPyTDistribution = SciPyTDistribution()
        self.assertAlmostEqual(tDist.getTPercentileValue(0.99, 8), 2.896459442760522)

    def test_getTValue_whenDFNegative(self):    
        """
        Tests that the getTValue function raises a value exception when given a negative df argument
        """
        table: SciPyTDistribution = SciPyTDistribution()
        self.assertRaises(ValueError, table.getTPercentileValue, 1.96, -1)

    def test_getTValue_whenDFNone(self):    
        """
        Tests that the getTValue function raises a value exception when given a null df argument
        """
        table: SciPyTDistribution = SciPyTDistribution()
        self.assertRaises(ValueError, table.getTPercentileValue, 1.96, None)

    def test_getTValue_whenAreaNegative(self):    
        """
        Tests that the getTValue function raises a value exception when given a negative Area argument
        """
        table: SciPyTDistribution = SciPyTDistribution()
        self.assertRaises(ValueError, table.getTPercentileValue, -1, 5)

    def test_getTValue_whenAreaOverOne(self):    
        """
        Tests that the getTValue function raises a value exception when given a too large Area argument
        """
        table: SciPyTDistribution = SciPyTDistribution()
        self.assertRaises(ValueError, table.getTPercentileValue, 2, 5)

    def test_getTValue_whenAreaNone(self):    
        """
        Tests that the getTValue function raises a value exception when given a null Area argument
        """
        table: SciPyTDistribution = SciPyTDistribution()
        self.assertRaises(ValueError, table.getTPercentileValue, None, 5)
