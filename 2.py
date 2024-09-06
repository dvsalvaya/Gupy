def Fibonacci(n):
    sequencia = [0,1]
    i = 0
    while sequencia[-1] < n:
        i += 1
        sequencia.append(sequencia[i]+sequencia[i-1])
        if sequencia[-1] == n:
            return "Pertence"
    return "Não pertence"
