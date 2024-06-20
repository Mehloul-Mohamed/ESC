# Not a complete implementation. Still needs more work
def italize(command):
    result=''
    for c in command:
        n=ord(c)
        if (n in range(65,91)) or (n in range(97,123)):
            result+=chr(119938+n-97)
        else:
            result+=c
    return result
