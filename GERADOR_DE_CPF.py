# Importações
from random import randint


# Funções
def getNumberState(initial_state):  # Retorna o número do estado pela sigla ou None.
    STATES = [
        {'number': 0, 'initial': ['RS']},
        {'number': 1, 'initial': ['DF', 'MT', 'MS', 'TO']},
        {'number': 2, 'initial': ['AM', 'PA', 'RR', 'AP', 'AC', 'RO']},
        {'number': 3, 'initial': ['CE', 'MA', 'PI']},
        {'number': 4, 'initial': ['PB', 'PE', 'AL', 'RN']},
        {'number': 5, 'initial': ['BA', 'SE']},
        {'number': 6, 'initial': ['MG']},
        {'number': 7, 'initial': ['RJ', 'ES']},
        {'number': 8, 'initial': ['SP']},
        {'number': 9, 'initial': ['PR', 'SC']},
    ]

    for state in STATES:
        if initial_state.upper() in state['initial']:
            return state['number']

    return None


def inputAmount(text):  # Retorna um inteiro maior que 0.
    while True:
        try:
            n = int(input(text))
        except ValueError:
            print('[ERRO]: Informe um inteiro.')
        else:
            if n > 0:
                return n
            print('[ERRO]: Informe um valor maior que 0.')


def inputState(text):  # Retorna a sigla do estado ou None.
    while True:
        initial_state = input(text).strip()

        if initial_state == '':
            return None

        number_state = getNumberState(initial_state)
        if number_state is not None:
            return number_state

        print('[ERRO]: Sigla de estado inválida.')


def inputYesOrNo(text):
    while True:
        choice = input(text).upper()
        if choice in ['S', 'N']:
            return choice == 'S'

        print('[ERRO]: Informe apenas [S/N]. Tente novamente...')


def genFirstNineNumbers(state):  # Retorna uma sequência de 9 números padronizados de acordo com o estado ou não.
    return ''.join(
        [str(state) if state and pos == 8 else str(randint(0, 9)) for pos, x in enumerate(range(9))])


def getDigit(numbers, start, finish, multiplier):  # Retorna um digito válido para uma sequência de números.
    res = 0

    for n in numbers[start:finish]:
        res += int(n) * multiplier
        multiplier -= 1

    res = (res * 10) % 11

    return str(0 if res > 9 else res)


def assingDigits(numbers):  # Atribui os digitos a sequência de números.
    d1 = getDigit(numbers, 0, 9, 10)
    d2 = getDigit(numbers + d1, 0, 10, 11)

    return numbers + d1 + d2


def applyMaskInCPF(cpf):
    return f'{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}'


def generateCpfs(amount, state, mask=False):
    res = []

    for x in range(amount):
        numbers = genFirstNineNumbers(state)
        cpf = assingDigits(numbers)
        res.append(applyMaskInCPF(cpf) if mask else cpf)

    return res


def main():

    while True:
        amount = inputAmount('Informe a quantidade de CPFs: ')
        state = inputState('Informe o estado. Caso não queira especificar, deixe em branco: ')
        is_masked = True if inputYesOrNo('Atribuir pontuação? ') else False

        cpfs = generateCpfs(amount, state, mask=is_masked)

        print(cpfs)

        choice = inputYesOrNo('Deseja continuar? ')
        if not choice:
            break


if __name__ == '__main__':
    main()
