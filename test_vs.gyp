import numpy as np
# count = 0                            # счетчик попыток
# number = np.random.randint(1,100)    # загадали число
# print ("Загадано число от 1 до 99")

# while True:                        # бесконечный цикл
#     predict = int(input())         # предполагаемое число
#     count += 1                     # плюсуем попытку
#     if number == predict: break    # выход из цикла, если угадали
#     elif number > predict: print (f"Угадываемое число больше {predict} ")
#     elif number < predict: print (f"Угадываемое число меньше {predict} ")
        
# print (f"Вы угадали число {number} за {count} попыток.")
# print()

# import numpy as np
# number = np.random.randint(1,100)    # загадали число
# print ("Загадано число от 1 до 99")

# for count in range(1,100):         # более компактный вариант счетчика
#     predict = np.random.randint(1,100) # предполагаемое число
#     if number == predict: break    # выход из цикла, если угадали
#     elif number > predict: print (f"Угадываемое число больше {predict} ")
#     elif number < predict: print (f"Угадываемое число меньше {predict} ")
        
# print (f"Вы угадали число {number} за {count} попыток.")


def game_core_v1(number):
    '''Просто угадываем на random ни как не используя информацию о больше или меньше.
       Функция Принимает загаданное число и возвращает число попыток'''
    count = 0
    while True:
        count+=1
        predict = np.random.randint(1, 101) # предполагаемое число
        if number == predict: 
            break
    return(count) # выход из цикла, если угадали
        
        
def score_game(game_core_v1):
    '''Запускаем игру 1000 раз, чтоб узнать как быстро игра угадывает число'''
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


def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его
       в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    predict = np.random.randint(1,100)
    while number != predict:
        count+=1
        if number > predict: 
            predict += 1
        elif number < predict: 
            predict -= 1
    return(count) # выход из цикла, если угадали

# Проверяем
score_game(game_core_v2)