dict_comp = {}
sum_profit = 0
i = 0

with open('file5_7.txt', encoding='utf-8') as f:
    for el in f.readlines():
        company = el.split()[0]
        profit = int(el.split()[2]) - int(el.split()[3])
        dict_comp[company] = profit

    for el in dict_comp.values():
        if el > 0:
            sum_profit += el
            i += 1
    av_profit = sum_profit / i

    dict_profit = {'average profit': av_profit}
    list_comp = [dict_comp, dict_profit]
    print(list_comp)

import json

with open('file5_7.json', 'w') as j:
    json.dump(list_comp, j)
