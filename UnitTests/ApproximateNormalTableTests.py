import unittest
from Utilities.NormalDistriution.ApproximateNormalTable import ApproximateNormalTable

class ApproximateNormalTableTests(unittest.TestCase):
    """Unit testing class for the ApproximateNormalTable"""

    def test_pdf_whencalled(self):
        """
        Tests the value of the pdf function
        """
        self.assertAlmostEqual(ApproximateNormalTable.pdf(0), 0.22507907903927651)

    def test_pdf_whenNone(self):
        """
        Tests the value of the pdf function
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
        Tests the value of the pdf function
        """
        table: ApproximateNormalTable = ApproximateNormalTable()
        self.assertRaises(ValueError, table.getLeftTailArea, None)

    def test_getZValue_whenCalled(self):
        """
        Tests
        """
        table: ApproximateNormalTable = ApproximateNormalTable()
        self.assertAlmostEqual(table.getZValue(0.975), 1.96)

    def test_getZValue_whenNegative(self):
        """
        
        """
        table: ApproximateNormalTable = ApproximateNormalTable()
        self.assertRaises(ValueError, table.getZValue, -1)

    def test_getZValue_whenNone(self):
        """
        
        """
        table: ApproximateNormalTable = ApproximateNormalTable()
        self.assertRaises(ValueError, table.getZValue, None)

    def test_getZValue_whenOverOne(self):
        """
        
        """
        table: ApproximateNormalTable = ApproximateNormalTable()
        self.assertRaises(ValueError, table.getZValue, 2)
