#   /---------------------------------------------------------/
#  /  Ссылка >> https://inf-ege.sdamgia.ru/problem?id=27820  /
# /---------------------------------------------------------/

def game(s, c=0):
    if s >= 41: 
        return True
    elif c > 1: 
        return False
    else: 
        return game(s+1, c+1) or game(s+2, c+1) or game(s*2, c+1)

for s in range(1, 42):
    if game(s):
        print(s)
        break

#     <!-- Функция игры --->
# >>> def game(s, c=0): <!-- s: счётчик камней, c: счётчик ходов --->
# >>>     if s >= 41: <!-- Истина, если второй игрок победил --->
#             return True
# >>>     elif c > 1: <!-- Ложь, если второй игрок не победил --->
#             return False
# >>>     else: <!-- Действия игры: +1, +2 или *2 --->
#             return game(s+1, c+1) or game(s+2, c+1) or game(s*2, c+1)
#
# >>> for s in range(1, 42): <!-- Значения s от 1 до 41 включительно --->
# >>>     if game(s): <!-- Если истина: вывод значения, выход из цикла --->
# >>>         print(s)
# >>>         break
