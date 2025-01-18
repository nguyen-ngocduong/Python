infile = open('logs/Inpu2.txt', 'r')
outfile = open('logs/output2.txt', 'w')
a = []
data = infile.read()
b = data.split(',')
print(b)
tmp = ''
for name in b:
    tmp = name.split()
    name = ' '.join(tmp).title()
    outfile.write(name + '\n')
# for i in range(len(data)):
#     if data[i] != ',':
#         tmp += data[i]
#     else:
#         a.append(tmp)
#         tmp = ''
# a.append(tmp)
# print(a)
# for name in a:
#     tmp = name.split()
#     name = ' '.join(tmp).title()
#     outfile.write(name + '\n')
infile.close()
outfile.close()