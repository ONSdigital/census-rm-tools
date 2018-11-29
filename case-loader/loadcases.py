from datetime import datetime
from datetime import timedelta

import psycopg2
import psycopg2.extras
psycopg2.extras.register_uuid()

# connect to postgres database
conn = psycopg2.connect("host=localhost port=6432 dbname=postgres user=postgres")
cur = conn.cursor()

# clear down the postgres tables ready for import
print ("\nclearing postgres tables...")

cur.execute("delete from action.actionrule")
conn.commit()
print ("actionrule data deleted (" + str(datetime.now()) + ")")

cur.execute("delete from action.actiontype")
conn.commit()
print ("actiontype data deleted (" + str(datetime.now()) + ")")

cur.execute("delete from action.actionplan")
conn.commit()
print ("actionplan data deleted (" + str(datetime.now()) + ")")


# clear the tables to be populated
cur.execute("truncate casesvc.casegroup cascade")
conn.commit()
print ("\ncasegroup truncated (" + str(datetime.now()) + ")")

cur.execute("truncate casesvc.case cascade")
conn.commit()
print ("case truncated (" + str(datetime.now()) + ")")

cur.execute("truncate casesvc.caseevent cascade")
conn.commit()
print ("caseevent truncated (" + str(datetime.now()) + ")")


# copy the data into the postgres tables
print ("\ncopying files into postgres tables...")

with open('casegroup.csv', 'r') as f:
    cur.copy_from(f, 'casesvc.casegroup', sep=',')
conn.commit()
print ("\ncasegroup populated (" + str(datetime.now())+ ")")

with open('case.csv', 'r') as f:
    cur.copy_from(f, 'casesvc.case', sep=',')
conn.commit()
print ("case populated (" + str(datetime.now()))

with open('caseevent.csv', 'r') as f:
    cur.copy_from(f, 'casesvc.caseevent', sep=',')
conn.commit()
print ("caseevent populated (" + str(datetime.now())+ ")")

with open('actionplan.csv', 'r') as f:
   cur.copy_from(f, 'action.actionplan', sep=',')
conn.commit()
print ("actionplan populated (" + str(datetime.now())+ ")")

with open('actiontype.csv', 'r') as f:
    cur.copy_from(f, 'action.actiontype', sep=',')
conn.commit()
print ("actiontype populated " + str(datetime.now())+ ")")

with open('actionrule.csv', 'r') as f:
    cur.copy_from(f, 'action.actionrule', sep=',')
conn.commit()
print ("actionrule populated (" + str(datetime.now())+ ")")

conn.close()

print ("postgres tables populated (" + str(datetime.now())+ ")")
