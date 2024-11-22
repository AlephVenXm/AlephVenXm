#   /---------------------------------------------------------/
#  /  Ссылка >> https://inf-ege.sdamgia.ru/problem?id=27802  /
# /---------------------------------------------------------/

class Node:
    def __init__(self, left=None, middle=None, right=None, win=None):
        self.left = left
        self.middle = middle
        self.right = right
        self.win = win

def build_tree(s, d=0):
    if s >= 67:
        return Node(win=True)
    if d > 1:
        return Node(win=False)
    left = build_tree(s+1, d+1)
    middle = build_tree(s+4, d+1)
    right = build_tree(s*5, d+1)
    return Node(left, middle, right)

def tree(node):
    if node.win is not None:
        return node.win
    else:
        return tree(node.left) or tree(node.middle) or tree(node.right)

for s in range(1, 68):
    if tree(build_tree(s)):
        print(s)
        break

# >>> class Node: <!-- Класс узла дерева --->
# >>>     def __init__(self, left=None, middle=None, right=None, win=None):
# >>>         self.left = left <!-- Левое ответвление --->
# >>>         self.middle = middle <!-- Среднее ответвление --->
# >>>         self.right = right <!-- Правое ответвление --->
# >>>         self.win = win <!-- Является концом (листом) дерева или нет --->
#
# >>> def build_tree(s, d=0): <!-- Построение дерева --->
# >>>     if s >= 67: <!-- Окончание (лист) ветки: Истина --->
# >>>         return Node(win=True)
# >>>     if d > 1: <!-- Окончание (лист) ветки: Ложь --->
# >>>         return Node(win=False)
# >>>     left = build_tree(s+1, d+1) <!-- Левая ветвь --->
# >>>     middle = build_tree(s+4, d+1) <!-- Средняя ветвь --->
# >>>     right = build_tree(s*5, d+1) <!-- Правая ветвь --->
# >>>     return Node(left, middle, right) <!-- Узел дерева --->
#
# >>> def tree(node): <!-- Нахождение концов (листьев) дерева --->
# >>>     if node.win is not None: <!-- Если лист: вернуть результат --->
# >>>         return node.win
# >>>     else: <!-- Прохождение по всем ответвлениям дерева --->
# >>>         return tree(node.left) or tree(node.middle) or tree(node.right)
#
# >>> for s in range(1, 68): <!-- Значения s от 1 до 67 включительно --->
#         <!-- Построить и пройтись по дереву с начальным значением s --->
# >>>     if tree(build_tree(s)): <!-- Если истина: вывод значения, выход из цикла --->
# >>>         print(s)
# >>>         break
