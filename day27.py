#program function
def f(x):
    hasil = 2*(x**3) + 2*x + 15/x
    print("f(%d) = 2(%d)^3 + 2(%d) + 15/(%d)" %(x,x,x,x),
          "\n", 7*" ","= ", hasil)
f(x=3)