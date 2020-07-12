def outside(function1):
    def outer():
        return "outer "+ function1() +" outer "
    return outer

def inside(function2):
    def inner():
        return "inner "+function2()+" inner"
    return inner
@outside
@inside
def string():
    return 'inside'
print(string())



