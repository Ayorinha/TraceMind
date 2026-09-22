from tracemind.metrics import error_rate,success_rate

def test_error_and_success_rates():
    assert error_rate(10,2) == .2
    assert success_rate(10,2) == .8
