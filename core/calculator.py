correct_operators = ['+', '-', '/', '*', '**']

def calculator(a, b, operation):
    if operation == '+':
        return a + b
    else:
        if operation == '-':
            return a - b
        else:
            if operation == '/':
                return a / b
            else:
                if operation == '*':
                    return a * b
                else:
                    if operation == '**':
                        return a ** b

if __name__ == '__main__':
    
    while True:
        try:
            a = int(input('Введите число: '))
            break
        except ValueError:
            print('errrror, введи число')
            
    while True:
        try:
            b = int(input('Введите число: '))
            break
        except ValueError:
            print('errrror, введи число')
            
    while True:
        try:
            operation = input('Введите операцию: ')
            if operation in correct_operators:
                break
            else:
                print('errrror, введи что-то из списка +, -, /, *, **')
        except:
            print('ooops') 
            

    print('Результат: ', calculator(a, b, operation), '   PROFIT!')
    
