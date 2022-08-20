import unittest
from Utilities.NormalDistriution.ApproximateNormalTable import ApproximateNormalTable

class ApproximateNormalTableTests(unittest.TestCase):
    """Unit testing class for the ApproximateNormalTable"""

    def test_construction_stepNone(self):
        """
        Tests that the constructor raises an exception when given a null step argument
        """
        self.assertRaises(ValueError, ApproximateNormalTable, step=None)

    def test_construction_stepNegative(self):
        """
        Tests that the constructor raises an exception when given a negative step argument
        """
        self.assertRaises(ValueError, ApproximateNormalTable, step=-1)

    def test_construction_precisionNone(self):
        """
        Tests that the constructor raises an exception when given a null precisio argument
        """
        self.assertRaises(ValueError, ApproximateNormalTable, precision=None)

    def test_construction_precisionNegative(self):
        """
        Tests that the constructor raises an exception when given a negatve precisio argument
        """
        self.assertRaises(ValueError, ApproximateNormalTable, precision=-1)

    def test_construction_lowerboundNone(self):
        """
        Tests that the constructor raises an exception when given a null lowerbound argument
        """
        self.assertRaises(ValueError, ApproximateNormalTable, lowerbound=None) 

    def test_construction_upperboundNone(self):
        """
        Tests that the constructor raises an exception when given a null upperbound argument
        """
        self.assertRaises(ValueError, ApproximateNormalTable, upperbound=None)  

    def test_pdf_whencalled(self):
        """
        Tests the value of the pdf function
        """
        self.assertAlmostEqual(ApproximateNormalTable.pdf(0), 0.22507907903927651)

    def test_pdf_whenNone(self):
        """
        Tests that the pdf function raises a value exception when given a null argument
        """
        self.assertRaises(ValueError, ApproximateNormalTable.pdf, None)

    def test_getLeftTailArea_valBelowLowerBound(self):
        """
        Tests the value of getLeftTailArea when the given zval is below the tables lower bound
        """
        table: ApproximateNormalTable = ApproximateNormalTable()
        self.assertEqual(table.getLeftTailArea(-6), 0)

    def test_getLeftTailArea_valAboveUpperBound(self):
        """
        Tests the value of getLeftTailArea when the given zval is above the upper lower bound
        """
        table: ApproximateNormalTable = ApproximateNormalTable()
        self.assertEqual(table.getLeftTailArea(6), 1)

    def test_getLeftTailArea_whenCalled(self):
        """
        Tests the value of getLeftTailArea when the given zval within range of the bounds
        """
        table: ApproximateNormalTable = ApproximateNormalTable()
        self.assertAlmostEqual(table.getLeftTailArea(1.96), 0.9750315874100378)

    def test_getLeftTailArea_whenNone(self):
        """
        Tests that the getLeftTailArea function raises a value exception when given a null argument
        """
        table: ApproximateNormalTable = ApproximateNormalTable()
        self.assertRaises(ValueError, table.getLeftTailArea, None)

    def test_getZPercentileValue_whenCalled(self):
        """
        Tests the z value when called normally
        """
        table: ApproximateNormalTable = ApproximateNormalTable()
        self.assertAlmostEqual(table.getZPercentileValue(0.975), 1.96)

    def test_getZPercentileValue_whenNegative(self):
        """
        Tests that the getZValue function raises a value exception when given a negative argument
        """
        table: ApproximateNormalTable = ApproximateNormalTable()
        self.assertRaises(ValueError, table.getZPercentileValue, -1)

    def test_getZPercentileValue_whenNone(self):
        """
        Tests that the getZValue function raises a value exception when given a null argument
        """
        table: ApproximateNormalTable = ApproximateNormalTable()
        self.assertRaises(ValueError, table.getZPercentileValue, None)

    def test_getZPercentileValue_whenOverOne(self):
        """
        Tests that the getZValue function raises a value exception when given an argument over 1
        """
        table: ApproximateNormalTable = ApproximateNormalTable()
        self.assertRaises(ValueError, table.getZPercentileValue, 2)
