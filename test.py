from gb2tiny import parse
from coverageX import compare

parse("Pacific.gb","Pacific.json")
parse("RcPescado.gb","RcPescado.json")
compare("Pacific.json", "RcPescado.json")
