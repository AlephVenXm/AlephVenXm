#       /---------------------------------------------------------/
#      /  Ссылка >> https://inf-ege.sdamgia.ru/problem?id=72594  /
#     /---------------------------------------------------------/
#    /  Вводи эту команду в консоль если нет нужных библиотек  /
#   /---------------------------------------------------------/
#  />>       py -m pip install openpyxl pandas numpy       <</
# /---------------------------------------------------------/

import pandas as pd, numpy as np

table = pd.read_excel("09.xlsx").to_numpy()

counts = map(lambda line: np.unique(line, return_counts=True), table)

lineCount = 0
for i, j in counts:
    if max(j) >= 3 and min(j) == 1:
        meanRepeat = np.mean(i[j != 1])
        meanUnique = np.mean(i[j == 1]) 
        if meanRepeat < meanUnique:
            lineCount += 1

print(f"Ответ: {lineCount}")

#     <!-- Чтение таблицы --->
# >>> table = pd.read_excel("09.xlsx").to_numpy()
#     <!-- Числа, Числа повторения --->
# >>> counts = map(lambda line: np.unique(line, return_counts=True), table) 
#
# >>> lineCount = 0 <!-- Счётчик --->
# >>> for i, j in counts: <!-- Для Чисел, Чисел повторений --->
#         <!-- Число повторяется не менее трёх раз и есть хотя бы одно уникальное --->
# >>>     if max(j) >= 3 and min(j) == 1: 
# >>>         meanRepeat = np.mean(i[j != 1]) <!-- Среднее значение повторяющихся чисел --->
# >>>         meanUnique = np.mean(i[j == 1]) <!-- Среднее значение уникальных чисел --->
#             <!-- Среднее значение повторяющихся чисел меньше среднего значения уникальных --->
# >>>         if meanRepeat < meanUnique:
# >>>             lineCount += 1
#
# >>> print(f"Ответ: {lineCount}") <!-- Вывод --->