with open('text_7.txt', 'r', encoding='utf-8') as f_obj:
    my_dict = {}
    n = 0
    midl_prof = 0
    for line in f_obj:
        new_line = line.split()
        profit = float(new_line[2]) - float(new_line[3])
        my_dict[new_line[0]] = profit

        if profit > 0:
            midl_prof += profit
            n += 1

    midl_prof = midl_prof / n
    finish_list = [my_dict, {'average_profit': midl_prof}]
    print(finish_list)

import json
with open('text_77.json', 'w', encoding='utf-8') as write_f:
    json.dump(finish_list, write_f, ensure_ascii=False)
