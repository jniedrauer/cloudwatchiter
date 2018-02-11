# pylint: disable-all

import pytest
from cloudwatchiter.abc_expression import AbstractExpression

def abc(cls):
    cls.__abstractmethods__ = set()
    cls.element_count = 2
    return cls

def test_invalid_init():
    cls = abc(AbstractExpression)
    with pytest.raises(ValueError):
        expr = cls('foo')

def test_cron_init():
    cls = abc(AbstractExpression)
    expr = cls('cron(1 2)')
    assert expr.type == 'cron'

def test_rate_init():
    cls = abc(AbstractExpression)
    expr = cls('rate(1 2)')
    assert expr.type == 'rate'

def test_invalidate_elements():
    with pytest.raises(ValueError):
        AbstractExpression.validate_elements(
            elements=['1'],
        )

def test_validate_elements():
    elements = AbstractExpression.validate_elements(
        elements=['1', '2'],
    )
    assert elements == ['1', '2']

def test_elements():
    cls = abc(AbstractExpression)
    expr = cls('cron(1 2)')
    assert expr.elements == ['1', '2']
