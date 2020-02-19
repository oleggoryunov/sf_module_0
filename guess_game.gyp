def score_game(game_core_v1):
#    '''Запускаем игру 1000 раз, чтоб узнать как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 1010, size=(10000))
    for number in random_array:
        count_ls.append(game_core_v2(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

    # запускаем
#score_game(game_core_v1)

#game_core_v1(45)

import numpy as np
import pdb
def game_core_v3(number):
#     '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его
#        в зависимости от того, больше оно или меньше нужного.
#        Функция принимает загаданное число и возвращает число попыток'''
    pdb.set_trace()
    count = 0
    minv=0
    maxv=101
    predict = np.random.randint(0,101)
    while number != predict:
        count+=1
        if number > predict:
            minv=predict
            predict = int(round(maxv-(maxv-minv)/2))
        elif number < predict:
             maxv=predict
             predict = int(round(maxv-(maxv-minv)/2))
    return(count) # выход из цикла, если угадали
game_core_v3(44)


# Проверяем
#score_game(game_core_v2)

print('test')