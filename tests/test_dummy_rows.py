from src.dummy_rows import build_dummy_rows


def test_build_dummy_rows_size():
    rows = build_dummy_rows(3)
    assert len(rows) == 3


def test_build_dummy_rows_shape():
    row = build_dummy_rows(1)[0]
    assert set(row.keys()) == {"event_id", "customer_id", "event_type", "amount", "event_date"}


def test_build_dummy_rows_empty():
    assert build_dummy_rows(0) == []
