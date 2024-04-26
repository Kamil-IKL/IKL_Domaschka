team1 = str('"Мастера кода"')
team2 = str('"Волшебники"')

team1_num = 6
team2_num = 6
print('\nВ команде %s участников: %d !' % (team1, team1_num))
print('В команде %s участников: %d !' % (team2, team2_num))
print('Итого сегодня в командах участников: %s = %d и %s = %d !\n' % (team1, team1_num, team2, team2_num,))

score_1 = 40  # количество задач команды team1
score_2 = 42  # количество задач команды team2
tasks_total = score_1 + score_2  # количество задач
print('Команда {} данных задач решила: {} !'.format(team1, score_1))  # порядок вывода распределяются по умолчанию
# print('Команда {1} данных решила задач: {0}!'.format(score_2, team2)) # порядок вывода аргументов определяю сам
print('Команда %s данных задач решила: %d !' % (team2, score_2))
print(f'Команды решили {score_1} и {score_2} задач cоответственно.\n')

team1_time = 1552.512  # время решения задач команды team1
team2_time = 2153.31451  # время решения задач команды team2
print('{0} решили данные задачи за {1:0.2f} c !'.format(team1, team1_time))  # перевел на ручную спец.полей (0 и 1)
# указал для поля 1 два знака после запятой
print(f'{team2} решили данные задачи за {team2_time:0.2f} c !')

if score_1 == score_2:
    chalenge_result = print(f'Результат биьвы: Команды {team1} и {team2} сыграли в ничью !')
    if score_1 > score_2:
        chalenge_result = print(f'Результат битвы: Победа команды {team1} !')
else:
    chalenge_result = print(f'Результат битвы: Победа команды {team2} !')

print(f'\n{" Статистика ":*^50}')
time_avg = round((team1_time + team2_time) / tasks_total, 2)  # вычисляю и сразу округляю до сотых
print(f'Сегодня было решено {tasks_total} задачи, в среднем по {time_avg:0.1f} секунды на задачу !')
