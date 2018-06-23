from algorithm_logger import Arg, FunctionCall

#-------------------------------------------------------------------------------

def test_functioncall():
    fc = FunctionCall([Arg('a', 0, int)])
    fc1 = fc((1, 2, 3), {})
    assert fc.parameters == dict()
    assert fc1.parameters == dict(a=1)

#-------------------------------------------------------------------------------

if __name__ == '__main__': # pragma: no cover
    from syn.base_utils import run_all_tests
    run_all_tests(globals(), verbose=True, print_errors=False)
