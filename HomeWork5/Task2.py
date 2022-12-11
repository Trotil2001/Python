
""" 
Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход 
друг после друга. Первый ход определяется жеребьёвкой. За один ход можно 
забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему 
последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все 
конфеты у своего конкурента?

a) Добавьте игру против бота

b) Подумайте как наделить бота ""интеллектом""


"""
from random import randint


def move_player(name_player, candies, max_candies):
    valid = False
    while not valid:
        move = int(input(f'Ход игрока {name_player}:'))
        if move > 0 and move <= max_candies and move <= candies:
            print(f'{name_player} забрал {move} конфет')
            candies -= move
            print(f'Осталось {candies} конфет')
            valid = True
        else:
            print(
                f'Количество конфет должно быть от 1 до {max_candies} и не больше')
    return candies


def stupid_bot(name_player, candies, max_candies):
    move = randint(
        1, max_candies) if candies >= max_candies else randint(1, candies)
    print(f'Ход игрока {name_player}: {move}')
    print(f'{name_player} забрал {move} конфет')
    candies -= move
    print(f'Осталось {candies} конфет')
    return candies


def smart_bot(name_player, candies, max_candies):
    move = candies % (max_candies + 1)
    if move == 0:
        move = randint(1, max_candies) if candies >= max_candies else candies
    print(f'Ход игрока {name_player}: {move}')
    print(f'Бот забрал {move} конфет')
    candies -= move
    print(f'Осталось {candies} конфет')
    return candies


def check_win(candies, moves, first_name, second_name):
    if candies == 0:
        return first_name if moves else second_name
    else:
        return False


def play(player1, player2, n_player1, n_player2, candies, max_candies):
    ferst_moves = randint(0, 1)
    count_for_check_win = candies // max_candies
    win = False
    print(f'Количество конфет {candies}')
    while not win:
        if ferst_moves == 0:
            candies = player1(n_player1, candies, max_candies)
        else:
            candies = player2(n_player2, candies, max_candies)
        ferst_moves = not ferst_moves
        if count_for_check_win <= 0:
            temp = check_win(candies, ferst_moves, n_player1, n_player2)
            if temp:
                print(f'{temp} выиграл')
                win = True
        count_for_check_win -= 1


n_player1 = 'Player1'
n_player2 = 'Player2'
candies = 2021
max_candies = 28


type_game = input(
    'Введите 0 для игры с другим игроком или другую цифру для игры с ботом ')
if (type_game == '0'):
    play(move_player, move_player, n_player1, n_player2, candies, max_candies)
else:
    intel = input(
        'Введите 0, для игры с глупым ботом или другую цифру для игры с умным ботом ')
    if intel == '0':
        play(move_player, stupid_bot, n_player1, 'Bot', candies, max_candies)
    else:
        play(move_player, smart_bot, n_player1, 'Bot', candies, max_candies)
