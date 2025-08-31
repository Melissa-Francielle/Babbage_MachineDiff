
def resultado (diferenca, i): 
    if diferenca[i][-1] == diferenca[-1][-1]:
        return diferenca[i][-1]
    else:
        return diferenca[i][-1] - resultado(diferenca, i + 1)
    

def func_babbage(y):
    tamanho = len(y)
    tabela_resultados = [y]
    for i in range(tamanho - 1):
        nova_linha = []
        for j in range (tamanho - i - 1):
            calculo = tabela_resultados[i][j] - tabela_resultados[i][j + 1]
            nova_linha.append(round(calculo, 10))
        tabela_resultados.append(nova_linha)
    return tabela_resultados


def func_polinomios(x, coeficientes, grau):
    calculo_soma = 0 
    auxiliar = 0 
    while (auxiliar <= grau):
        calculo_soma += coeficientes[auxiliar] * (x ** auxiliar)
        auxiliar += 1
    return calculo_soma

def main ():
    coeficiente = list() 
    print(f'Insira qual o grau desse polinomio: ')
    grau = int(input())
    auxiliar_grau = grau 

    for i in range(0, grau + 1):
        print(f'Insira o valor para o coeficiente {i}: ')
        valor_coeficiente = int(input())
        auxiliar_grau -= 1
        coeficiente.append(valor_coeficiente)

    abscissas = list() 
    print(f'Insira o valor inicial do eixo x: ')
    valor_x = float(input())
    print(f'Insira o valor de quanto deve ser incrementado os valores de x: ')
    proximo = float(input())
    incremento = valor_x

    print(f'\nQual o valor da sequência que gostaria de ser calculado?')
    print(f'Insira aqui: ')
    valor_sequencia = float(input())

    for i in range(0, 100):
        abscissas.append(incremento)
        incremento += proximo
        if abs(incremento - valor_sequencia) < 1e-10:  
            break
        if i==99 and abscissas !=valor_sequencia:
            print(f'Entrada não aceita, por favor tente novamente.')
            exit()

    print('-'*30)

    ordenada = [round(func_polinomios(x, coeficiente, grau), 6) for x in abscissas]
    maquina_diferencial = func_babbage(ordenada)
    print(f'Entrada (x): {abscissas}')
    print(f'Pn(x): {ordenada}')
    print('')

    print('-'*30)

    print(f'Tabela de Diferenças: ')
    for coluna, linha in enumerate(maquina_diferencial):
        if coluna == 0:
            print(f"Pn(x): {linha}")
        else:
            print(f"dif {coluna-1}: {linha}")
        
    print(f'\nPolinômio: ', end='')
    print('\n')
    print(f'Resultado para a entrada dada: {valor_sequencia}')

    for i, valor in enumerate(coeficiente):
        if valor >= 0 and i != 0 and i + 1 != len(coeficiente):
            print(f'+{valor}x^{grau - i}', end='')
        if valor >= 0 and i == 0:
            print(f'{valor}x^{grau - i}', end='')
        if valor < 0:
            print(f'{valor}x^{grau - i}', end='')
        if i + 1 == len(coeficiente):
            if valor >= 0:
                print(f'+{valor}', end=' é ')
            if valor < 0:
                print(valor, end=' é ')

    res = func_polinomios(valor_sequencia, coeficiente, grau)
    print(f"\nO resultado para x={valor_sequencia} no polinômio é {round(res, 6)}")

if __name__ == "__main__":
    main()
