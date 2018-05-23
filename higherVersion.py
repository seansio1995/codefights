def higherVersion(ver1, ver2):
    if "." not in ver1 and "." not in ver2:
        return int(ver1)>int(ver2)
    v1=list(map(int,ver1.split(".")))
    v2=list(map(int,ver2.split(".")))

    for i in range(len(v1)):
        if v1[i]>v2[i]:
            return True
        elif v1[i]<v2[i]:
            return False
        else:
            continue
    return False
