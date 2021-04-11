from .bch import BCH
from .bsty import BSTY
from .btc import BTC
from .gzro import GZRO
from .ltc import LTC
from .lbry import LBC

COINS = {"BTC": BTC, "BCH": BCH, "LTC": LTC, "GZRO": GZRO, "BSTY": BSTY, "LBC": LBC}

__all__ = list(COINS.keys()) + ["COINS"]
