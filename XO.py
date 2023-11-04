# Колличество клеток
board_size = 3
# Игровое поле
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Выводим игровое поле
def draw_board():
    print('_' * 4 * board_size)
    for i in range(board_size):
        print((' ' * 3 + '|') * 3)
        print('', board[i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print(('_' * 3 + '|') * 3)

def check_win():

    win = False
    win_combination = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # Горизонтальные линии
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # Вертикальные линии
        (0, 4, 8), (2, 4, 6), # Диагональные линии
    )
    for pos in win_combination:
        if (board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]]):
            win = board[pos[0]]

    return win

# Выполняем ход
def game_step(index, char):
    if (index > 10 or index < 1 or board [index - 1] in ('X', 'O')):
        return False

    board[index - 1] = char
    return True

# Проверяем победу одного из игроков

def start_game():
# Текущий игрок
    current_player = 'X'
# Номер шага
    step = 1
    draw_board()

    while (step < 10):
        index = input('Ходит игрок ' + current_player + '. Введите номер поля (0 - выход):')

        if (index == 'O'):
            break

# Если получилост сделать шаг
        if (game_step(int(index), current_player)):
            print('Удачный ход')

            if (current_player == 'X'):
                current_player = 'O'
            else:
                current_player = 'X'

            draw_board()
            # Увеличим номер хода
            step += 1
        else:
            print('Неверный номер! Повторите!')

    if (step == 10):
        print('Игра окончена. Ничья!')
    else:
        print('Выиграл' + check_win())





print('Добро пожаловать в крестики-нолики!')
start_game()


