# создание переменной
my_heigh = 164
print(my_heigh)

# перезапись переменной
my_name = "Кристина"
my_name = "Кристина Маслова"
print(my_name)

# пользовательский ввод
pet_name = input("Как зовут вашего питомца?")
print("Ваш питомец - " + pet_name)

# создание функции
def print_python():
    print("Учу Python!")

print_python()

# параметризация функций - печать слова по буквам в одной строке
def print_letter(let):
    print(let, end="")

print_letter("С")
print_letter("т")
print_letter("у")
print_letter("д")
print_letter("е")
print_letter("н")
print_letter("т")