import csv

def exportingInCsv(csv_columns, dict_data, fileName):
  f = str(fileName) + ".csv"
  csvfile = open(f, 'w')
  writer = csv.DictWriter(csvfile, fieldnames = csv_columns)
  writer.writeheader()
  for data in dict_data:
    writer.writerow(data)
  csvfile.close()