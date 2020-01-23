import mysql.connector
import csv 
import json

with open('config.json') as json_data_file:
    data = json.load(json_data_file)

for k,v in data.items():
	if k == "host":
		host = v
	elif k == "passwd":
		passwd = v
	elif k == "db":
		db = v
	else:
		user = v

mydb = mysql.connector.connect(host=host, user=user, passwd=passwd, database=db)

mycursor = mydb.cursor()

result = mycursor.execute("select * from table_name")

with open('mycsv.csv', 'w') as f:
	thewriter = csv.writer(f)

	for row in result:
		thewriter.writerow(row)

    print("CSV file loaded successfully...")
		