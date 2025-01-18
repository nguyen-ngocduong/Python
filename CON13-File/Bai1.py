f1 = open('logs/Input1.txt', 'r')
f2 = open('logs/output1.txt', 'w')
for name in f1:
    name = name.title()
    f2.write(name)
f1.close()
f2.close()