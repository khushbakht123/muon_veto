from __future__ import annotations

import numpy as np
from pygama.dsp.errors import DSPFatal

from numba import guvectorize

from pygama.dsp.utils import numba_defaults_kwargs as nb_kwargs

@guvectorize(
    ["void(float32[:], float32, int32[:])", "void(float64[:], float64, int64[:])"], 
#    ["void(float32[:], float32, int32[:])"],
    "(),()->()",
    **nb_kwargs,
)

def trigger_thr(heights: np.ndarray, value: float, triggered: np.ndarray) -> None:
      
    
#    triggered[:] = np.nan
 
#    if np.isnan(heights).any() or np.isnan(value):
#        return

    triggered[0] = 1 if heights[0] > value else 0

    
#    triggered = np.zeros(len(heights))
#    triggered[0]=heights[0]
    

#    for i in range(0,len(heights), 1):
#        
#        if(heights[i] > value):
#            triggered[i]=1.0
