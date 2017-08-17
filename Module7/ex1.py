import pandas as p



import re












class data_python():

	def data_init(self):

		self.data_file = p.read_csv("/Users/bivekadhikari/Desktop/PythonBootcamp/greatKaas/read_write_files/Book.csv",
																		na_values=['NA      ', 'NA    ', 'NA   ', 'NA', 'NA ', 'NA ', 'NaN', 'NAN', ''],
																		error_bad_lines=False, skipinitialspace=True)
		#print(self.data_file.head(10))
		self.data_file

		for name in self.data_file["Name"]:
			if len(" ") > 2 in name:
				first_name = name.split()[1]
				middle_name = name.split()[2]
				last_name = name.split()[-1]
				# print (first_name)
				# print (last_name)

			else:
				first_name = name.split()[1]
				last_name = name.split()[-1]
				# print (first_name)
				# print (last_name)

	def data_clean(self):

	 	self.data_clean['new_var1'] = temp_var.apply(data_python.data_init)
	 	print(self.data_clean)
	 	return self.data_clean


if __name__ == '__main__':
	dlt = data_python()
	finaldf = dlt.data_clean()