def my_func(**kwargs):

    return kwargs


print(my_func(Имя=input('Введите имя'), Фамилия=input('Введите фамилию'), год_рождения=input('Укажите год рождения'),
              город_проживания=input('Введите город проживания'), email=input('Укажите email'), 
              телефон=input('Укажите телефон')))
