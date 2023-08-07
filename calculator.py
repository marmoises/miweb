def calculadora(a:int,b:int,op:str)->int:
    print('Inicio de la Calculadora')
    def sumar()->int:
        return a+b

    def restar()->int:
        return a-b

    def mult()->int:
        return a*b
    
    def pot()->int:
        return a**b
    
    def division()->int or float or None:
        try:
            return a/b
        except ZeroDivisionError as e:
            print(f'Error: {e}')

    def obtener_resto()->int:
        try:
            return a%b
        except Exception as e:
            print(f'Error: {e}')
    
    if op == 'sumar':
        return sumar
    elif op == 'restar':
        return restar
    elif op == 'mult':
        return mult
    elif op == 'division':
        return division
    elif op == 'pot':
        return pot
    elif op == 'resto':
        return obtener_resto