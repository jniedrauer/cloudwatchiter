"""Rate Schedule Expressions"""


from datetime import datetime, timedelta
from typing import List
from .abc_expression import AbstractExpression


class Rate(AbstractExpression):
    """Cloudwatch rate Schedule Expression"""

    element_count: int = 2
    valid_types: tuple = (
        'rate',
    )
    valid_units = (
        'minute',
        'minutes',
        'hour',
        'hours',
        'day',
        'days',
    )

    def __init__(self, *args):
        super().__init__(*args)
        self._validate_unit()
        self._validate_value()

    def get_next(self, count: int = 1, start: int = 1) -> List[datetime]:
        """Get next event(s)"""
        return self._get_range(count=count, start=start)

    def get_previous(self, count: int = 1, start: int = 1) -> List[datetime]:
        """Get past event(s)"""
        return self._get_range(count=count, start=start, forward=False)

    def _get_range(self, count, start, forward=True) -> List[datetime]:
        """Shared implementation for get_next and get_previous"""
        if not self.unit.endswith('s') and not all((count == 1, start == 1)):
            # Only one event will occur
            raise ValueError(
                'Requested range invalid for rate expression'
            )
        result: List[datetime] = []
        for i in range(count):
            result.append(
                self._get_unit_floor()
                + self._get_timedelta(start, forward=forward)
                + self._get_timedelta(i, forward=forward)
            )
        return result

    def _get_timedelta(self, quantity: int, forward: bool = True) -> timedelta:
        """Return a timedelta for given unit"""
        if forward:
            multiplier = 1
        else:
            multiplier = -1
        if self.unit.startswith('minute'):
            return timedelta(minutes=(int(self.value) * quantity * multiplier))
        elif self.unit.startswith('hour'):
            return timedelta(hours=(int(self.value) * quantity * multiplier))
        elif self.unit.startswith('day'):
            return timedelta(days=(int(self.value) * quantity * multiplier))
        else:
            raise ValueError

    def _get_unit_floor(self) -> datetime:
        """Return now rounded down to unit"""
        if self.unit.startswith('minute'):
            return self.now - timedelta(
                seconds=self.now.second,
                microseconds=self.now.microsecond,
            )
        elif self.unit.startswith('hour'):
            return self.now - timedelta(
                minutes=self.now.minute,
                seconds=self.now.second,
                microseconds=self.now.microsecond,
            )
        elif self.unit.startswith('day'):
            return self.now - timedelta(
                hours=self.now.hour,
                minutes=self.now.minute,
                seconds=self.now.second,
                microseconds=self.now.microsecond,
            )
        else:
            raise ValueError

    def _validate_unit(self) -> None:
        """Validate unit property"""
        if self.unit not in self.valid_units:
            raise ValueError(
                'Invalid unit: {self.unit}, '
                'expected: {self.valid_units}'
            )

    def _validate_value(self) -> None:
        """Validate value property"""
        try:
            assert int(self.value) > 0
        except (AssertionError, ValueError):
            raise ValueError(
                'Invalid rate: {self.value}, '
                'expected: positive integer'
            )

    @property
    def value(self) -> str:
        """Rate value"""
        return self.elements[0]

    @property
    def unit(self) -> str:
        """Rate unit"""
        return self.elements[1]
