#Counting emails
import sqlite3
conn=sqlite3.connect('emaildb.sqlite')
cur=conn.cursor() #file handle(opening it and sending the sql commands to the cu0rsor and then getting the responses through the same cursor)
cur.execute('DROP TABLE IF EXISTS Counts') #if the sql file is al]ready present, it will update and delete the previous files
cur.execute('CREATE TABLE Counts(email TEXT, count INTEGER)')
fname=input('Enter file name: ')
if (len(fname)<1) : fname = 'mbox.txt'
fh=open(fname)
for line in fh :
    if not line.startswith('From: ') : continue
    pieces=line.split()
    email=pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,)) #count is from CREATE TABLE, ? is a placeholder
    row = cur.fetchone() #grab one from email and give it 'row'
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,)) #if in the row the file is not previously present it will insert
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,))
    conn.commit() #store the values int he memory

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
