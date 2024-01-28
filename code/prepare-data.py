import sys
import pandas as pd

csv_dir_path = sys.argv[1]

dfs = []
for page_number in range(1, 100):
    file_name = f'{csv_dir_path}/{page_number}.csv'
    
    try:
        current_df = pd.read_csv(file_name, dtype={'ИНН': str, 'СНИЛС': str, 'ОГРН': str})
        
        # current_df['Номер страницы в pdf'] = page_number
        dfs.append(current_df)
    except FileNotFoundError:
        print(f"Файл {file_name} не найден.")

df = pd.concat(dfs, ignore_index=True)
df.columns = df.columns.str.replace('\n', '')
df = df.applymap(lambda x: x.replace('\n', '') if isinstance(x, str) else x)


df.to_csv('data/result/the-registry.csv', index=False)
