def calculadora(a:int,b:int,op:str)->int:
    
    def sumar()->int:
        return a+b

    def restar()->int:
        return a-b

    def mult()->int:
        return a*b
    
    if op == 'sumar':
        return sumar
    elif op == 'restar':
        return restar
    elif op == 'mult':
        return mult

def main():
    print(f'Resultado de la Suma: {calculadora(1,2,"sumar")()}')
    print(f'Resultado de la Resta: {calculadora(1,2,"restar")()}')
    print(f'Resultado de la Multiplicacion: {calculadora(1,2,"mult")()}')

main()