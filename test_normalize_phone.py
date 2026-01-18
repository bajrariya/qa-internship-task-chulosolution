import pytest
from phone import normalize_phone


# -------- VALID CASES --------
def test_valid_case_with_country_code():
    assert normalize_phone("+9779812345678") == "+9779812345678"

def test_valid_case_starting_zero():
    assert normalize_phone("09812345678") == "+9779812345678"

def test_valid_case_10_digits():
    assert normalize_phone("9812345678") == "+9779812345678"


# -------- INVALID CASES --------
def test_invalid_case_letters():
    with pytest.raises(ValueError):
        normalize_phone("98AB345678")

def test_invalid_case_short_number():
    with pytest.raises(ValueError):
        normalize_phone("98123")

def test_invalid_case_wrong_start():
    with pytest.raises(ValueError):
        normalize_phone("1234567890")


# -------- EDGE CASES --------
def test_edge_case_empty():
    with pytest.raises(ValueError):
        normalize_phone("")

def test_edge_case_spaces_only():
    with pytest.raises(ValueError):
        normalize_phone("   ")
