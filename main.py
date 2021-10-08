
files_list = ['1.txt', '2.txt', '3.txt']
temp_dict = {}
sorted_dict = {}
for file in files_list:
  with open(file, 'r', encoding="utf-8") as file:
    temp_dict[file.name] = len(file.readlines())
sorted_values = sorted(temp_dict.values())
for i in sorted_values:
    for key in temp_dict.keys():
        if temp_dict[key] == i:
            sorted_dict[key] = temp_dict[key]
            break     
with open('out_file.txt', 'a', encoding="utf-8") as out_file:
  for sorted_file, len_file in  sorted_dict.items():
    with open(sorted_file) as file:
       out_file.write(sorted_file + '\n' + str(len_file) + '\n' +file.read()+ '\n')