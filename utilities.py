def clear_screen():
    import os
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

def input_integer(prompt):
    while True:
        try:
            answer = int(input(prompt))

            if answer < 1:
                raise IndexError

            break
        except IndexError:
            prompt = "-> Introduzca un número entero mayor o igual que 1: "
        except ValueError:
            prompt = "-> Introduzca un número entero: "

    return answer
