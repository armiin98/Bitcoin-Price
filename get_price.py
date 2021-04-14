# A PYTHON SCRIPT TO GET SOME CRYPTOCURRENCIES PRICE

# IMPORT REQUEST MODULE
import requests

# IMPORT CLEAR SCREEN MUDULE
from clear_screen import clear 

# IMPORT SQL CONFIGS
from sqlconf import show_database, save_database

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


# SAVE IN MYSQL
def save_data() : 
    try :  
        save_database()
           
    except : 
        print("An error occurred when saving data in mysql database!")   
        
def programme():

    choose = input("""

        <Menu>

    1) SHOW BITCOIN PRICE
    2) SHOW DATABSE
    3) EXIT
    :? """)

    # SHOW BITCOIN PRICE
    if choose == "1" : 
        clear()
        print("Please wait to get information (make sure you have internet connection)!.")
        date_time()

        # GET PRICE OF BITCOIN
        def prices():
            global nameg,priceg
            nameg = "bitcoin"
            r = requests.get(" https://api.coindesk.com/v1/bpi/currentprice.json")
            respond = r.json()
            priceg = respond["bpi"]["USD"]["rate"]

            # SET VARIABLES
            bitcoin = crypto(nameg,dateg,timeg,priceg)
            global name, date, time, price
            name = bitcoin.name
            date = bitcoin.date
            time = bitcoin.time
            price = bitcoin.price

            # SHOW PRICE AND OTHER INFO TO USER IN A TABLE
            print("")
            print("**",name,"**")
            print("")
            print("+","="*17,"+","="*17,"+","="*17,"+",sep="")
            print("|","Date".center(15),"|","time".center(15),"|","price".center(15),"|")
            print("+","="*17,"+","="*17,"+","="*17,"+",sep="")
            print("|",bitcoin.date.center(15),"|",bitcoin.time.center(15),"|",bitcoin.price.center(15),"|")
            print("+","-"*17,"+","-"*17,"+","-"*17,"+",sep="")
            print("")

            # SAVE IN DATABASE OR NOT
            answer = input("Do you want to save this data in mysql?(y/n): ")
            if answer.upper() == "Y" : 
                save_data()
                programme()
            else:
                programme()
        prices() 

    # SHOW DATABASE
    elif choose == "2" :
        try : 
            clear()
            print("Enter your name and password to connect to database")
            show_database() 
        except : 
            print("\nAn error occured when showing data from database!")  

        finally : 
            programme()    
    # EXIT
    elif choose == "3" :
        clear()
        exit()  

    # WRONG SELECTION
    else : 
        print("\nWrong selection! try again.")
        programme()            

programme()            