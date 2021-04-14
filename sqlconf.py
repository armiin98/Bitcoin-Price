# CONNECT TO DATABASE
def show_database():
    import  mysql.connector
    cnx = mysql.connector.connect(
    user=input("username: "),
    password=input("password: "),
    host="127.0.0.1"
    ) 
    print("connected")
    
    # SHOW TABLE INFORMATION
    cursor = cnx.cursor()    
    cursor.execute("USE crypto")
    cursor.execute("SELECT * FROM bitcoin")
    data = cursor.fetchall() 
    print("")
    for item in data :   
        print("   ",item)
    cnx.close() 

# SAVE TO DATABASE
def save_database():
    # CONNECTING TO DATA BASE
    print("Enter your name and password to connect to database")
    import  mysql.connector
    cnx = mysql.connector.connect(
    user=input("Username: "),
    password=input("Password: "),
    host="127.0.0.1"
    ) 
    print("Connected")

    cursor = cnx.cursor()
    # CHECK IF DATABASE EXIST OR NOT
    cursor.execute("SHOW DATABASES")
    list_of_databases = []
    for x in cursor:
        list_of_databases.append(x)
    if ('crypto',) not in list_of_databases : 
        print("Creating crypto database !...")
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
        print("Creating bitcoin table !...")
        cursor.execute("CREATE TABLE bitcoin (date VARCHAR(255), time VARCHAR(255), price VARCHAR(255))")

    # INSERT VALUES TO TABLE
    cursor.execute("insert into bitcoin values(\"%s\",\"%s\",\"%s\")"%(date,time,price))
    cnx.commit()
    print("Saved in mysql succesfully")
    cnx.close()