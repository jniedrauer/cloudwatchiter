# pylint: disable-all

import pytest
from cloudwatchiter.cron import Cron

def test_invalid_elements():
    with pytest.raises(ValueError):
        cron = Cron('cron(1 2 3)')

def test_valid_elements():
    cron = Cron('cron(1 2 3 4 ? *)')

def test_element_split():
    cron = Cron('cron(1 2 3 4 ? *)')
    assert len(cron.elements) == Cron.element_count

def test_minutes():
    cron = Cron('cron(1 2 3 4 ? *)')
    assert cron.minutes == '1'

def test_hours():
    cron = Cron('cron(1 2 3 4 ? *)')
    assert cron.hours == '2'

def test_day():
    cron = Cron('cron(1 2 3 4 ? *)')
    assert cron.day == '3'

def test_month():
    cron = Cron('cron(1 2 3 4 ? *)')
    assert cron.month == '4'

def test_day_of_week():
    cron = Cron('cron(1 2 3 4 ? *)')
    assert cron.day_of_week == '?'

def test_year():
    cron = Cron('cron(1 2 3 4 ? *)')
    assert cron.year == '*'
