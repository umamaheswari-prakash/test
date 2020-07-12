#1.MODIFIED PROGRAM
def function_outside():
    msg="Hi"
    def function_inside():
        msg="Hello"
        print(msg)
    return function_inside()
function_outside()
print("Hello")
#2.ERROR CORRECTION
def f(x):
    def g(y=x):
        return y
    return g
a=5
b=1
print(f(a)(b))

