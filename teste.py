def funcao(temp):
    print(f"-> Chamando funcao({temp})")  # Antes da chamada recursiva
    if temp == 0:
        print(f"<- Retornando 0 (caso base)")
        return 0
    else:
        resultado_parcial = funcao(temp - 1)
        resultado = temp + resultado_parcial
        print(f"<- Retornando {temp} + {resultado_parcial} = {resultado}")
        return resultado

inicial = 5
final = funcao(inicial)
print(f"\nResultado final: {final}")