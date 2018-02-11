"""Rate Schedule Expressions"""

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

    def get_next(self, start: int = None, end: int = None):
        """Get next event(s)"""
        pass

    def get_previous(self, start: int = None, end: int = None):
        """Get past event(s)"""
        pass

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
