
#-------------------------------------------------------------------------------


class Event(object):
    pass


#-------------------------------------------------------------------------------


class FunctionCall(Event):
    def __call__(self, args, kwargs):
        # copy self, log args and kwargs according to spec, then return copy
        ret = self.copy()
        return ret

    def copy(self):
        return type(self)()

    @classmethod
    def from_spec(cls, spec):
        return cls()


#-------------------------------------------------------------------------------


class LoopIteration(Event):
    pass


#-------------------------------------------------------------------------------
# __all__

__all__ = ('Event', 'FunctionCall', 'LoopIteration',)

#-------------------------------------------------------------------------------
