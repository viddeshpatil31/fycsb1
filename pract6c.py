f=open('syit1.txt','r')
lines=f.readlines()
lastlines=lines[-4:]
print(lastlines)
f.close()
