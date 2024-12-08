# https://kompege.ru/variant?kim=25070441

import pandas as pd

data_0 = pd.read_excel("3_18918.xlsx", sheet_name="Движение шаров")
data_1 = pd.read_excel("3_18918.xlsx", sheet_name="Шары")
data_2 = pd.read_excel("3_18918.xlsx", sheet_name="Магазин")
ids = data_2[data_2["Район"] == "Зимний"]["ID магазина"].to_list()
arts = data_1[data_1["Наименование шара"] == " Сияние Зимы"]["Артикул"].to_list()
price = data_1[data_1["Наименование шара"] == " Сияние Зимы"]["Цена за 1 шт."].to_list()[0]

s = 0
for i in data_0.index:
    id = data_0["ID магазина"][i]
    art = data_0["Артикул"][i]
    type = data_0["Тип операции"][i]
    date = data_0["Дата"][i]
    if id in ids and art in arts and type == "Продажа" and date >= pd.Timestamp("2023-12-11"):
        s += data_0["Количество, шт."][i] * price
print(s)
