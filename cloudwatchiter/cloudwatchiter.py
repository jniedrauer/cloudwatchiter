"""Returns an instance of Cron or Rate"""


from .cron import Cron
from .rate import Rate


def cloudwatchiter(expression: str) -> object:
    """Factory function for expression classes"""
    if expression.startswith('cron'):
        return Cron(expression)
    elif expression.startswith('rate'):
        return Rate(expression)
    else:
        raise ValueError('Invalid expression')
