import re
regex = '[+-]?[0-9]+\.[0-9]+'
def find(floatnum):
    if (re.search(regex ,floatnum)):
        print(True)
    else:
        print(False)

if __name__ == '__main__':
    floatnum = "4"
    find(floatnum)
    floatnum = "5.000"
    find(floatnum)
    floatnum = "6.95"
    find(floatnum)
    floatnum = "0.6"
    find(floatnum)

import re
regex="[A-Z]+\d{4}+[A-Z]+"
def pan(pannum):
    if (re.search(regex, pannum)):
        print(True)
    else:
        print(False)
if __name__ == '__main__':
    pannum = "DECAA8056B"
    pan(pannum)
    pannum = " BWBPC6417P "
    pan(pannum)
    pannum = "JaMDD8000M"
    pan(pannum)
    pannum = "XABJT54321"
    pan(pannum)