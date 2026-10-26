import numpy as np

def solve(x):
    ret = []
    mi = min(x)
    ma = max(x)
    for i in range(len(x)):
        nume = x[i]-mi
        denom = ma-mi
        try:
            res = nume/denom
            ret.append(res)
        except ZeroDivisionError as e:
            ret.append(float(0))
    return np.array(ret)
