#       /---------------------------------------------------------/
#      /  Ссылка >> https://inf-ege.sdamgia.ru/problem?id=47006  /
#     /---------------------------------------------------------/
#    /  Вводи эту команду в консоль если нет нужных библиотек  /
#   /---------------------------------------------------------/
#  />>       py -m pip install openpyxl pandas numpy       <</
# /---------------------------------------------------------/

import pandas as pd, numpy as np

t = np.sort(pd.read_excel("107_9.xlsx").to_numpy())

c = sum([1 for l in t if l[0]+l[1] > l[-1] and l[0]+l[2] > l[-1] and l[1]+l[2] > l[-1]])

print(f"Ответ: {c}")

# >>> import pandas as pd, numpy as np
#     <!-- Ввод и сортировка таблицы --->
# >>> t = np.sort(pd.read_excel("107_9.xlsx").to_numpy())
#     <!-- Счётчик --->
# >>> c = sum([1 for l in t if l[0]+l[1] > l[-1] and l[0]+l[2] > l[-1] and l[1]+l[2] > l[-1]])
#
# >>> print(f"Ответ: {c}") <!-- Вывод --->