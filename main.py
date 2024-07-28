import pandas as pd
import numpy as np

# Шаг 1: Создание DataFrame
data = {
    'Ученик': ['Ученик1', 'Ученик2', 'Ученик3', 'Ученик4', 'Ученик5', 'Ученик6', 'Ученик7', 'Ученик8', 'Ученик9', 'Ученик10'],
    'Математика': [8, 7, 9, 8, 7, 9, 8, 8, 9, 8],
    'Физика': [8, 8, 8, 9, 7, 8, 8, 8, 8, 8],
    'Химия': [7, 8, 8, 8, 7, 9, 8, 8, 8, 9],
    'Биология': [9, 8, 8, 8, 8, 9, 9, 8, 8, 8],
    'История': [8, 8, 9, 8, 8, 8, 9, 9, 8, 8]
}

df = pd.DataFrame(data)

# Шаг 2: Вывод первых нескольких строк DataFrame
print("Первые несколько строк DataFrame:")
print(df.head())

# Шаг 3: Вычисление средней оценки по каждому предмету
mean_scores = df.mean(numeric_only=True)
print("\nСредние оценки по каждому предмету:")
print(mean_scores)

# Шаг 4: Вычисление медианной оценки по каждому предмету
median_scores = df.median(numeric_only=True)
print("\nМедианные оценки по каждому предмету:")
print(median_scores)

# Шаг 5: Вычисление Q1 и Q3 для оценок по математике
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math

print("\nQ1 для оценок по математике:", Q1_math)
print("Q3 для оценок по математике:", Q3_math)
print("IQR для оценок по математике:", IQR_math)

# Шаг 6: Вычисление стандартного отклонения
std_dev = df.std(numeric_only=True)
print("\nСтандартное отклонение по каждому предмету:")
print(std_dev)