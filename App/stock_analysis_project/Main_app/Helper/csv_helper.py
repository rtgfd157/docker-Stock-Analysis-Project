from Main_app.models import ComapnyStockData
import csv

def insert_companies_to_db_from_csv():
    ComapnyStockData.objects.all().delete()

    print(" load_db from csv file")
    lista = []
    with open('others/2.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                #print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                #print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                x = row[0].replace("^", "-")
                lista.append(ComapnyStockData(ticker=x, company_name=row[1], stock_exchange=row[2]))
                # line_count += 1
                # print(line_count)

    print("before bulk create")
    ComapnyStockData.objects.bulk_create(lista)
