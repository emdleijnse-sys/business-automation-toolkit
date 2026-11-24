"""Dependency-free financial utilities. All monetary inputs use one currency."""
from decimal import Decimal
from collections import defaultdict

def money(value):
    result = Decimal(str(value))
    if not result.is_finite():
        raise ValueError("Amount must be finite")
    return result

def forecast(opening, periods):
    """Return sequential closing balances from (receipts, payments) pairs."""
    balance = money(opening)
    result = []
    for receipts, payments in periods:
        receipts, payments = money(receipts), money(payments)
        if min(receipts, payments) < 0:
            raise ValueError("Receipts and payments must be nonnegative")
        balance += receipts - payments
        result.append(balance)
    return result

def reconcile(bank, ledger):
    """Match (reference, signed amount) rows only when unique on both sides.
    Return matched pairs and unresolved row indices; never guess duplicates.
    """
    def index(rows):
        groups = defaultdict(list)
        for i, (reference, amount) in enumerate(rows):
            if reference and reference.strip():
                groups[(reference.strip(), money(amount))].append(i)
        return groups
    bank, ledger = list(bank), list(ledger)
    a, b = index(bank), index(ledger)
    matched = sorted((ids[0], b[key][0]) for key, ids in a.items()
                     if len(ids) == 1 and len(b.get(key, [])) == 1)
    used_a, used_b = {i for i,j in matched}, {j for i,j in matched}
    return {"matched": matched,
            "unmatched_bank": [i for i in range(len(bank)) if i not in used_a],
            "unmatched_ledger": [j for j in range(len(ledger)) if j not in used_b]}

def ecommerce_kpis(revenue, cost_of_goods, variable_costs, orders):
    """Calculate contribution and ratios; revenue excludes VAT and refunds."""
    revenue, cost_of_goods, variable_costs = map(money, (revenue, cost_of_goods, variable_costs))
    if not isinstance(orders, int) or orders < 0:
        raise ValueError("Orders must be a nonnegative integer")
    gross = revenue - cost_of_goods
    contribution = gross - variable_costs
    return {"gross_profit": gross, "contribution": contribution,
            "gross_margin": gross / revenue if revenue else None,
            "contribution_margin": contribution / revenue if revenue else None,
            "average_order_value": revenue / orders if orders else None}
