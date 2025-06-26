distancia_percorrida = float(input("Informe a distância percorrida em Km: "))
combustivel_gasto = float(input("Informe quanto gastou de combustível em litros: "))

media_por_litro = distancia_percorrida / combustivel_gasto

print(f"\nDistância percorrida: {distancia_percorrida} km.")
print(f"Combustível gasto: {combustivel_gasto} l.")
print(f"Comsumo médio: {media_por_litro:.2f} km/l.")