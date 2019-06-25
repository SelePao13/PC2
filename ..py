matriz = [1,2,4],[3,2,8],[5,4,9]
matriz_2 = [4,5,6],[3,2,5],[1,9,4]
matriz_3 =[8,2,9],[6,7,2],[1,7,3]

temp = 0
puntero = 0

for i in range (len(matriz)):
    temp += matriz[i][puntero]
    puntero += 1

if matriz_2:
    for x in range (len(matriz_2)):
        temp += matriz_2[x][puntero]
    puntero += 1 


for a in range (len(matriz_3)):
    temp += matriz_3[a][puntero]
    puntero += 1

print("La suma diagonal de la matriz es:",temp)

num = input("Introduce resultado de la matriz: ")
num = int(num)
if num == 0:
    print ("Este número es par.")
elif num%2 == 0:
    print ("Este numero es par")
else:
    print ("Este numero es impar")

