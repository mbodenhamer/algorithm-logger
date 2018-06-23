from nose.tools import assert_raises

from algorithm_logger import Arg, Kwarg, ValidationError
from algorithm_logger.spec import SpecBase

#-------------------------------------------------------------------------------
# SpecBase

def test_specbase():
    spec = SpecBase(type=int, name='foo')
    assert_raises(NotImplementedError, spec.find_value, (), {})

#-------------------------------------------------------------------------------
# Arg

def test_arg():
    arg = Arg('a', 1, int)
    assert arg.find_value((1, 2, 3), {}) == 2
    assert arg.find_value((1,), {}) is None
    assert arg.name == 'a'

    arg = Arg('a', 1, int, required=True)
    assert arg.find_value((1, 2, 3), {}) == 2
    assert_raises(ValidationError, arg.find_value, (1,), {})
    assert arg.type is int

#-------------------------------------------------------------------------------
# Kwarg

def test_kwarg():
    kwarg = Kwarg('a', float)
    assert kwarg.find_value((), dict(a=1.1, b=2.2)) == 1.1
    assert kwarg.find_value((), dict(b=2.2)) is None
    assert kwarg.name == 'a'

    kwarg = Kwarg('a', float, required=True, name='b')
    assert kwarg.find_value((), dict(a=1.1, b=2.2)) == 1.1
    assert_raises(ValidationError, kwarg.find_value, (), dict(b=2.2))
    assert kwarg.type is float
    assert kwarg.name == 'b'

#-------------------------------------------------------------------------------

if __name__ == '__main__': # pragma: no cover
    from syn.base_utils import run_all_tests
    run_all_tests(globals(), verbose=True, print_errors=False)
