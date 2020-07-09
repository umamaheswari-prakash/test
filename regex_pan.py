import re
regex='[A-Z]{5}[0-9]{4}[A-Z]{1}'
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
