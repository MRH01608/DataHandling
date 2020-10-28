import csv, os

F_in = "C:\\Users\\mherbert\\Desktop\\Data\\Test_Data.csv"
fnames = ['Run_date', 'Genotype', 'Enzyme', 'Analyte', 'ONLP', 'Run_ID']

with open (F_in, 'r') as foo:
	csv_file = csv.DictReader(foo, delimiter=',',fieldnames=fnames)
	for row in csv_file:
		print(row)