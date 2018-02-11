"""Rate Schedule Expressions"""

from .abc_expression import AbstractExpression


class Rate(AbstractExpression):
    """Cloudwatch rate Schedule Expression"""

    element_count = 2

    def get_next(self, start: int = None, end: int = None):
        """Get next event(s)"""
        pass

    def get_previous(self, start: int = None, end: int = None):
        """Get past event(s)"""
        pass

    @property
    def value(self) -> str:
        """Rate value"""
        return self.elements[0]

    @property
    def unit(self) -> str:
        """Rate unit"""
        return self.elements[1]
