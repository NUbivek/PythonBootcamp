def string_template():

	from string import Template

	s = Template('${name} was born in ${country}')

	print(s.substitute (name = 'Bivek', country = 'Nepal'))

string_template()
