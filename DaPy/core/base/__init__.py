from ._sheet import SeriesSet, Frame
from ._matrix import Matrix
from ._function import (is_seq, is_iter, is_math, is_value, get_sorted_index)
##from ._numeric import (cov, corr, frequency, quantiles, distribution,
##                     describe, mean)
from ._numeric import _sum as sum

__all__ = ['SeriesSet', 'Frame', 'Matrix', # 2-dim data structures
           'is_seq', 'is_iter', 'is_math', 'is_value', # funcs for judgement data
           'get_sorted', ] # funcs for data process
          # 'cov', 'corr', 'frequency', 'quntiles', # funcs for statistic
           #'distribution', 'describe', 'mean', 'sum']
