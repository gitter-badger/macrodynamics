try:
    import pyximport
    pyximport.install()
except ImportError:
    pass

from .structure import *
from .dynamics import *
from .util import *
