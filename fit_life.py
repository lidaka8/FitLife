print('Здравствуйте!  Вас приветствует FitLife-бот. Давайте познакомимся!')
user_name = input('Ваше зовут ')
user_age = int(input('Сколько Вам лет? '))
print('Посчитаем Ваш ИМТ (Индекс Массы Тела), и ежедневную  норму воды')
user_weight = float(input('Какой Ваш вес? '))
while True:
    try:
        user_height = float(input('Ваш рост в м.(используйте точку, 1.75)? '))
        break
    except ValueError:
        print('Ошибка: используйте точку, для ввода роста')

# расчёт индекса массы тела
bmi = user_weight / (user_height ** 2)
result_bmi = round(bmi, 1)
WATER_PER_KG = 30
water_ml = user_weight * WATER_PER_KG
ML_IN_L = 1000
water_l = water_ml / ML_IN_L
result_water_l = round(water_l, 1)

print(
    f'Отчет для пользователя: {user_name} {user_age}г. \n'
    f'Ваш Индекс Массы Тела: {result_bmi} \n'
    f'Рекомендуемая норма воды: {result_water_l} л. в день \n'
    'Расчет окончен. Будьте здоровы!'
)
