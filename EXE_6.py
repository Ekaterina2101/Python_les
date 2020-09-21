with open('text_6.txt', 'r', encoding='utf-8') as f_obj:
    f_dict = {}
    for f_list in f_obj:
        new_list = f_list.split()

        ob_key = new_list[0][:-1]
        midl_list = [el for el in new_list[1:] if el != '-']

        counter = 0
        for el_1 in midl_list:

            new_el = [n for n in el_1 if 48 <= ord(n) <= 57]
            new_el = int(''.join(new_el))
            counter = counter + new_el

        f_dict[ob_key] = counter

    print(f_dict)
