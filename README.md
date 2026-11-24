# Business Automation Toolkit

An early-stage, dependency-free Python toolkit for small-business financial workflows. The goal is to provide transparent, reusable building blocks rather than a full accounting system.

## Features
- Exact one-to-one transaction reconciliation by reference and signed amount; duplicates remain unresolved.
- Sequential cash balance forecasting from expected receipts and payments.
- E-commerce gross profit, contribution margin and average order value.

## Quick start
Requires Python 3.10 or newer. Clone this repository and run:

```sh
python example.py
python -m unittest -v
```

All examples use synthetic data. Monetary values use Decimal; use a single currency per calculation. Revenue should exclude VAT and refunds. Ratios are fractions, not percentages. Reconciliation is not a substitute for accounting review. No external services or credentials are required.

## Status and roadmap
Initial prototype; no adoption or production-readiness claims. Planned work includes CSV adapters, reporting exports, forecast-versus-actual comparisons and more robust reconciliation rules.

Contributions are welcome; see CONTRIBUTING.md. Licensed under MIT (see LICENSE).
