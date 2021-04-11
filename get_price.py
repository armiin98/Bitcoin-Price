# A PYTHON SCRIPT TO GET SOME CRYPTOCURRENCIES PRICE

# IMPORT REQUEST MODULE
import requests

# CLASS OF CRYPTOES
class crypto : 
    def __init__(self,name,date,time,price):
        self.name = name
        self.date = date
        self.time = time
        self.price = price

# GENERATE DATE AND TIME    
def date_time():
    import datetime
    now = datetime.datetime.now()
    global dateg , timeg
    dateg = str(now.strftime("%Y-%m-%d"))
    timeg = str(now.strftime("%H:%M:%S"))
date_time()

# GET PRICE
def prices():
    global nameg,priceg
    nameg = "bitcoin"
    r = requests.get(" https://api.coindesk.com/v1/bpi/currentprice.json")
    respond = r.json()
    priceg = respond["bpi"]["USD"]["rate"]
prices()

bitcoin = crypto(nameg,dateg,priceg,timeg)

name = bitcoin.name
date = bitcoin.date
time = bitcoin.time
price = bitcoin.price

# SAVE IN MYSQL
import  mysql.connector
cnx = mysql.connector.connect(user="root",password="",host="127.0.0.1",database="bitcoin") 
cursor = cnx.cursor()

# CHECK IF DATABASE EXIST OR NOT
cursor.execute("SHOW DATABASES")
list_of_databases = []
for x in cursor:
  list_of_databases.append(x)

if ('crypto',) not in list_of_databases : 
    cursor.execute("CREATE DATABASE crypto")
    cursor.execute("USE crypto")   
else : 
    cursor.execute("USE crypto")

cursor.execute("SHOW TABLES")
list_of_tables = []
for x in cursor:
    list_of_tables.append(x)

if ('cryptocurrency',) not in list_of_tables:
    cursor.execute("CREATE TABLE cryptocurrency (name VARCHAR(255), date VARCHAR(255), time VARCHAR(255), price VARCHAR(255))")

cursor.execute("insert into cryptocurrency values(\"%s\",\"%s\",\"%s\",\"%s\")"%(name,date,time,price))
cnx.commit()
cnx.close()
