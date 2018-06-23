from syn.base import Attr, Base
from syn.five import STR

from .base import ValidationError

#-------------------------------------------------------------------------------
# SpecBase


class SpecBase(Base):
    _attrs = dict(type = Attr(type, doc='The type of this argument'),
                  required = Attr(bool, False, doc='If true, will throw an error if argument is not present'))
    _opts = dict(init_validate = True)

    def find_value(self, args, kwargs):
        raise NotImplementedError


#-------------------------------------------------------------------------------
# Arg


class Arg(SpecBase):
    '''Descriptor of a positional argument.'''
    _attrs = dict(index = Attr(int, doc='The index of this argument in *args'))
    _opts = dict(args = ('index', 'type'))


    def find_value(self, args, kwargs):
        if len(args) <= self.index:
            if self.required:
                raise ValidationError('Positional argument (index={}) '
                                      'not present'.format(self.index))
            return
        return args[self.index]


#-------------------------------------------------------------------------------
# Kwarg


class Kwarg(SpecBase):
    '''Descriptor of a keyword-only argument.'''
    _attrs = dict(key = Attr(STR, doc='The key of this argument in **kwargs'))
    _opts = dict(args = ('key', 'type'))

    def find_value(self, args, kwargs):
        if self.key not in kwargs:
            if self.required:
                raise ValidationError('Keyword argument (key={}) '
                                      'not present'.format(self.key))
            return
        return kwargs[self.key]


#-------------------------------------------------------------------------------
# __all__

__all__ = ('Arg', 'Kwarg')

#-------------------------------------------------------------------------------
