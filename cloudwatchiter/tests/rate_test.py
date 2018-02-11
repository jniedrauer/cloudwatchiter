# pylint: disable-all

import pytest
from cloudwatchiter.rate import Rate

def test_invalid_elements():
    with pytest.raises(ValueError):
        rate = Rate('rate(1)')

def test_invalid_type():
    with pytest.raises(ValueError):
        rate = Rate('cron(1 day)')

def test_valid_elements():
    rate = Rate('rate(5 minutes)')

def test_element_split():
    rate = Rate('rate(5 minutes)')
    assert len(rate.elements) == Rate.element_count

def test_element_values():
    rate = Rate('rate(5 minutes)')
    assert rate.value == '5'
    assert rate.unit == 'minutes'

def test_invalid_units():
    with pytest.raises(ValueError):
        rate = Rate('rate(5 weeks)')
    with pytest.raises(ValueError):
        rate = Rate('rate(5 months)')
    with pytest.raises(ValueError):
        rate = Rate('rate(5 years)')

def test_valid_units():
    assert Rate('rate(1 day)').unit == 'day'
    assert Rate('rate(4 minutes)').unit == 'minutes'
    assert Rate('rate(1 hour)').unit == 'hour'

def test_invalid_value():
    with pytest.raises(ValueError):
        rate = Rate('rate(-1 days)')
    with pytest.raises(ValueError):
        rate = Rate('rate(day)')

def test_valid_value():
    assert Rate('rate(1 day)').value == '1'
    assert Rate('rate(4 minutes)').value == '4'
    assert Rate('rate(5 hour)').value == '5'
