from rpy2.robjects import r, DataFrame, FloatVector
from collections import OrderedDict

def calcOutlierScore(lists):
    lists = zip(*lists)
    rlists = list(map(FloatVector, lists))
    d = OrderedDict(zip(map(str, range(len(rlists))), rlists))
    data = DataFrame(d)
    tr = r['IsolationTrees'](data, rFactor=0)
    sc = r['AnomalyScore'](data, tr)
    return list(dict(zip(sc.names, list(sc)))['outF'])
