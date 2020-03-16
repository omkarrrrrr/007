import re

# find non white space

print re.findall(r'\s', 'fyit syit tyit 123456')

# find all digits

print re.findall(r'\d', 'fyit syit tyit 123456')

# find the non digits

print re.findall(r'\D', 'fyit syit tyit 123456')

# splits

print re.findall(r'\S', 'fyit syit tyit 123456')

# finding white space

print re.findall(r'\s', 'fyit syit tyit 123456')

# finding start of string

print re.findall(r'\A', 'fyit syit tyit 123456')

# matching end of string

print re.findall(r'\a', 'fyit syit tyit 123456')

# match a and b

print re.findall(r't|T', 'fyit syit tyit 123456')
