from toolkit import forecast, reconcile, ecommerce_kpis

# Synthetic examples only.
print(forecast(10000, [(5000, 7000), (6000, 4000)]))
print(reconcile([("INV-001", 125), ("INV-002", 80)], [("INV-001", 125)]))
print(ecommerce_kpis(1000, 400, 150, 20))
