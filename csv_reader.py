import csv
import sys

#f = open(sys.argv[1], 'rt')
"""try:
    reader = csv.reader(f)
    for row in reader:
        print row
finally:
    f.close()
"""

"""reader = csv.DictReader(open(sys.argv[1], 'rb'))

dict_list = []
for line in reader:
    dict_list.append(line)

print(dict_list)
"""
f = open(sys.argv[1],'r')
file_reader = csv.reader(f)
new_dict = {}
first = True
genre_list = []
print(file_reader)
for i in file_reader:
    if first:
        first = False
    else:
        if i[0] not in genre_list:
            genre_list.append(i[0])
print(genre_list)

for i in genre_list:
    new_dict[i] = []

first_line = True
f = open(sys.argv[1],'r')
file_reader = csv.reader(f)
for i in file_reader:
    if first_line:
        first_line = False
    else:
        new_dict[i[0]].append(tuple((i[1],i[2])))

print new_dict
