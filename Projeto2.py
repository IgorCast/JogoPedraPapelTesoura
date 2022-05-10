import random

while True:
    escolhas = ['pedra', 'papel', 'tesoura']
    
    computador = random.choice(escolhas)
    jogador = None

    while jogador not in escolhas:
        jogador = input('pedra, papel ou tesoura?: ').lower()

    if jogador == computador:
        print(f'Computador: {computador}')
        print(f'Jogador: {jogador}')
        print('EMPATE!')

    elif jogador == 'pedra':
        if computador == 'papel':
            print(f'Computador: {computador} ')
            print(f'Jogador: {jogador}')
            print('Voce perdeu!')
        if computador == 'tesoura':
            print(f'Computador: {computador}')
            print(f'Jogador: {jogador}')
            print('Voce venceu!') 

    elif jogador == 'tesoura':
        if computador == 'papel':
            print(f'Computador: {computador}')
            print(f'Jogador: {jogador}')
            print('Voce venceu!')
        if computador == 'pedra':
            print(f'Computador: {computador}')
            print(f'Jogador: {jogador}')
            print('Voce perdeu!')

    elif jogador == 'papel':
        if computador == 'pedra':
            print(f'Computador: {computador}')
            print(f'Jogador: {jogador}')
            print('Voce venceu!')
        if computador == 'tesoura':
            print(f'Computador: {computador}')
            print(f'Jogador: {jogador}')
            print('Voce perdeu!')

    play_again = input('Jogar novamente? [SIM/NAO]: ').lower()

    if play_again != 'sim':
        break

print('Adeus!')



