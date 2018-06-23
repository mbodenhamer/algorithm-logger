from algorithm_logger import Arg, Logger

#-------------------------------------------------------------------------------
# Logger

def test_logger():
    logger = Logger()

    @logger.log(dict(a = Arg(0, int)))
    def foo(a):
        return a + 1

    assert logger.events['foo'] == []
    foo(1)
    assert len(logger.events['foo']) == 1
    event = logger.events['foo'][0]
    assert event.return_value == 2

    foo(2)
    assert logger.events['foo'][-1].return_value == 3

    logger.disable()
    foo(3)
    assert logger.events['foo'][-1].return_value == 3

    logger.enable()
    foo(3)
    assert logger.events['foo'][-1].return_value == 4

    logger.decoration_enabled = False
    
    @logger.log(dict(a = Arg(0, int)))
    def bar(a):
        return a * 2
    
    bar(3)
    assert logger.events['bar'] == []

    foo(10)
    assert logger.events['foo'][-1].return_value == 11

    logger.log_event()

#-------------------------------------------------------------------------------

if __name__ == '__main__': # pragma: no cover
    from syn.base_utils import run_all_tests
    run_all_tests(globals(), verbose=True, print_errors=False)
