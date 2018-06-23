
#-------------------------------------------------------------------------------


class Event(object):
    pass


#-------------------------------------------------------------------------------


class FunctionCall(Event):
    def __init__(self, spec):
        self.spec = spec
        self.parameters = {}

    def __call__(self, args, kwargs):
        ret = self.copy()
        for arg in self.spec:
            ret.parameters[arg.name] = arg.find_value(args, kwargs)
        return ret

    def copy(self):
        return type(self)(self.spec)


#-------------------------------------------------------------------------------


class LoopIteration(Event):
    pass


#-------------------------------------------------------------------------------
# __all__

__all__ = ('Event', 'FunctionCall', 'LoopIteration',)

#-------------------------------------------------------------------------------
