import builtins
import re
def valid(blacklist):
    functions=[]
    for fn in dir(builtins):
        if re.search("["+re.escape(blacklist)+"]",fn) == None:
            functions.append(fn)
    return functions
