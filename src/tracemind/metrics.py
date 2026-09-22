"""Stable observability metrics for AI executions."""

def error_rate(total: int, errors: int) -> float:
    if total <= 0 or errors < 0 or errors > total:
        raise ValueError("invalid execution counts")
    return errors / total

def success_rate(total: int, errors: int) -> float:
    return 1.0 - error_rate(total, errors)