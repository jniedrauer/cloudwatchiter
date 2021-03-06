"""Cron Schedule Expressions"""


from datetime import datetime
from typing import List
from .abc_expression import AbstractExpression


class Cron(AbstractExpression):
    """Cloudwatch cron Schedule Expression"""

    element_count: int = 6
    valid_types: tuple = (
        'cron',
    )

    def get_next(self, count: int = 1, start: int = 1) -> List[datetime]:
        """Get next event(s)"""
        pass

    def get_previous(self, count: int = 1, start: int = 1) -> List[datetime]:
        """Get past event(s)"""
        pass

    @property
    def minutes(self) -> str:
        """Cron minutes"""
        return self.elements[0]

    @property
    def hours(self) -> str:
        """Cron hours"""
        return self.elements[1]

    @property
    def day(self) -> str:
        """Cron days"""
        return self.elements[2]

    @property
    def month(self) -> str:
        """Cron month"""
        return self.elements[3]

    @property
    def day_of_week(self) -> str:
        """Cron day of week"""
        return self.elements[4]

    @property
    def year(self) -> str:
        """Cron year"""
        return self.elements[5]
