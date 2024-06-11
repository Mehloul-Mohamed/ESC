def mess(command,use_eval=False):
    result=""
    for c in command:
        result+="chr("
        result+="(()==())+"*(ord(c)-1)
        result+="(()==()))+"
    if use_eval:
        return "eval("+result[:-1]+")"
    return result[:-1]

def mess_all(command,use_eval=False):
    result=""
    for c in command:
        result+="chr("
        result+="all(())+"*(ord(c)-1)
        result+="all(()))+"
    if use_eval:
        return "eval("+result[:-1]+")"
    return result[:-1]
