def calculadora(a:int,b:int,op:str)->int:
    print('Inicio de la Calculadora')
    def sumar()->int:
        return a+b

    def restar()->int:
        return a-b

    def mult()->int:
        return a*b
    
    def division()->int or float or None:
        try:
            return a/b
        except ZeroDivisionError as e:
            print(f'Error: {e}')
    
    if op == 'sumar':
        return sumar
    elif op == 'restar':
        return restar
    elif op == 'mult':
        return mult
    elif op == 'division':
        return division

def main():
    print(f'Resultados: ')
    print(f'Resultado de la Suma: {calculadora(1,2,"sumar")()}')
    print(f'Resultado de la Resta: {calculadora(1,2,"restar")()}')
    print(f'Resultado de la Multiplicacion: {calculadora(1,2,"mult")()}')
    print(f'Resultado de la Division: {calculadora(1,2,"division")()}')

main()