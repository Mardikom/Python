# regular expression

import re

строка = "65+9/55/9*7-4+3-4-5*4"

print(re.split("[-/*+]", строка))

