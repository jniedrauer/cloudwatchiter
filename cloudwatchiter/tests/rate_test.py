# pylint: disable-all

import pytest
from cloudwatchiter.rate import Rate

def test_invalid_elements():
    with pytest.raises(ValueError):
        rate = Rate('rate(1)')

def test_valid_elements():
    rate = Rate('rate(5 minutes)')

def test_element_split():
    rate = Rate('rate(5 minutes)')
    assert len(rate.elements) == Rate.element_count

def test_element_values():
    rate = Rate('cron(5 minutes)')
    assert rate.value == '5'
    assert rate.unit == 'minutes'
