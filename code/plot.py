# %%
import sys
import pandas as pd
import matplotlib.pyplot as plt

csv_file = sys.argv[1]

df = pd.read_csv(csv_file, dtype={'ИНН': str, 'СНИЛС': str, 'ОГРН': str})

date_columns = ['Дата принятия решения о включении', 'Дата принятия решения об исключении', 'Дата рождения']
df[date_columns] = df[date_columns].apply(pd.to_datetime, format='%d.%m.%Y', errors='coerce')


# Группируем данные по году и месяцу, считаем количество записей
monthly_counts = df['Дата принятия решения о включении'].dt.to_period('M').value_counts().sort_index()
monthly_counts_exclusion = df['Дата принятия решения об исключении'].dt.to_period('M').value_counts().sort_index()


# Создаем полный диапазон годов-месяцев
full_range = pd.period_range(start=monthly_counts.index.min(), end=monthly_counts.index.max(), freq='M')

# Восстанавливаем отсутствующие месяцы с нулевым значением
monthly_counts = monthly_counts.reindex(full_range, fill_value=0)
monthly_counts_exclusion = monthly_counts_exclusion.reindex(full_range, fill_value=0)

# Строим барчарт
plt.figure(figsize=(12, 6))
bar_chart = monthly_counts.plot(kind='bar', color='skyblue', label='Включение', fontsize=6)
# bar_chart.set_xlabel('Год-Месяц', fontsize=8)
bar_chart.set_ylabel('Количество записей')
bar_chart.set_title('Распределение по году-месяцу включения и исключения из реестра')

bar_chart_exclusion = monthly_counts_exclusion.plot(kind='bar', color='salmon', label='Исключение', alpha=0.7)

# Устанавливаем метки только для месяца
# bar_chart.set_xticklabels(monthly_counts.index.strftime('%m'), rotation=90, ha='right')
bar_chart.set_xticklabels([])

# Добавляем вертикальные линии для разделения по годам
years = monthly_counts.index.year.unique()
for year in monthly_counts.index.year.unique()[1:]:
    year_start = pd.to_datetime(str(year))
    loc = year_start.strftime('%Y-%m')
    
    plt.axvline(x=bar_chart.get_xticks()[full_range.get_loc(loc)], color='red', linestyle='--', linewidth=0.8, alpha=0.5)
    plt.text(bar_chart.get_xticks()[full_range.get_loc(loc)], -1, str(year), color='red', ha='center', va='center', rotation=0, fontsize=10)


plt.legend()

plt.savefig('data/result/imgs/Распределение по году-месяцу включения и исключения из реестра.png')