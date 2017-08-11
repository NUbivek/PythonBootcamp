import csv
with open('2012_to_2014_loans_data.csv', 'rb') as loans_raw_data:
	reader = csv.DictReader(loans_raw_data)
with open('2012_to_2014_institutions_data.csv', 'rb') as institutions_raw_data:
	reader = csv.DictReader(institutions_raw_data)
