def inverte(palavra):
    list(palavra)
    invertida=[]
    for i in range(len(palavra)):
        invertida.append(palavra[-i-1])

    return invertida


