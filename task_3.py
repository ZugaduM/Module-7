team1_num = 6
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
team1_avg_time = team1_time / score_1
team2_avg_time = team2_time / score_2
time_avg = round((team1_avg_time + team2_avg_time) / 2, 3)

def result():
  if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    return 'Победа команды Мастера кода!'
  elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    return 'Победа команды Волшебники Данных!'
  else:
    return 'Ничья!'


challenge_result = result()

print("В команде Мастера кода участников: %s ! " % team1_num)
print("В команде Волшебники Данных участников: %s ! " % team2_num)
print("Итого сегодня в командах участников: %s и %s !" % (team1_num, team2_num))

print("Команда Мастера кода решила задач: {} !".format(score_1))
print("Команда Волшебники данных решила задач: {} !".format(score_2))
print("Мастера кода решили задачи за {} с !".format(team1_time))
print("Волшебники данных решили задачи за {} с !".format(team2_time))

print(f"Команды решили {score_1} и {score_2} задач.")
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')
print(challenge_result)
