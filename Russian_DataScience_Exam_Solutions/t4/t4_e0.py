#   /---------------------------------------------------------/
#  /    Ссылка >> https://kompege.ru/variant?kim=25070441    /
# /---------------------------------------------------------/

from itertools import product

a = ["11110", "000", "01", "100", "101", "1110", "001"]
b = []

for k in range(len(max(a))):
    for i in product("01", repeat=k):
        if any(j.startswith("".join(i)) for j in a) or any("".join(i).startswith(j) for j in a):
            continue
        else:
            b.append("".join(i))

print(f"Ответ: {min(b)}")

# >>> from itertools import product
#     <!-- Существующие кодировки --->
# >>> a = ["11110", "000", "01", "100", "101", "1110", "001"]
# >>> b = []
#     <!-- Берём максимальную длину кодировки --->
# >>> for k in range(len(max(a))):
# >>>     for i in product("01", repeat=k):
#             <!-- Кодировка не начинается с других и наоборот --->
# >>>         if any(j.startswith("".join(i)) for j in a) or any("".join(i).startswith(j) for j in a):
# >>>             continue
# >>>         else:
# >>>             b.append("".join(i))
#    
# >>> print(f"Ответ: {min(b)}") <!-- Вывод кратчайшей кодировки --->
