
## Universidade Estadual do Norte do Paraná - Campus Luiz Meneghel

### Trabalho de Computação Simbólica - Máquina Diferencial de Charles Babbage (4º ano do curso de Ciência da Computação)

##### Docente: Rafael de Lima Aguiar
##### Discente: Melissa Francielle dos Santos 

-----

## 1. Sobre: 
A Máquina Diferencial de Charles Babbage foi uma calculadora mecânica projetada para calcular funções polinomiais e imprimir tabelas matemáticas de forma automática. Babbage, considerado o "pai da computação", concebeu a máquina na década de 1820, mas a tecnologia da época dificultou sua construção completa. 

![Máquina Diferencial](https://hermes.dio.me/assets/articles/5af6e95a-78ad-41f5-b685-9860765cb725.jpg)

----
## 2. Requisitos do Trabalho 
O trabalho em questão deve apresentar o funcionamento da Máquina Diferencial de Charles Babbage de forma que siga os seguintes requisitos:

- Trabalho individual
- O artefato deve ser um script em PYTHON
- Sem comentários

O trabalho também apresenta diferentes notas para diferentes tipos de implementação sendo elas:
*  [70] Fazer a máquina responder ao próximo valor de entrada da sequência que
foi inserida para um polinômio de grau 2: considerando o exemplo do anexo, seu
programa deve encontrar o valor para utilizando a tabela de diferenças. 𝑥 = 0, 5

* [80] Fazer a máquina responder ao próximo valor de entrada da sequência que
foi inserida para um polinômio de qualquer grau: encontrar o próximo valor da sequência utilizando a tabela para um polinômio de qualquer grau.

*  [90] Fazer a máquina gerar o resultado de qualquer valor de entrada que esteja
no padrão dos valores de utilizados como entrada para um polinômio de grau 2:𝑥
utilizando o exemplo em anexo, poderia ser pedido para calcular o resultado para
, por exemplo.𝑥 = 0, 9

* [100] Fazer a máquina gerar o resultado de qualquer valor de entrada que esteja
no padrão dos valores de utilizados como entrada para um polinômio de qualquer𝑥
grau.

---

## 3.  Funcionamento do Código da Máquina Diferencial
Este programa implementa a máquina diferencial para o cálculo de valores de polinômios e gera tabelas das diferenças finitas, utilizando o método dado por Babbage. Apresentando a seguir o funcionamento do código, e suas principais funcões:
---

### 1. Função resultado
 Essa função é responsável pelos resultados, onde ela percorre de forma recursiva a tabela de diferenças, analisando quando o último elemento da linha for igual ao último da última linha e assim retornar os valores. Caso não seja verdadeira a condição ele segue subtraindo até que se chegue ao valor desejado.

```python
def resultado(diferenca, i): 
    if diferenca[i][-1] == diferenca[-1][-1]:
        return diferenca[i][-1]
    else:
        return diferenca[i][-1] - resultado(diferenca, i + 1)
```

### 2. Função de Babbage
A função dada como `func_babbage` é responsável por contruir a tabela de diferenças finitas, onde recebe os eixos X e Y, e a cada interação estará criando uma nova linha de diferenças. 
```python
def func_babbage(y):
    tamanho = len(y)
    tabela_resultados = [y]
    for i in range(tamanho - 1):
        nova_linha = []
        for j in range(tamanho - i - 1):
            calculo = tabela_resultados[i][j] - tabela_resultados[i][j + 1]
            nova_linha.append(round(calculo, 10))
        tabela_resultados.append(nova_linha)
    return tabela_resultados
```

Apresentando um exemplo de saída possível desse tipo de código. Exemplo de saída:

```
Pn(x): [10, 15, 22, 31]
dif 0: [-5, -7, -9]
dif 1: [2, 2]
dif 2: [0]
```

### Função polinomios
A função dos polinomios é básica, e apresenta apenas o calculo do valor de um polinomio no ponto do eixo X. É uma função com funcionamneto simples e rápido. 

```python
def func_polinomios(x, coeficientes, grau):
    calculo_soma = 0 
    auxiliar = 0 
    while (auxiliar <= grau):
        calculo_soma += coeficientes[auxiliar] * (x ** auxiliar)
        auxiliar += 1
    return calculo_soma
```

### Função Main
A main estará realizando a organização e execução do programa, sendo feita inserção dos elementos pelo usuário como: grau do polinômio e seus coeficientes. Além disso, o usuário define o valores inicial do eixo X e o incremento que será utilizado para gerar os pontos da sequência, determinando o valor especificado pelo usuário é assim avaliado e calculado a lista de valores dada para ` Pn(x)`  e criada a tabela de diferenças e assim mostrando os resultados obtidos por meio do funcionamento do código. 
```python
def main():
    coeficiente = list() 
    print(f'Insira qual o grau desse polinomio: ')
    grau = int(input())
    ...
```

O código em questão busca atender o requisito de valor 90 dado nas especificações deste trabalho no qual:
 O código deve fazer com que a máquina gere o resultado de qualquer valor de entrada que esteja no padrão dos valores utilizados com entrada para um polinômio de grau 2:x, utilizando o exemplo em anexo, poderia ser pedido para calcular por exemplo o resultado para x = 0.9.
