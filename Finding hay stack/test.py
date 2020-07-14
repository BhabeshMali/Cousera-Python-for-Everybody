#import re
#fhandle = open('1.txt')
#handle = fhandle.read()
##numlist=list()
#sum=0
#for line in handle :
    #line=line.strip()
    #findings=re.findall("[0-9]+",line)
    #for t in findings:
#        numlist.append(int(t))
#print(sum(numlist))
import re
name = input("Enter file:")
if len(name) < 1 : name = "test.txt"
fh = open(name)
newlist = list()
for line in fh :
    line = re.findall('[0-9]+', line)  #finds all numbers '.[0-9]*[0-9]' was before and it missed py4e.com and etx
    for number in line :
        newlist.append(int(number)) # creates newlist with int line values
print(sum(newlist))
