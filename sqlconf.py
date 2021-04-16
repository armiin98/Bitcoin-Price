## SHOW DATABASE OF BITCOIN PRICE IN CHART
def show_database():
    # CONNECTING TO DATABASE
    import  mysql.connector
    cnx = mysql.connector.connect(
    user=input("username: "),
    password=input("password: "),
    host="127.0.0.1") 
    print("connected")
    cursor = cnx.cursor()    
    cursor.execute("USE crypto")
    cursor.execute("SELECT * FROM bitcoin")
    data = cursor.fetchall() 
    print("")

    # SET DATA TO USE IN MATPLOTLIB
    x = []
    y = []
    for item in data : 
        x.append(item[0])
        y.append(float(item[2].replace(",","")))
    
    # USING MATPLOTLIB LIBRARY TO SHOW PRICES IN CHART
    import matplotlib.pyplot as plt 
    import numpy as np
    x = np.array(x)
    y = np.array(y)
    font1 = {'family':'serif','color':'blue','size':20}
    font2 = {'family':'serif','color':'darkred','size':15}
    plt.plot(x,y, marker = 'o', ms = 10, mec = 'r')
    plt.title("Bitcoin Price Chart", fontdict = font1)
    plt.xlabel("Date", fontdict = font2)
    plt.ylabel("$Price", fontdict = font2)
    plt.show()
    cnx.close() 

# SAVE TO DATABASE
def save_database(date,time,price):
    # CONNECTING TO DATABASE
    print("Enter username and password to connect to database")
    import  mysql.connector
    cnx = mysql.connector.connect(
    user=input("Username: "),
    password=input("Password: "),
    host="127.0.0.1") 
    print("Connected")
    cursor = cnx.cursor()

    # CHECK IF DATABASE EXIST OR NOT
    cursor.execute("SHOW DATABASES")
    list_of_databases = []
    for x in cursor:
        list_of_databases.append(x)
    if ('crypto',) not in list_of_databases : 
        print("Creating crypto database ..")

        # CREATE DATABASE
        cursor.execute("CREATE DATABASE crypto")
        cursor.execute("USE crypto")   
    else : 
        cursor.execute("USE crypto")

    # CHECK IF TALBE EXIST OR NOT
    cursor.execute("SHOW TABLES")
    list_of_tables = []
    for x in cursor:
        list_of_tables.append(x)

        # CREATE TABLE
    if ('bitcoin',) not in list_of_tables:
        print("Creating bitcoin table ..")
        cursor.execute("CREATE TABLE bitcoin (date VARCHAR(255), time VARCHAR(255), price VARCHAR(255))")

    # INSERT VALUES TO TABLE
    cursor.execute("insert into bitcoin values(\"%s\",\"%s\",\"%s\")"%(date,time,price))
    cnx.commit()
    print("Data Saved in Mysql Succesfully!")
    cnx.close()