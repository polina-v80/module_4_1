# current_year = 2024
# date_of_birth = int(input("В каком году Вы родились? "))
# age = current_year - date_of_birth
# def godlet (god):
#     return {
#         god<0: "ошибка",
#         god%10==0: "лет",
#         god%10==1: "год",
#         god%10>1 and god%10<5: "года",
#         god%10>4: "лет",
#         god%100>10 and god%100<20: "лет"
#     } [True]
#
# print("В этом году Вам", age, godlet(age))







def print_params(a=1, b='строка', c=True):
    print("Параметр a:", a)
    print("Параметр b:", b)
    print("Параметр c:", c)
    print()

# Вызов функции print_params с разным количеством аргументов
print_params()
print_params(5)
print_params(b=25)
print_params(c=[1,2,3])

# Распаковка параметров
values_list = [10, 'новая строка', False]
values_dict = {'a': 7, 'b': 'слово', 'c': True}

print_params(*values_list)
print_params(**values_dict)

# Распаковка + отдельные параметры
values_list_2 = [15, 'еще строка']
print_params(*values_list_2, 42)

