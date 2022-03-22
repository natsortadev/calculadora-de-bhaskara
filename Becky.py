while (True):
    print("> olá! meu nome é becky.")
    print("> estou aqui para ajudar com as equações de segundo grau. B.)")
    print("> primeiro, me dê o valor de 'a'...")
    a = float(input())
    print("> ...o valor de 'b'...")
    b = float(input())
    print("> ...e, por último, me dê o valor de 'c'.")
    c = float(input())
    print("> vou calcular para você!")
    print("> [Becky está pensando...]")
    print("> aqui está!")
    
    float(a)
    float(b)
    float(c)
    
    #bhaskara
    #{(b * -1) + {[(b ** 2) - (4 * a * c)] ** 0.5}} / (2 * a)
    x1 = ((b * -1) + (((b ** 2) - (4 * a * c)) ** 0.5)) / (2 * a)
    x2 = ((b * -1) - (((b ** 2) - (4 * a * c)) ** 0.5)) / (2 * a)
    print(f"x' = {x1}")
    print(f"x'' = {x2}")
    #delta
    delta = (b ** 2) - (4 * a * c)
    print(f"delta é {delta}")