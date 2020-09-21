with open("text.txt", "w", encoding="utf-8") as f_obj:
    st_ = 'Инициализация'
    while st_ != '':
        st_ = input('Введите строку')
        f_obj.write(f'{st_}\n')
