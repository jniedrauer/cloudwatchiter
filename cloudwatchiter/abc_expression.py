"""Cloudwatch rate expression"""

from abc import ABC, abstractmethod
from datetime import datetime
from typing import List

class AbstractExpression(ABC):
    """Abstract base class for Cloudwatch expressions"""

    # mypy has some trouble iterating over properties still
    valid_types: tuple = tuple()

    @property
    @classmethod
    def element_count(cls):
        """Overriden by child classes"""
        raise NotImplementedError

    def __init__(self, expression: str) -> None:
        self.now = datetime.utcnow()
        __split: List[str] = expression.rstrip(')').split('(')
        self.type: str = self.validate_type(__split[0])
        try:
            self.elements = self.validate_elements(
                __split[1].split(' ')
            )
        except IndexError:
            raise ValueError('Invalid expression')

    @classmethod
    def validate_type(cls, typestr: str) -> str:
        """Validate that expression is a valid type"""
        if not typestr in cls.valid_types:
            raise ValueError(f'Invalid expression type: {typestr}')
        return typestr

    @classmethod
    def validate_elements(cls, elements: List[str]) -> List[str]:
        """Verify that number of elements matches expected"""
        if len(elements) != cls.element_count:
            raise ValueError(
                f'Invalid number of elements: {len(elements)}, '
                f'expected: {cls.element_count}'
            )
        return elements

    @abstractmethod
    def get_next(self, count: int = 1, start: int = 1) -> List[datetime]:
        """Get next event(s)"""
        raise NotImplementedError

    @abstractmethod
    def get_previous(self, count: int = 1, start: int = 1) -> List[datetime]:
        """Get past event(s)"""
        raise NotImplementedError
