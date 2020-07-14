import re
fhandle = open('1.txt')
handle = fhandle.read()
findings = re.findall("[0-9]+", handle)
dice = [int(i) for i in findings]
sum = 0
for k in dice:
	sum += k
print(sum)
