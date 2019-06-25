matriz = [1,2,4],[3,2,8],[5,4,9]

temp = 0
puntero = 0


for i in range (len(matriz)):
    temp += matriz[i][puntero]
    puntero += 1

print("La suma diagonal de la matriz es:",temp) 

num = input("Introduce resultado de la matriz:")
num = int(num)
if num == 0:
    print ("Este número es par.")
elif num%2 == 0:
    print ("Este numero es par")
else:
    print ("Este numero es impar")
