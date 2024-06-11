def transform(command,use_eval=False):
    result=[]
    for c in command:
        n=[]
        for i in range(ord(c)):
            n.append("(()==())")
        result.append("chr("+"+".join(n)+")")
    if use_eval:
        return "eval("+'+'.join(result)+")"
    return '+'.join(result)

def transform2(command,use_eval=False):
    result=[]
    for c in command:
        n=[]
        for i in range(ord(c)):
            n.append("all(())")
        result.append("chr("+"+".join(n)+")")
    if use_eval:
        return "eval("+'+'.join(result)+")"
    return '+'.join(result)
