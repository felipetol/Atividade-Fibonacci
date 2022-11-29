"""
Código para a avaliação de Lógica Aplicada para a professora Tania Camila
Alunos:
Everton Kenji Ikeda
Felipe Leite Toledo
Pedro Lucas Tavares Noda

O trabalho proposto envolvia codificar duas funções que devolvessem o n-ésimo valor na sequência da Fibonacci, uma que
fizesse de forma iterativa e outra que fizesse de maneira recursiva
"""


# ITERATIVA
def fibonacci_iterativo(num):
    if num > 0:
        fib = []
        count_iterativo = 0
        for n in range(num):
            if n < 2:
                fib.append(1)
            else:
                fib.append(fib[n-1] + fib[n-2])
            count_iterativo += 1
        return f"Fibonacci sequence number: {fib[-1]}\nCount: {count_iterativo}"
    else:
        return f"Fibonacci sequence number: None\nCount: 0"


count_recursivo = 0


# RECURSIVA
def fibonacci_recursivo(num):
    global count_recursivo
    count_recursivo += 1
    if num == 0 or num == 1:
        return num
    else:
        return fibonacci_recursivo(num - 1) + fibonacci_recursivo(num - 2)


print("Forma iterativa ")
print(fibonacci_iterativo(int(input("Insert number: "))))

print("\nForma recursiva ")
print(str(f"Fibonacci sequence number: {fibonacci_recursivo(int(input('Insert number: ')))}\nCount: {count_recursivo}"))

