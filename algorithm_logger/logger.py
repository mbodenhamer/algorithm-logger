from collections import defaultdict
from functools import wraps
from syn.base import Attr, Base, init_hook

from .event import FunctionCall

#-------------------------------------------------------------------------------


class Logger(Base):
    _attrs = dict(logging_enabled = Attr(bool, True),
                  decoration_enabled = Attr(bool, True),
                  events = Attr(dict, internal=True)
                  )

    @init_hook
    def _init(self):
        if not hasattr(self, 'events'):
            self.events = defaultdict(list)

    def disable(self):
        self.logging_enabled = False

    def enable(self):
        self.logging_enabled = True

    def log_decorator(self, spec, before=True, after=False, name=None, log_return=True):
        def decorator(f):
            if not self.decoration_enabled:
                return f

            event_type_name = name
            if name is None:
                event_type_name = f.__name__
            event_type = FunctionCall(spec)

            @wraps(f)
            def func(*args, **kwargs):
                if self.logging_enabled:
                    event = event_type(args, kwargs)
                ret = f(*args, **kwargs)
                if self.logging_enabled:
                    if log_return:
                        event.return_value = ret
                    self.record_event(event_type_name, event)
                return ret
            return func
        return decorator

    def log_event(self):
        pass

    def log(self, *args, **kwargs):
        # Determine what the context is from args and kwargs, then call log_decorator or log_event
        # But this also needs to be fast, so strike a balance between magic and speed
        return self.log_decorator(*args, **kwargs)

    def record_event(self, name, event):
        self.events[name].append(event)


#-------------------------------------------------------------------------------
# __all__

__all__ = ('Logger',)

#-------------------------------------------------------------------------------
