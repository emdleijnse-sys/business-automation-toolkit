import unittest
from decimal import Decimal
from toolkit import forecast, reconcile, ecommerce_kpis

class ToolkitTests(unittest.TestCase):
    def test_forecast(self):
        self.assertEqual(forecast(100, [(20, 10), (0, 50)]), [Decimal(110), Decimal(60)])
    def test_invalid_forecast(self):
        with self.assertRaises(ValueError):
            forecast(0, [(-1, 0)])
    def test_exact_match(self):
        self.assertEqual(reconcile([("A", "1.20")], [("A", "1.2")])["matched"], [(0, 0)])
    def test_duplicate_not_matched(self):
        self.assertEqual(reconcile([("A", 1), ("A", 1)], [("A", 1)])["unmatched_bank"], [0, 1])
    def test_blank_reference(self):
        self.assertEqual(reconcile([("", 1)], [("", 1)])["matched"], [])
    def test_kpis(self):
        k = ecommerce_kpis(100, 40, 10, 2)
        self.assertEqual(k["contribution"], Decimal(50))
        self.assertEqual(k["average_order_value"], Decimal(50))
    def test_zero_revenue(self):
        self.assertIsNone(ecommerce_kpis(0, 0, 0, 0)["gross_margin"])

if __name__ == "__main__":
    unittest.main()
