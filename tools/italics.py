def italize(command):
    result=''
    for c in command:
        n=ord(c)
        if (n in range(65,91)):
            result+=chr(119912+n-65)
        elif (n in range(97,123)):
            result+=chr(119938+n-97)
        else:
            result+=c
    return result
