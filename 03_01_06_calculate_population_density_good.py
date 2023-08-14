import csv

input_file_name = input('Enter file_name:') # try節から外だし
try:
    with open(input_file_name, mode='r') as f:
        reader = csv.reader(f)
        for row in reader:
            population_density = float(row[1]) / float(row[2])
            print(f'{row[0]}の人口密度は{population_density}です')
except FileNotFoundError:
    print(f'ファイルがありません')
except ZeroDivisionError:
    print(f'{row[0]}:{row[1]}, {row[2]} => 値0は指定できません')
except ValueError:
    print(f'{row[0]}:{row[1]}, {row[2]} => 数値以外は指定できません')
