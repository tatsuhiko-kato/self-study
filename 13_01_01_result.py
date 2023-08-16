import csv

with open('13_01_01_sample.csv', mode='r', encoding='utf-8') as read_file:
    reader = csv.reader(read_file)
    next(reader)  # ヘッダー行を飛ばす
    with open('13_01_01_result.tsv', newline='', mode='w', encoding='utf-8') as write_file:
        writer = csv.writer(write_file, delimiter='\t')
        writer.writerow(['都道府県', '人口密度'])
        for row in reader:
            population_density = float(row[2]) / float(row[3])
            writer.writerow([row[1], int(population_density)])

