import unittest
import api_manager
from api_manager import Invoice, getInvoiceById, postInvoice, getTaxById

class TestAPI(unittest.TestCase):
    
    def setUp(self):
        self.invoice = Invoice("1", 500, 100)
        
    def test_getInvoiceById(self):
        invoice = getInvoiceById("1")
        self.assertEqual(invoice.ID, "1")
        self.assertEqual(invoice.Amount, 500)
        self.assertEqual(invoice.Tax, 100)
        
    def test_postInvoice(self):
        invoice = postInvoice("2", 600, 150)
        self.assertEqual(invoice.ID, "2")
        self.assertEqual(invoice.Amount, 600)
        self.assertEqual(invoice.Tax, 150)
        
    def test_getTaxById(self):
        tax = getTaxById("1")
        self.assertEqual(tax, 100)

if __name__ == "__main__":
    unittest.main()