from .rintf import calcOutlierScore
from rpy2.robjects.packages import importr

lib = importr('IsolationForest')
