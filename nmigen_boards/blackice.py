from torii_boards.blackice import *
from torii_boards.blackice import __all__


import warnings
warnings.warn("instead of nmigen_boards.blackice, use amaranth_boards.blackice",
              DeprecationWarning, stacklevel=2)
