# This file is placed in the Public Domain.

from obj import Default, Object
from zzz import js

class Names(Object):

    names = Default({
    })

    modules = Object({
    })

    @staticmethod
    def add(func):
        Names.modules[func.__name__] = func.__module__

    @staticmethod
    def getnames(nm, dft=None):
        return Names.names.get(nm, dft)

    @staticmethod
    def getmodule(mn):
        return Names.modules.get(mn, None)

