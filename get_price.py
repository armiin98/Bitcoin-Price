# A PYTHON SCRIPT TO GET BITCOIN PRICE

# IMPORT REQUEST MODULE
import requests

# IMPORT SQL CONFIGS
from sqlconf import show_database, save_database

# GENERATE DATE AND TIME    
def date_time():
    import datetime
    now = datetime.datetime.now()
    global date , time
    date = str(now.strftime("%Y-%m-%d"))
    time = str(now.strftime("%H:%M:%S"))
        
def programme():

    choose = input("""

        <Menu>

    1) SHOW BITCOIN PRICE
    2) SHOW DATABSE
    3) EXIT
    :? """)

    # SHOW BITCOIN PRICE
    if choose == "1" : 
        print("\nGetting Current Price .. ")
        date_time()

        # GET PRICE OF BITCOIN
        def prices():
            global name,price
            name = "bitcoin"
            r = requests.get(" https://api.coindesk.com/v1/bpi/currentprice.json")
            respond = r.json()
            price = respond["bpi"]["USD"]["rate"]

            # SHOW PRICE AND OTHER INFO TO USER IN A TABLE
            print("")
            print("**",name,"**")
            print("")
            print("+","="*17,"+","="*17,"+","="*17,"+",sep="")
            print("|","Date".center(15),"|","time".center(15),"|","price".center(15),"|")
            print("+","-"*17,"+","-"*17,"+","-"*17,"+",sep="")
            print("|",date.center(15),"|",time.center(15),"|",price.center(15),"|")
            print("")

            # ASK TO SAVE IN DATABASE OR NOT
            answer = input("Do you want to save this data in mysql?(y/n): ")
            if answer.upper() == "Y" : 
                try :  
                    save_database(date,time,price)
                except : 
                    print("An error occurred when saving data in mysql database!")                 
                finally : 
                    programme()
            else:
                programme()
        prices() 

    # SHOW DATABASE
    elif choose == "2" :
        print("Enter username and password to connect to database")
        try :   
            show_database()
        except : 
           print("\nAn error occured when showing data from database!")  
        finally : 
            programme()    

    # EXIT
    elif choose == "3" :
        print("Bye!")
        exit()  

    # WRONG SELECTION
    else : 
        print("\nWrong selection! try again.")
        programme()            

programme()            