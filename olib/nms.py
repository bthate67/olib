# This file is placed in the Public Domain.

from obj import Default, Object
from zzz import js

class Names(Object):

    names = Default({
        "bus": [
            "bus.Bus",
            "Bus"
        ],
        "cfg": [
            "obj.Cfg"
        ],
        "client": [
            "hdl.Client"
        ],
        "command": [
            "evt.Command",
            "Command"
        ],
        "default": [
            "Default",
            "obj.Default"
        ],
        "enoclass": [
            "err.ENOCLASS",
            "ENOCLASS"
        ],
        "enofilename": [
            "err.ENOFILENAME",
            "ENOFILENAME"
        ],
        "enomore": [
            "err.ENOMORE",
            "ENOMORE"
        ],
        "enotimplemented": [
            "err.ENOTIMPLEMENTED",
            "ENOTIMPLEMENTED"
        ],
        "enotxt": [
            "err.ENOTXT",
            "ENOTXT"
        ],
        "enouser": [
            "err.ENOUSER"
        ],
        "event": [
            "evt.Event",
            "Event"
        ],
        "getter": [
            "prs.Getter"
        ],
        "handler": [
            "hdl.Handler"
        ],
        "loader": [
            "Loader",
            "ldr.Loader"
        ],
        "names": [
            "Names",
            "nms.Names"
        ],
        "o": [
            "obj.O"
        ],
        "obj": [
            "obj.Obj"
        ],
        "object": [
            "Object",
            "obj.Object"
        ],
        "objectlist": [
            "ObjectList",
            "obj.ObjectList"
        ],
        "option": [
            "prs.Option"
        ],
        "output": [
            "Output",
            "opt.Output"
        ],
        "repeater": [
            "clk.Repeater"
        ],
        "request": [
            "request.Request"
        ],
        "setter": [
            "prs.Setter"
        ],
        "skip": [
            "prs.Skip"
        ],
        "thr": [
            "thr.Thr"
        ],
        "timed": [
            "prs.Timed"
        ],
        "timer": [
            "clk.Timer"
        ],
        "token": [
            "prs.Token"
        ]
    })

    modules = Object({
    })

    inits =  Object({
        "bus": "bus",
        "clk": "clk",
        "dbs": "dbs",
        "edt": "edt",
        "err": "err",
        "evt": "evt",
        "fnd": "fnd",
        "hdl": "hdl",
        "itr": "itr",
        "ldr": "ldr",
        "nms": "nms",
        "obj": "obj",
        "opt": "opt",
        "prs": "prs",
        "tbl": "tbl",
        "thr": "thr",
        "tms": "tms",
        "trc": "trc",
        "trm": "trm",
        "url": "url",
        "utl": "utl",
        "zzz": "zzz"
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

    @staticmethod
    def getinit(mn):
        return Names.inits.get(mn, None)

