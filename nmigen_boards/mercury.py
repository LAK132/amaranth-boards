from torii_boards.mercury import *
from torii_boards.mercury import __all__


import warnings
warnings.warn("instead of nmigen_boards.mercury, use amaranth_boards.mercury",
              DeprecationWarning, stacklevel=2)
