#program membuat function

def akar_kuadrat(a,b,c):  
    x_1 = (-b + (b**2 - 4*a*c )**(1/2))/ 2 * a
    x_2 = (-b - (b**2 - 4*a*c )**(1/2))/ 2 * a
    print("x1 = ", x_1)
    print("x2 = ", x_2)
akar_kuadrat(1,-6,8)    

def akar(x):
    akar = x**(1/2)
    print(f"akar dari {x} adalah {akar}")
akar(16)

