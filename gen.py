import random
code =1
while code<10000 :
	code = code+1
	a = random.randint(10000000,99999999)
	b ='0773'	
	c = str(b)+str(a)+str(':')+str(b)+str(a)
	with open("list.txt", "a") as m:
		m.write(c)
		m.write('\n')