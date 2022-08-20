import unittest
from Utilities.ChiSquaredDistribution.SciPyChiSquared import SciPyChiSquared

class SciPyChiSquaredTests(unittest.TestCase):
    """Unit testing class for the SciPyChiSquared"""
    
    def test_getLeftTailArea_whenCalled(self):
        """
        Tests the value of getLeftTailArea when the given zval within range of the bounds
        """
        chiSquareDist: SciPyChiSquared = SciPyChiSquared()
        self.assertAlmostEqual(chiSquareDist.getLeftTailArea(2.2, 8), 0.02574181652967084)

    def test_getLeftTailArea_whenChiValNone(self):
        """
        Tests that the getLeftTailArea function raises a value exception when given a null chi val argument
        """
        chiSquareDist: SciPyChiSquared = SciPyChiSquared()
        self.assertRaises(ValueError, chiSquareDist.getLeftTailArea, None, 8)

    def test_getLeftTailArea_whenDFNone(self):    
        """
        Tests that the getLeftTailArea function raises a value exception when given a null df argument
        """
        chiSquareDist: SciPyChiSquared = SciPyChiSquared()
        self.assertRaises(ValueError, chiSquareDist.getLeftTailArea, 1.96, None)

    def test_getLeftTailArea_whenDFNegative(self):    
        """
        Tests that the getLeftTailArea function raises a value exception when given a negative df argument
        """
        chiSquareDist: SciPyChiSquared = SciPyChiSquared()
        self.assertRaises(ValueError, chiSquareDist.getLeftTailArea, 1.96, -1)

    def test_getChiSquaredPercentileVal_whenCalled(self):
        """
        Tests the value of getChiSquaredVal when the given arguments within range of the bounds
        """
        chiSquareDist: SciPyChiSquared = SciPyChiSquared()
        self.assertAlmostEqual(chiSquareDist.getChiSquaredPercentileVal(0.99, 8), 20.090235029663233)

    def test_getChiSquaredPercentileVal_whenDFNegative(self):    
        """
        Tests that the getChiSquaredVal function raises a value exception when given a negative df argument
        """
        chiSquareDist: SciPyChiSquared = SciPyChiSquared()
        self.assertRaises(ValueError, chiSquareDist.getChiSquaredPercentileVal, 1.96, -1)

    def test_getChiSquaredPercentileVal_whenDFNone(self):    
        """
        Tests that the getChiSquaredVal function raises a value exception when given a null df argument
        """
        chiSquareDist: SciPyChiSquared = SciPyChiSquared()
        self.assertRaises(ValueError, chiSquareDist.getChiSquaredPercentileVal, 1.96, None)

    def test_getChiSquaredPercentileVal_whenAreaNegative(self):    
        """
        Tests that the getChiSquaredVal function raises a value exception when given a negative Area argument
        """
        chiSquareDist: SciPyChiSquared = SciPyChiSquared()
        self.assertRaises(ValueError, chiSquareDist.getChiSquaredPercentileVal, -1, 5)

    def test_getChiSquaredPercentileVal_whenAreaOverOne(self):    
        """
        Tests that the getChiSquaredVal function raises a value exception when given a too large Area argument
        """
        chiSquareDist: SciPyChiSquared = SciPyChiSquared()
        self.assertRaises(ValueError, chiSquareDist.getChiSquaredPercentileVal, 2, 5)

    def test_getChiSquaredPercentileVal_whenAreaNone(self):    
        """
        Tests that the getChiSquaredVal function raises a value exception when given a null Area argument
        """
        chiSquareDist: SciPyChiSquared = SciPyChiSquared()
        self.assertRaises(ValueError, chiSquareDist.getChiSquaredPercentileVal, None, 5)

    def test_getChiSquaredUpperVal_whenCalled(self):
        """
        Tests the value of getChiSquaredUpperVal with legal argument values
        """
        chiSquareDist: SciPyChiSquared = SciPyChiSquared()
        self.assertAlmostEqual(chiSquareDist.getChiSquaredUpperVal(0.99, 8), 21.954954990659534)

    def test_getChiSquaredUpperVal_whenDFNone(self):
        """
        Tests that getChiSquaredUpperVal raises an error when given a negative df
        """
        chiSquareDist: SciPyChiSquared = SciPyChiSquared()
        self.assertRaises(ValueError, chiSquareDist.getChiSquaredUpperVal, 0.95, None)

    def test_getChiSquaredUpperVal_whenDFNegative(self):
        """
        Tests that getChiSquaredUpperVal raises an error when given a negative df
        """
        chiSquareDist: SciPyChiSquared = SciPyChiSquared()
        self.assertRaises(ValueError, chiSquareDist.getChiSquaredUpperVal, 0.95, -1)

    def test_getChiSquaredUpperVal_type1ConfidenceNone(self):
        """
        Tests that getChiSquaredUpperVal raises an error when given a negative type1Confidence
        """
        chiSquareDist: SciPyChiSquared = SciPyChiSquared()
        self.assertRaises(ValueError, chiSquareDist.getChiSquaredUpperVal, None, 5)

    def test_getChiSquaredUpperVal_type1ConfidenceNegative(self):
        """
        Tests that getChiSquaredUpperVal raises an error when given a negative type1Confidence
        """
        chiSquareDist: SciPyChiSquared = SciPyChiSquared()
        self.assertRaises(ValueError, chiSquareDist.getChiSquaredUpperVal, -1, 5)

    def test_getChiSquaredUpperVal_type1ConfidenceTooLarge(self):
        """
        Tests that getChiSquaredUpperVal raises an error when given a type1Confidence that is over one
        """
        chiSquareDist: SciPyChiSquared = SciPyChiSquared()
        self.assertRaises(ValueError, chiSquareDist.getChiSquaredUpperVal, 2, 5)

    
    def test_getChiSquaredLowerVal_whenCalled(self):
        """
        Tests the value of getChiSquaredLowerVal with legal argument values
        """
        chiSquareDist: SciPyChiSquared = SciPyChiSquared()
        self.assertAlmostEqual(chiSquareDist.getChiSquaredLowerVal(0.99, 8), 1.3444130870148103)

    def test_getChiSquaredLowerVal_whenDFNone(self):
        """
        Tests that getChiSquaredLowerVal raises an error when given a negative df
        """
        chiSquareDist: SciPyChiSquared = SciPyChiSquared()
        self.assertRaises(ValueError, chiSquareDist.getChiSquaredLowerVal, 0.95, None)

    def test_getChiSquaredLowerVal_whenDFNegative(self):
        """
        Tests that getChiSquaredLowerVal raises an error when given a negative df
        """
        chiSquareDist: SciPyChiSquared = SciPyChiSquared()
        self.assertRaises(ValueError, chiSquareDist.getChiSquaredLowerVal, 0.95, -1)

    def test_getChiSquaredLowerVal_type1ConfidenceNone(self):
        """
        Tests that getChiSquaredLowerVal raises an error when given a negative type1Confidence
        """
        chiSquareDist: SciPyChiSquared = SciPyChiSquared()
        self.assertRaises(ValueError, chiSquareDist.getChiSquaredLowerVal, None, 5)

    def test_getChiSquaredLowerVal_type1ConfidenceNegative(self):
        """
        Tests that getChiSquaredLowerVal raises an error when given a negative type1Confidence
        """
        chiSquareDist: SciPyChiSquared = SciPyChiSquared()
        self.assertRaises(ValueError, chiSquareDist.getChiSquaredLowerVal, -1, 5)

    def test_getChiSquaredLowerVal_type1ConfidenceTooLarge(self):
        """
        Tests that getChiSquaredLowerVal raises an error when given a type1Confidence that is over one
        """
        chiSquareDist: SciPyChiSquared = SciPyChiSquared()
        self.assertRaises(ValueError, chiSquareDist.getChiSquaredLowerVal, 2, 5)
