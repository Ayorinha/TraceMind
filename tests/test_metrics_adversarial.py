import pytest
from tracemind.metrics import bounded_rate
def test_bounded_rate_rejects_invalid_counts():
    with pytest.raises(ValueError): bounded_rate(10, 11)