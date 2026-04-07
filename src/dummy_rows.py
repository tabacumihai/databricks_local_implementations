from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import date, timedelta
from typing import List


@dataclass(frozen=True)
class CustomerEvent:
    event_id: int
    customer_id: int
    event_type: str
    amount: float
    event_date: str


def build_dummy_rows(n: int = 10) -> List[dict]:
    if n <= 0:
        return []

    base_date = date(2026, 1, 1)
    event_types = ["signup", "purchase", "renewal", "support"]

    rows: List[dict] = []
    for i in range(1, n + 1):
        item = CustomerEvent(
            event_id=i,
            customer_id=1000 + i,
            event_type=event_types[(i - 1) % len(event_types)],
            amount=round(10.0 * i + 0.99, 2),
            event_date=(base_date + timedelta(days=i - 1)).isoformat(),
        )
        rows.append(asdict(item))
    return rows
