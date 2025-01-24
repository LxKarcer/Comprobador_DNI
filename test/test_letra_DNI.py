import pytest
from ..DNI_ok import casosTest

# test/test_DNI_ok.py


@pytest.mark.parametrize("dni", casosTest)
def test_dni_format(dni):
    assert len(dni) == 9, f"Length of DNI {dni} is not 9"
    assert dni[:-1].isdigit(), f"First 8 characters of DNI {dni} are not digits"
    assert dni[-1].isalpha(), f"Last character of DNI {dni} is not a letter"