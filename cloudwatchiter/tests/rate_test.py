# pylint: disable-all

from datetime import datetime
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

def test_minute_floor():
    rate = Rate('rate(1 minute)')
    rate.now = datetime(year=2018, month=2, day=11, hour=12, minute=30,
                        second=30)
    expected = datetime(year=2018, month=2, day=11, hour=12, minute=30)
    assert rate._get_unit_floor() == expected

def test_hour_floor():
    rate = Rate('rate(2 hours)')
    rate.now = datetime(year=2018, month=2, day=11, hour=12, minute=30,
                        second=30)
    expected = datetime(year=2018, month=2, day=11, hour=12)
    assert rate._get_unit_floor() == expected

def test_day_floor():
    rate = Rate('rate(3 day)')
    rate.now = datetime(year=2018, month=2, day=11, hour=12, minute=30,
                        second=30)
    expected = datetime(year=2018, month=2, day=11)
    assert rate._get_unit_floor() == expected

def test_day():
    rate = Rate('rate(1 day)')
    rate.now = datetime(year=2018, month=2, day=11, hour=12)

    expected = [datetime(year=2018, month=2, day=12)]
    assert rate.get_next() == expected

def test_invalid_day():
    rate = Rate('rate(1 day)')
    rate.now = datetime(year=2018, month=2, day=11, hour=12)

    with pytest.raises(ValueError):
        result = rate.get_next(1, 2)

def test_days_slice():
    rate = Rate('rate(2 days)')
    rate.now = datetime(year=2018, month=2, day=11, hour=12)

    expected = [
        datetime(year=2018, month=2, day=13),
        datetime(year=2018, month=2, day=15),
    ]
    assert rate.get_next(count=2) == expected

def test_hours_back_slice():
    rate = Rate('rate(2 hours)')
    rate.now = datetime(year=2018, month=2, day=11, hour=10, minute=30,
                        second=20)
    expected = [
        datetime(year=2018, month=2, day=11, hour=6),
        datetime(year=2018, month=2, day=11, hour=4),
        datetime(year=2018, month=2, day=11, hour=2),
    ]
    assert rate.get_previous(count=3, start=2) == expected

def test_minute_back():
    rate = Rate('rate(5 minute)')
    rate.now = datetime(year=2018, month=2, day=11, hour=12, minute=30,
                        second=20)
    expected = [
        datetime(year=2018, month=2, day=11, hour=12, minute=25)
    ]
    assert rate.get_previous() == expected
