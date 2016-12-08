import sys
import csv
import MySQLdb

mydb = MySQLdb.connect(host='localhost',
        user='root',
        passwd='',
        db='scm')
cursor = mydb.cursor()

i = 0
csv_data = csv.reader(file("electronic.csv"))
for row in csv_data:
    if i == 0:
        i = 1
        continue
    cursor.execute('INSERT INTO electroniccomponents(n_c10, feed_mode, status, type, Des, description, mpn, value, packaging, packing)' 'VALUES("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")', row)

i = 0
csv_data = csv.reader(file("supplier.csv"))
for row in csv_data:
    if i == 0:
        i = 1
        continue
    cursor.execute('INSERT INTO suppliers(distributor, payment_term, position, contacts, contacts_mobile, email, bank, account_address, address)' 'VALUES("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")', row)

#close the connection to the database.
mydb.commit()
cursor.close()
print "Done"
