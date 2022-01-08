#program meencari akar kuadrat persamaan

nilai_a = int(input("Masukkan nilai a :"))
nilai_b = int(input("Masukkan nilai b :"))
nilai_c = int(input("Masukkan nilai c :"))

x_1 = (-nilai_b + (nilai_b * nilai_b - 4*nilai_a *nilai_c )**(1/2))/ 2 * nilai_a
x_2 = (-nilai_b - (nilai_b * nilai_b - 4*nilai_a *nilai_c )**(1/2))/ 2 * nilai_a

print("x1 = ", x_1)
print("x2 = ", x_2)