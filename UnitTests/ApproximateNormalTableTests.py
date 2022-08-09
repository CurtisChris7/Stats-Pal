import unittest
from Utilities.ApproximateNormalTable import ApproximateNormalTable

class ApproximateNormalTableMethods(unittest.TestCase):

    def test_pdf_whencalled(self):
        self.assertAlmostEqual(ApproximateNormalTable.pdf(0), 0.22507907903927651)

