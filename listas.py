nombres = ['Jaaciel', 'Arturo', 'Alexia', 'Isabella']
edades = [26, 7, 27, 2]
apellidos = [
    ['Briseño', 'Espinoza'], ['Briseño', 'Arreola'],
    ['Arreola', 'Araujo'], ['Briseño', 'Arreola']
]
# print(nombres)
# nombres.append('Lupita')
# print(nombres)
# # nombres.extend('Lupita')
# # print(nombres)
# nombres.pop()
# print(nombres)
# nombres.insert(0,'Erik')
# print(nombres)
# print(len(nombres))
# print(nombres[-1])
# print(nombres[0:2])


# print(apellidos)
# print(apellidos[0])
# print(apellidos[0][0])

print(max(edades))
print(min(edades))
print(sorted(edades))

# edades.remove(2)
# print(edades)


for nombre in nombres:
    print(nombre)
    
pares = []
for i in range(100):
    if i % 2 == 0:
        pares.append(i)

print(pares)

pares = [i for i in range(100) if i % 2 == 0]
print(pares)