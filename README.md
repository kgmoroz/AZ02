# AZ02
 Загрузка данных. Обработка пропущенных значений и дубликатов. Преобразование данных и работа с типами.

Задание: Исследование оценок учеников

Представьте, что у вас есть таблица из 10 учеников с оценками учеников по 5 разным предметам. Вам нужно выполнить несколько шагов, чтобы проанализировать эти данные:

1. Самостоятельно создайте DataFrame с данными

2. Выведите первые несколько строк DataFrame, чтобы убедиться, что данные загружены правильно

3. Вычислите среднюю оценку по каждому предмету

4. Вычислите медианную оценку по каждому предмету

5. Вычислите Q1 и Q3 для оценок по математике:

Q1_math = df['Математика'].quantile(0.25)

Q3_math = df['Математика'].quantile(0.75)

- можно также попробовать рассчитать IQR

6. Вычислите стандартное отклонение