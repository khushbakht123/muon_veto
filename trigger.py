from __future__ import annotations

import numpy as np
from pygama.dsp.errors import DSPFatal

from numba import guvectorize
from pygama.dsp.utils import numba_defaults_kwargs as nb_kwargs

@guvectorize(
    ["void(float32, float32, int32)", "void(float64, float64, int64)"],
    "(n),()->(n)",
    **nb_kwargs,
)
def trigger(heights: float, value: float, triggered: int) -> None:
    
    triggered = int(heights > value)

    

'''@guvectorize(["void(float64[:], float64, int64[:])","void(float64[:], float64, int64[:])"], '(n),()->(n)')

def trigger(x: np.ndarray, y: float, triggered: np.ndarray):
    
    for i in range(x.shape[0]):
        triggered[i] = int(x[i] > y)'''


'''Json code-implementation:

"triggered":{
      "function": "trigger",
      "module": "pygama.dsp.processors",
      "args": ["trigger_heights", "15.0", "triggered"],
      "unit": "ADC"
    }'''