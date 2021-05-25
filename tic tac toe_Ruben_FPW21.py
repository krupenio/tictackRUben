########### Функция вступление ###############


def intro():
    print('Начинаем игру крестики нолики')
    print("-----------------------------")
    print('Перед Вами знакомое с детства игровое поле')
    global player_one
    player_one = str(input('Введите имя первого игрока: '))
    print(f'Первый игрок {player_one}, Вам нужно ввести номер клетки куда вы хотите поставить крестик (Х) ')
    global player_two
    player_two = str(input('Введите имя второго игрока: '))
    print(f'{player_two}, а Вам нужно ввести номер клетки куда вы хотите поставить нолик (0)\n  ---Поехали ---')



########### Функция выводит игровое поле #############
board = list(range(1,10))    # задаем поле
winner_line = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]   # все выигрышные варианты

def show_board():            # функция вызывающая игровое поле
    for i in range(3):
        print("-------------")
        print('|',board[0+i*3],'|', board[1 + i*3],'|', board[2 + i*3],'|')

########### Функция постановки крестиков и ноликов ################

def players_input(crossorno):   #функция позволяющая выбирать поле куда вносить крестик  и нолик. нулевой и четные зода за крестиком, нечетные за ноликом
    while True:
        value = input("Куда поставить " + crossorno + ' ? ')
        if not value in '123456789':
            print("Вы ввели что-то не то. В какую клетку вы зотиет поставить крестик?")
            continue
        value = int(value)
        if str(board[value - 1]) in 'XO':
            print('Сюда уже нельзя ставить')
            continue
        board[value-1] = crossorno
        break

def check_win():   # проверяем, есть ли выигрышная комбинация
    for each in winner_line:
        if (board[each[0]-1]) == (board[each[1]-1]) == (board[each[2]-1]):
            return board[each[1]-1]
    else:
        return False

def game_itself(): # непосредственно сам процесс игры на основе предыдущих вункций
    intro()
    counter = 0
    while True:
        show_board()
        if counter % 2 == 0:
            players_input('X')
        else:
            players_input('O')
        if counter > 3:
            winner = check_win()
            if winner:
                show_board()
                counter_X = 0
                counter_O = 0
                for each in board:
                    if each == 'X':
                        counter_X += 1
                    elif each == 'O':
                        counter_O += 1
                if counter_X > counter_O:
                    print(f'ИГРА ЗАКОНЧЕНА!!!! Победил(а) {player_one}')
                else:
                    print(f'ИГРА ЗАКОНЧЕНА!!!! Победил(а) {player_two}')
                break
        counter += 1
        if counter > 8: # для ничейного исхода
            show_board()
            print('НИЧЬЯ!!! Попробуйте еще раз')
            break

game_itself()



