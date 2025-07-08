# tests/test_filter.py
from get_papers.filter import is_non_academic

def test_non_academic_affiliation():
    assert is_non_academic("Pfizer Inc.") is True
    assert is_non_academic("Moderna Biotech Ltd.") is True
    assert is_non_academic("Johnson & Johnson") is True

def test_academic_affiliation():
    assert is_non_academic("Harvard University") is False
    assert is_non_academic("AIIMS Hospital, Delhi") is False
    assert is_non_academic("Indian Institute of Technology") is False
