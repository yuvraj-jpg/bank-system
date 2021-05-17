import mysql.connector
from datetime import date
dt1=date.today()
con=mysql.connector.connect(host='localhost',user='root',password='',database='bank')
cur=con.cursor()
print("PRESS 1 for CREATE ACCOUNT  :      ")   # jo jo bank mai kr skte wo  sb
print("PRESS 2 for WIDTHRAWL :      ")
print("PRESS 3 for DEPOSIT :      ")
print("PRESS 4 for BALANCE ENQUIRY :      ")
print("PRESS 5 for FUND TRANSFER :      ")
print("PRESS 6 for ACCOUNT STATUS :      ")
n=int(input('ENTER your choice :      '))    # for enter you choice what to do 
if n==1:     # if you choose create account you will enter deatils  
    name=input('Enter your NAME :      ')
    address=input('Enter your ADDRESS :      ')
    phone=input('Enter your PHONE NO. .....')
    email=input('Enter your EMAIL ADDRESS :      ')
    father=input('Enter your FATHER NAME :      ')
    country=input('Enter your COUNTRY :      ')
    state=input('Enter your STATE :      ')
    city=input('Enter your CITY :      ')
    amount=input('Enter your AMOUNT ADDED :      ')
    pin=input('Enter your PIN :      ')
    account="AXIS"
    s="Select * from  system"                                     # query likhi python me jo hmne ek variable k andr store ki
    cur.execute(s)                                           # yeh query chalane k lie 
    x=0
    for dt in cur:                                      # for checking row loop
       x+=1
    if x>0:
        x+=1
        x=x+10
        account=account+str(x)
    else:
        account="AXIS11"
    s="insert into system values('""','"+account+"','"+name+"','"+address+"','"+phone+"','"+email+"','"+father+"','"+country+"','"+state+"','"+city+"','"+str(amount)+"','"+pin+"')"  # yah pe '" islie lagaya kuki jo hmara data hai voh variable k andr store hai or sb string type hai toh ise database me dalne k lie aisa format likhna pdhta hai
    cur.execute(s)
    con.commit()             # query save krne k lie db me 
    print('CONGRATS !!!!! \nACCOUNT SUCCESSFULLY CREATED !!!!!!')
elif n==2:
    ac1=input("Enter account no. :      ")
    p1=input("Enter pin no :      ")
    s="Select * from system where account='"+ac1+"' and pin='"+p1+"'"
    cur.execute(s)
    x=0
    camt=0
    for dt in cur:
        x=x+1
        camt=int(dt[10])
        
    if x>0:
        wamt=int(input("Enter Amount to WIDTHRAW :      "))
        

        if wamt<=camt:
            camt=camt-wamt
            s="update system set amount="+str(camt)+" where account='"+ac1+"'"
            cur.execute(s)
            con.commit()
            print("After Withdraw ",wamt," Your current Balnce is= ",camt)
            t="insert into tran(account,date,amount,des)values('"+ac1+"','"+str(dt1)+"',"+str(wamt)+",'WIDTHRAW')"
            cur.execute(t)
            con.commit()
          
        else:
            print("Insufficient balance")

    else:
        print("Invlaid Account or pin")
elif n==3:
    ac1=input("Enter account no. :      ")
    p1=input("Enter pin no :      ")
    s="Select * from system where account='"+ac1+"' and pin='"+p1+"'"
    cur.execute(s)
    x=0
    camt=0
    for dt in cur:
        x=x+1
        camt=int(dt[10])
    if x>0:
        wamt=int(input("Enter Amount to DEPOSIT :      "))
        camt=camt+wamt
        s="update system set amount="+str(camt)+" where account='"+ac1+"'"
        cur.execute(s)
        con.commit()
        print("After Deposit ",wamt," Your current Balnce is= ",camt)
        s="insert into tran(account,date,amount,des)values('"+ac1+"','"+str(dt1)+"',"+str(wamt)+",'DEPOSIT')"
        cur.execute(s)
        con.commit()
 
        
    else:
        print("Invlaid Account or pin")    
elif n==4:
    ac1=input("Enter account no. :      ")
    p1=input("Enter pin no :      ")
    s="Select * from system where account='"+ac1+"' and pin='"+p1+"'"
    cur.execute(s)
    x=0
    camt=0
    for dt in cur:
        x=x+1
        camt=int(dt[10])
    if x>0:
        print(" Your Current Balnce is= ",camt)
        
    else:
        print("Invlaid Account or pin")  
elif n==5:
    ac1=input("Enter account no. :      ")
    p1=input("Enter pin no :      ")
    s="Select * from system where account='"+ac1+"' and pin='"+p1+"'"
    cur.execute(s)
    x=0
    camt=0
    for dt in cur:
        x=x+1
        camt=int(dt[10])
    if x>0:
        wamt=int(input("Enter Amount to TRANSFER :      "))
        if wamt<=camt:
            tac=input("Enter Account Number to TRANSFER :      ")
            s="select * from system where account='"+tac+"'"
            p=0
            tamt=0
            cur.execute(s)
            for dt in cur:
                p=p+1
                tamt=int(dt[10])
            if p>0:
                camt=camt-wamt
                tamt=tamt+wamt
                s="update system set amount="+str(camt)+" where account='"+ac1+"'"
                cur.execute(s)
                con.commit()
                s="update system set amount="+str(tamt)+" where account='"+tac+"'"
                cur.execute(s)
                con.commit()
                print("SUCCESSFULLY TRANSFER !!!!!!!!!!!!")
                print("After Transfer ",wamt," Your current Balnce is= ",camt)
                s="insert into tran(account,date,amount,des)values('"+ac1+"','"+str(dt1)+"',"+str(wamt)+",'TRANSFER')"
                cur.execute(s)
                con.commit()
                s="insert into tran(account,date,amount,des)values('"+tac+"','"+str(dt1)+"',"+str(wamt)+",'RECIVED')"
                cur.execute(s)
                con.commit()

 
            else:
                print("Benifciry Account is not valid")
        else:   
            print("Insufficient balance")

    else:
        print("Invlaid Account or pin")
elif n==6:
    ac= input("Enter the account no. :      ")
    p=input("Enter Pin NUmber :     ")
    s="select * from system where account='"+ac+"'and pin='"+p+"'"
    cur.execute(s)
    x=0
    for dt in cur:
        x+=1
    if x>0:
        s="Select * from tran where account='"+ac+"'"
        cur.execute(s)
        print("S.no     Account         Date                    Amout   Des")
        for dt in cur:
            print(dt[0],"\t",dt[1],"\t",dt[2],"\t",dt[3],"\t",dt[4])
    else:
        print("Invalid account no.")
else:
    print('SORRY!!!! \nYOU ENTERED WRONG CHOICE .......')