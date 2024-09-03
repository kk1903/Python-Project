from easygui import passwordbox
import datetime
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="kariprav1903!",database="Lyods_Bakery")
mycursor=mydb.cursor()
ol=[] #ORDER LIST
oln=[] #ORDER LIST OF THE USER
b=[] #CHECKING FOR BONUS(DISCOUNT)
discount=[] #DISCOUNT


def create_sales():
    try:
        query='''create table sales
              (ITEM_NO char(4),
              ITEM_NAME varchar(25),
              CATEGORY char(15),
              QUANTITY int(4),
              COST int(5),
              TOTAL_COST int(5),
              DATE_OF_PURCHASE date,
              SUM_OF_TOTAL_ int(6),
              CONSTRAINT fk_inventory FOREIGN KEY(ITEM_NO)
              REFERENCES inventory(ITEM_NO)
              ON DELETE CASCADE
              ON UPDATE CASCADE);''' #sum of total discount
        mycursor.execute(query)
        mydb.commit()
    except:
        print("AN ERROR HAS OCCURED")


def create_inventory():
    try:
        query='''create table inventory
              (ITEM_NO char(10) not null unique primary key,
              ITEM_NAME char(25),
              CATEGORY char(25),
              ORIGINAL_QUANTITY int(4),
              QUANTITY int(5),
              COST__PER_ITEM int(5),
              DATE_OF_MANUFACTURE date,
              EXPIRY_DATE date);'''
        mycursor.execute(query)
        mydb.commit()
    except:
        print("AN ERROR HAS OCCURED")


def create_login():
    try:
        query='''create table login
              (USERNAME char(15),
              passwd char(6),
              VISITS int(4));'''
        mycursor.execute(query)
        mydb.commit()
    except:
        print("AN ERROR HAS OCCURED")


#INSERTING VALUES INTO INVENTORY
def i_ins():
    rn=datetime.datetime.now()
    print("Adding values to INVENTORY table")
    while True:
        try:
            item_no=input("ENTER ITEM NUMBER:\t\t\t")
            query='''select * from inventory where ITEM_NO='%s';'''%(item_no)
            mycursor.execute(query)
            results=mycursor.fetchall()
            if mycursor.rowcount==0:
                item_name=input("ENTER NAME OF FOOD ITEM:\t\t")
                category=input("ENTER CATEGORY:\t\t")
                oqty=int(input("ENTER THE QUANTITY MADE:"))
                qty=oqty
                cost=int(input("ENTER COST OF EACH ITEM:\t\t"))
                date=rn
                exp=input("ENTER EXPIRY DATE IN PROPER FORMAT:\t\t:")
                val=(item_no,item_name,category,oqty,qty,cost,date,exp)
                query="""insert into INVENTORY values(%s,%s,%s,%s,%s,%s,%s,%s)""";
                mycursor.execute(query,val)
                mydb.commit()
                print("--------------------------------------------")
                print("RECORD ADDED SUCCESSFULLY")
                print("--------------------------------------------")
            else:
                print("RECORD AVAILABLE! CAN'T ADD ITEM")
        except:
            print("AN ERROR HAS ARISEN!! CHECK THE DETAILS.")
        ans=input("Enter do u want to add more?('y' or 'Y' to continue and 'n' or 'N' to stop)")
        if ans=='y' or ans=='Y':
            continue
        elif ans=='n'or ans=='N':
            break
        else:
            print("INVALID CHOICE")
            break



#MODIFYING ITEMS IN INVENTORY
def i_modify():
    print("Modifying values to INVENTORY table")
    while True:
        try:
            item_no=input("ENTER ITEM NUMBER OF ITEM TO MODIFY:\t\t\t")
            val=(item_no,)
            queryn='''select * from inventory
                   where ITEM_NO=%s;'''
            mycursor.execute(queryn,val)
            results=mycursor.fetchall()
            if mycursor.rowcount<=0:
                print("\\#SORRY! NO MATCHING DETAILS AVAILABLE##")
                break
            else:
                print("What would you like to modify('1.Item_name','2.Category','3.Quantity','4.Cost','5.Date_of_manufacture','6.Expiry_date')?")
                mod=int(input("pls enter:"))
                if mod==1:
                    newname=input("Enter new item name:")
                    val=(newname,item_no)
                    query="""update inventory
                          set ITEM_NAME=%s"
                          where ITEM_NO=%s;"""
                    mycursor.execute(query,val)
                if mod==2:
                    cat=input("Enter the category:")
                    val=(cat,item_no)
                    query="""update inventory
                         set CATEGORY=%s"
                         where ITEM_NO=%s;"""
                    mycursor.execute(query,val)
                if mod==3:
                    newquant=int(input("Enter the quantity:"))
                    val=(newquant,item_no)
                    query="""update inventory
                          set ORIGINAL_QUANTITY=%s
                          where ITEM_NO=%s;"""
                    mycursor.execute(query,val)
                if mod==4:
                    newcost=input("Enter new cost:")
                    val=(newcost,item_no)
                    query="""update inventory
                          set COST_PER_ITEM=%s"
                          where ITEM_NO=%s;"""
                    mycursor.execute(query,val)
                if mod==5:
                    newdom=input("Enter new date of manufacture in correct format:")
                    val=(newdom,item_no)
                    query="""update inventory
                          set DATE_OF_MANUFACTURE=%s"
                          where ITEM_NO=%s;"""
                    mycursor.execute(query,val)
                if mod==6:
                    newexpd=input("Enter new expiry date in correct format:")
                    val=(newexpd,item_no)
                    query="""update inventory
                          set EXPIRY_DATE=%s"
                          where ITEM_NO=%s;"""
                    mycursor.execute(query,val)
                mydb.commit()
        except:
            print("AN ERROR HAS ARISEN! UNABLE TO ADD ITEM.")
            break                
        print('--------------------------------------------------')
        print("ITEM MODIFIED SUCCESSFULLY")
        print('--------------------------------------------------')
        ans=input("Enter do u want to modify more?('y' or 'Y' to continue and 'n' or 'N' to stop)")
        if ans=='y' or ans=='Y':
            continue
        elif ans=='N' or ans=='n':
            break
        else:
            print("INVALID CHOICE!")




#DELETING ITEM FROM INVENTORY
try:
    def i_del():
        print("Deleting values from INVENTORY table")
        while True:
            item_no=input("Enter item number of item to delete:\t\t\t")
            val=(item_no,)
            queryn='''select * from inventory
                      where ITEM_NO=%s;'''
            mycursor.execute(queryn,val)
            results=mycursor.fetchall()
            if mycursor.rowcount<=0:
                print("\\#SORRY! NO MATCHING DETAILS AVAILABLE##")
            else:
                ask=input("ARE YOU SURE YOU WANT TO DELETE ITEM FROM INVENTORY(Y/N)")
                if ask=='Y' or ask=='y':
                    query='''delete from INVENTORY
                             where ITEM_NO=%s;'''
                    mycursor.execute(query,val)
                    mydb.commit()
                    print('---------------------------------------------')
                    print('ITEM DELETED SUCCESSFULLY')
                    print('---------------------------------------------')
                elif ask=='N' or ask=='n':
                    break
                else:
                    print("INVALID CHOICE")
                    break                
            ans=input("Enter do u want to delete more?('y' or 'Y' to continue and 'n' or 'N' to stop)")
            if ans=='n' or ans=='N':
                break
            elif ans=='y' or ans=='Y':
                continue
            else:
                print("INVALID INPUT")
                break
except:
    print("ERROR IN DELETING!!")
    mydb.rollback()







#SEARCHING ITEMS FROM INVENTORY
try:
    def i_search():
        print("Searching values from INVENTORY table")
        while True:
            try:
                print("Do you want to search through item number or item name?Press '1' for item number and '2' for item name")
                ser=int(input("Enter ur choice"))
                if ser==1:
                    item_no=input("Enter item number of item to search:\t\t\t")
                    val=(item_no,)
                    query='''select * from inventory
                             where ITEM_NO=%s;'''
                    mycursor.execute(query,val)
                    results=mycursor.fetchall()
                    if mycursor.rowcount<=0:
                        print("\\#SORRY! NO MATCHING DETAILS AVAILABLE##")
                    else:
                        print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
                        print('%5s'%"ITEM_NO",'%15s'%'ITEM_NAME','%20s'%"ITEM_TYPE",'%20s'%'ORIGINAL_QTY','%20s'%'QUANTITY AVAILABLE','%15s'%'COST','%25s'%'DATE_OF_MANUFACTURE','%20s'%'EXPIRY_DATE')
                        print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
                        for row in results:
                            print('%5s'%row[0],'%15s'%row[1],'%20s'%row[2],'%15s'%row[3],'%20s'%row[4],'%20s'%row[5],'%25s'%row[6],'%20s'%row[7])
                    print("-"*130)
                elif ser==2:
                    item_name=input("Enter item name to be searched:\t\t\t")
                    val=(item_name,)
                    query='''select * from inventory
                             where ITEM_NAME=%s;'''
                    mycursor.execute(query,val)
                    results=mycursor.fetchall()
                    if mycursor.rowcount<=0:
                        print("\\#SORRY! NO MATCHING DETAILS AVAILABLE##")
                    else:
                        print("------------------------------------------------------------------------------------------------------------------")
                        print('%5s'%"ITEM_NO",'%15s'%'ITEM_NAME','%12s'%"ITEM_TYPE",'%10s'%'ORIGINAL_QTY','%10s'%'QUANTITY','%12s'%'COST','%25s'%'DATE_OF_MANUFACTURE','%20s'%'EXPIRY_DATE')
                        print("------------------------------------------------------------------------------------------------------------------")
                        for row in results:
                            print('%5s'%row[0],'%18s'%row[1],'%10s'%row[2],'%10s'%row[3],'%10s'%row[4],'%14s'%row[5],'%20s'%row[6],'%22s'%row[7])
                        print("-"*115)
                else:
                    print("INVALID CHOICE")        
            except:
                print("AN ERROR HAS OCCURED")
            ans=input("Enter do u want to search more?('y' or 'Y' to continue and 'n' or 'N' to stop)")
            if ans=='n' or ans=='N':
                break
            elif ans=='y' or ans=='Y':
                continue
            else:
                print("INVALID CHOICE")
                break
except:
    print("ERROR IN SEARCHING DATA")






#INSERTING VALUES INTO SALES TABLE(BY ADMIN)

def s_nins():
    while True:
        print("Inserting items into SALES table")
        print("-----------------------------------------------------------------")
        print("DO YOU WANT TO SEE THE MENU?")
        ans=input("Enter your answer")
        if ans=='y' or ans=='Y':
            query='''select * from inventory'''
            mycursor.execute(query)
            results=mycursor.fetchall()
            if mycursor.rowcount<=0:
                print("\\#SORRY! NO MATCHING DETAILS AVAILABLE##")
            else:
                print("------------------------------------------------------------------------------------------------------------------------------------")
                print('%5s'%"ITEM_NO",'%25s'%'ITEM_NAME','%20s'%"ITEM_TYPE",'%15s'%'QUANTITY','%12s'%'COST','%25s'%'DATE_OF_MANUFACTURE','%18s'%'EXPIRY_DATE')
                print("------------------------------------------------------------------------------------------------------------------------------------")
                for row in results:
                    print('%5s'%row[0],'%30s'%row[1],'%20s'%row[2],'%10s'%row[4],'%14s'%row[5],'%20s'%row[6],'%22s'%row[7])
                print("------------------------------------------------------------------------------------------------------------------------------------")
                print()
                print()
                print()
                try:
                    ino=input("ENTER THE ITEM NO OF THE ITEM WHICH YOU WOULD LIKE TO HAVE:")
                    mycursor.execute("select * from inventory where ITEM_NO='%s'"%(ino))
                    count=mycursor.fetchall()
                except:
                    print("ERROR IN ITEM_NO")
                if mycursor.rowcount<=0:
                    print('ITEM NOT AVAILABLE')
                else:
                    mycursor.execute("select Quantity from inventory where ITEM_NO='%s'"%(ino))
                    cty=mycursor.fetchall()
                    if int(cty[0][0])<0 or int(cty[0][0])==0:
                        mycursor.execute("update inventory set quantity=0 where ITEM_NO='%s'"%(ino))
                        print('ITEM NOT AVAILABLE')
                    else:
                        qn=int(input("ENTER THE QUANTITY:"))
                        if qn==0 or qn<0:
                            print('ORDER CANNOT BE PLACED!! PLEASE ENTER A VALID QUANTITYY')
                        elif qn>int(cty[0][0]):
                            print("QUANTITY AVAILABLE IS:",int(cty[0][0]))
                            new_qty=int(input("Enter new Quantity?"))
                            if new_qty==0 or new_qty>int(cty[0][0]):
                                print("SORRY! ORDER CANNOT BE PLACED")
                            else:
                                mycursor.execute('select ITEM_NO from sales')
                                rows=mycursor.fetchall()
                                a=[]                                            # CHECKING IF THE ITEM_NO IS ALREADY IN SALES
                                for i in rows:
                                    for j in i:
                                        a.append(j)
                                if ino not in a:
                                    try:
                                        mycursor.execute("insert into sales(ITEM_NO,Quantity) values('%s',%d)"%(ino,qn))
                                        mycursor.execute("update sales s , inventory i set s.ITEM_NO=i.ITEM_NO, s.ITEM_NAME=i.ITEM_NAME,s.SUM_OF_TOTAL_=0,s.DATE_OF_PURCHASE=curdate(),s.COST=i.COST_PER_ITEM,Total_cost=i.COST_PER_ITEM*s.Quantity where s.ITEM_NO=i.ITEM_NO")
                                        mycursor.execute("update inventory set Quantity=Quantity-'%d' where ITEM_NO='%s'"%(qn,ino))
                                        mydb.commit()
                                        print("YOUR ORDER HAS BEEN ADDED SUCCESSFULLY.")
                                    except:
                                        print("ORDER CANNOT BE ADDED!")
                                        mydb.rollback()
                                else:
                                    try:
                                        mycursor.execute("update sales set quantity=quantity+'%d' where ITEM_NO='%s'"%(qn,ino))
                                        mycursor.execute("update sales s , inventory i set s.ITEM_NO=i.ITEM_NO, s.ITEM_NAME=i.ITEM_NAME,s.SUM_OF_TOTAL_=SUM_OF_TOTAL_+0,s.DATE_OF_PURCHASE=curdate(), s.COST=i.COST_PER_ITEM,Total_cost=i.COST_PER_ITEM*s.Quantity where s.ITEM_NO=i.ITEM_NO")
                                        mycursor.execute("update inventory set Quantity=Quantity-'%d' where ITEM_NO='%s'"%(qn,ino))
                                        mydb.commit()
                                        print("YOUR ORDER HAS BEEN ADDED SUCCESSFULLY.")
                                    except:
                                        print("ORDER CANNOT BE ADDED")
                                        mydb.rollback()
                        else:
                            mycursor.execute('select ITEM_NO from sales')
                            rows=mycursor.fetchall()
                            a=[]                            # ORDER LIST FOR USER
                            for i in rows:
                                for j in i:
                                    a.append(j)
                            if ino in a:                    #CHECKING IF THE ITEM_NO IS PRESENT IN SALES
                                try:
                                    mycursor.execute("update sales set quantity=quantity+'%d' where ITEM_NO='%s'"%(qn,ino))
                                    mycursor.execute("update sales s , inventory i set s.ITEM_NO=i.ITEM_NO, s.ITEM_NAME=i.ITEM_NAME,s.SUM_OF_TOTAL_=SUM_OF_TOTAL_+0,s.DATE_OF_PURCHASE=curdate(), s.COST=i.COST_PER_ITEM, s.CATEGORY=i.CATEGORY, Total_cost=i.COST_PER_ITEM*s.Quantity where s.ITEM_NO=i.ITEM_NO")
                                    mycursor.execute("update inventory set Quantity=Quantity-'%d' where ITEM_NO='%s'"%(qn,ino))
                                    mydb.commit()
                                    print("ORDER ADDED SUCCESSFULLY.")
                                except:
                                    mydb.rollback()
                                    print("ORDER CANNOT BE ADDED!")
                            else:
                                try:
                                    mycursor.execute("insert into sales(ITEM_NO,Quantity) values('%s',%d)"%(ino,qn))
                                    mycursor.execute("update sales s , inventory i set s.ITEM_NO=i.ITEM_NO,s.ITEM_NAME=i.ITEM_NAME,s.SUM_OF_TOTAL_=0,s.DATE_OF_PURCHASE=curdate(),s.COST=i.COST_PER_ITEM,s.CATEGORY=i.CATEGORY,Total_cost=i.COST_PER_ITEM*s.Quantity where s.ITEM_NO=i.ITEM_NO")
                                    mycursor.execute("update inventory set Quantity=Quantity-'%d' where ITEM_NO='%s'"%(qn,ino))
                                    mydb.commit()
                                    print("ORDER SUCCESSFULLY ADDED.")
                                except:
                                    mydb.rollback()
                                    print("ORDER CANNOT BE ADDED!")
        elif ans=='N' or ans=='n':
            ino=input("ENTER THE ITEM NO OF THE ITEM WHICH YOU WOULD LIKE TO HAVE:")
            mycursor.execute("select * from inventory where ITEM_NO='%s'"%(ino))
            count=mycursor.fetchall()
            if mycursor.rowcount<=0:
                print('ITEM NOT AVAILABLE')
            else:
                mycursor.execute("select Quantity from inventory where ITEM_NO='%s'"%(ino))
                cty=mycursor.fetchall()
                if int(cty[0][0])<0 or int(cty[0][0])==0:
                    mycursor.execute("update inventory set quantity=0 where ITEM_NO='%s'"%(ino))
                    print('ITEM NOT AVAILABLE')
                else:
                    qn=int(input("ENTER THE QUANTITY:"))
                    if qn==0 :
                        print('ORDER CANNOT BE PLACED!!')
                    elif qn>int(cty[0][0]):
                        print("QUANTITY AVAILABLE IS:",int(cty[0][0]))
                        new_qty=int(input("Enter new Quantity?"))
                        if new_qty==0 or new_qty>int(cty[0][0]):
                            print("SORRY! ORDER CANNOT BE PLACED")
                        else:
                            mycursor.execute('select ITEM_NO from sales')
                            rows=mycursor.fetchall()
                            a=[]
                            for i in rows:
                                for j in i:
                                    a.append(j)
                            if ino not in a:
                                try:
                                    mycursor.execute("insert into sales(ITEM_NO,Quantity) values('%s',%d)"%(ino,qn))
                                    mycursor.execute("update sales s , inventory i set s.ITEM_NO=i.ITEM_NO, s.ITEM_NAME=i.ITEM_NAME,s.SUM_OF_TOTAL_=0,s.DATE_OF_PURCHASE=curdate(), s.COST=i.COST_PER_ITEM,Total_cost=i.COST_PER_ITEM*s.Quantity where s.ITEM_NO=i.ITEM_NO")
                                    mycursor.execute("update inventory set Quantity=Quantity-'%d' where ITEM_NO='%s'"%(qn,ino))
                                    mydb.commit()
                                    print("ORDER ADDED SUCCESSFULLY.")
                                except:
                                    print("ORDER CANNOT BE ADDED!")
                                    mydb.rollback()
                            else:
                                try:
                                    mycursor.execute("update sales set quantity=quantity+'%d' where ITEM_NO='%s'"%(qn,ino))
                                    mycursor.execute("update sales s , inventory i set s.ITEM_NO=i.ITEM_NO, s.ITEM_NAME=i.ITEM_NAME,s.SUM_OF_TOTAL_=SUM_OF_TOTAL_+0,s.DATE_OF_PURCHASE=curdate(), s.COST=i.COST_PER_ITEM,Total_cost=i.COST_PER_ITEM*s.Quantity where s.ITEM_NO=i.ITEM_NO")
                                    mycursor.execute("update inventory set Quantity=Quantity-'%d' where ITEM_NO='%s'"%(qn,ino))
                                    mydb.commit()
                                    print("ORDER ADDED SUCCESSFULLY.")
                                except:
                                    print("ORDER CANNOT BE ADDED!")
                                    mydb.rollback()
                    else:
                        mycursor.execute('select ITEM_NO from sales')
                        rows=mycursor.fetchall()
                        a=[]                    # CHECKING WHETHER THE ITEM IS ALREADY PRESENT IN SALES
                        for i in rows:
                            for j in i:
                                a.append(j)
                        if ino in a:
                            try:
                                mycursor.execute("update sales set quantity=quantity+'%d' where ITEM_NO='%s'"%(qn,ino))
                                mycursor.execute("update sales s , inventory i set s.ITEM_NO=i.ITEM_NO, s.ITEM_NAME=i.ITEM_NAME,s.SUM_OF_TOTAL_=SUM_OF_TOTAL_+0,s.DATE_OF_PURCHASE=curdate(), s.COST=i.COST_PER_ITEM, s.CATEGORY=i.CATEGORY, Total_cost=i.COST_PER_ITEM*s.Quantity where s.ITEM_NO=i.ITEM_NO")
                                mycursor.execute("update inventory set Quantity=Quantity-'%d' where ITEM_NO='%s'"%(qn,ino))
                                mydb.commit()
                                print("ORDER ADDED SUCCESSFULLY.")
                            except:
                                print("ORDER CANNOT BE ADDED!")
                                mydb.rollback()
                        else:
                            try:
                                mycursor.execute("insert into sales(ITEM_NO,Quantity) values('%s',%d)"%(ino,qn))
                                mycursor.execute("update sales s , inventory i set s.ITEM_NO=i.ITEM_NO,s.ITEM_NAME=i.ITEM_NAME,s.SUM_OF_TOTAL_=0,s.DATE_OF_PURCHASE=curdate(),s.COST=i.COST_PER_ITEM,s.CATEGORY=i.CATEGORY,Total_cost=i.COST_PER_ITEM*s.Quantity where s.ITEM_NO=i.ITEM_NO")
                                mycursor.execute("update inventory set Quantity=Quantity-'%d' where ITEM_NO='%s'"%(qn,ino))
                                mydb.commit()
                                print("ORDER SUCCESSFULLY ADDED")
                            except:
                                print("ORDER CANNOT BE ADDED")
                                mydb.rollback()
                            
            
                
        ans=input("DO YOU WANT TO ADD MORE ITEMS INTO THE SALES TABLE?(Y/N)")
        if ans=='y' or ans=='Y':
            continue
        elif ans=='n' or ans=='N':
            break
        else:
            print("INVALID CHOICE")





#INSERTING VALUES BY USER
def s_nuins():
    while True:
        try:
            ino=input("ENTER THE ITEM NO OF THE ITEM WHICH YOU WOULD LIKE TO HAVE:")
            mycursor.execute("select * from inventory where ITEM_NO='%s'"%(ino))
            count=mycursor.fetchall()
        except:
            print("PLS ENTER PROPER ITEM_NO")
        if mycursor.rowcount<=0:
            print('ITEM NOT AVAILABLE! PLEASE ENTER VALID ITEM_NO')
        else:
            mycursor.execute("select Quantity from inventory where ITEM_NO='%s'"%(ino))
            cty=mycursor.fetchall()
            if int(cty[0][0])<0 or int(cty[0][0])==0:
                mycursor.execute("update inventory set quantity=0 where ITEM_NO='%s'"%(ino))
                print('ITEM NOT AVAILABLE')
            else:
                qn=int(input("ENTER THE QUANTITY:"))
                if qn==0 :
                    print('ORDER CANNOT BE PLACED!!')
                elif qn>int(cty[0][0]):
                    print("QUANTITY AVAILABLE IS:",int(cty[0][0]))
                    ch=input("Do you want to continue with the available quantity?(Y OR y FOR 'YES' AND N OR n FOR 'NO')")
                    if ch=='y' or ch=='Y':
                        new_qty=int(input("Enter new Quantity?"))
                        if new_qty==0 or new_qty>int(cty[0][0]):
                            print("SORRY! ORDER CANNOT BE PLACED")
                        else:
                            mycursor.execute('select ITEM_NO from sales')
                            rows=mycursor.fetchall()
                            a=[]
                            for i in rows:
                                for j in i:
                                    a.append(j)
                            if ino not in a:
                                try:
                                    mycursor.execute("insert into sales(ITEM_NO,Quantity) values('%s',%d)"%(ino,qn))
                                    mycursor.execute("update sales s , inventory i set s.ITEM_NO=i.ITEM_NO, s.ITEM_NAME=i.ITEM_NAME, s.DATE_OF_PURCHASE=curdate(),s.COST=i.COST_PER_ITEM, Total_cost=i.COST_PER_ITEM*s.Quantity where s.ITEM_NO=i.ITEM_NO")
                                    mycursor.execute("update inventory set Quantity=Quantity-'%d' where ITEM_NO='%s'"%(qn,ino))
                                    mycursor.execute("select ITEM_NO, ITEM_NAME, CATEGORY, '%s', COST_PER_ITEM, COST_PER_ITEM*%s from INVENTORY where ITEM_NO='%s'"%(qn,qn,ino))
                                    rows=mycursor.fetchall()
                                    for i in rows:
                                        ol.append(i)       # ADDING ORDER TO USER'S LIST
                                        oln.append(list(i))
                                    mydb.commit()
                                    print("Added the order")
            
                                except:
                                    print("COULDN'T ADD THE ORDER!")
                                    mydb.rollback()
                            else:
                                try:
                                    mycursor.execute("update sales set quantity=quantity+'%d' where ITEM_NO='%s'"%(qn,ino))
                                    mycursor.execute("update sales s , inventory i set s.ITEM_NO=i.ITEM_NO, s.ITEM_NAME=i.ITEM_NAME, s.DATE_OF_PURCHASE=curdate(),s.COST=i.COST_PER_ITEM, Total_cost=i.COST_PER_ITEM*s.Quantity where s.ITEM_NO=i.ITEM_NO")
                                    mycursor.execute("update inventory set Quantity=Quantity-'%d' where ITEM_NO='%s'"%(qn,ino))
                                    mycursor.execute("select ITEM_NO, ITEM_NAME, CATEGORY, '%s', COST_PER_ITEM, COST_PER_ITEM*%s from INVENTORY where ITEM_NO='%s'"%(qn,qn,ino))
                                    rows=mycursor.fetchall()
                                    for i in rows:
                                        ol.append(i)
                                        oln.append(list(i))
                                    mydb.commit()
                                    print("Added the order")
                                    
                                except:
                                    print("COULDN'T ADD THE ORDER!")
                    elif ch=='n' or ch=='N':
                        pass
                else:
                    mycursor.execute('select ITEM_NO from sales')
                    rows=mycursor.fetchall()
                    a=[]
                    for i in rows:
                        for j in i:
                            a.append(j)
                    if ino in a:
                        try:
                            mycursor.execute("update sales set quantity=quantity+'%d' where ITEM_NO='%s'"%(qn,ino))
                            mycursor.execute("update sales s , inventory i set s.ITEM_NO=i.ITEM_NO, s.ITEM_NAME=i.ITEM_NAME, s.DATE_OF_PURCHASE=curdate(),s.COST=i.COST_PER_ITEM, s.CATEGORY=i.CATEGORY,Total_cost=i.COST_PER_ITEM*s.Quantity where s.ITEM_NO=i.ITEM_NO")
                            mycursor.execute("update inventory set Quantity=Quantity-'%d' where ITEM_NO='%s'"%(qn,ino))
                            mycursor.execute("select ITEM_NO, ITEM_NAME, CATEGORY, '%s', COST_PER_ITEM, COST_PER_ITEM*%s from INVENTORY where ITEM_NO='%s'"%(qn,qn,ino))
                            rows=mycursor.fetchall()
                            for i in rows:
                                ol.append(i)
                                oln.append(list(i))    # ADDING ORDER TO USER'S LIST
                            mydb.commit()
                            print("Added the order")
                                                       
                        except:
                            print("COULDN'T ADD THE ORDER!")
                    else:
                        try:
                            mycursor.execute("insert into sales(ITEM_NO,Quantity) values('%s',%d)"%(ino,qn))
                            mycursor.execute("update sales s , inventory i set s.ITEM_NO=i.ITEM_NO,s.ITEM_NAME=i.ITEM_NAME,s.DATE_OF_PURCHASE=curdate(),s.COST=i.COST_PER_ITEM,s.CATEGORY=i.CATEGORY,Total_cost=i.COST_PER_ITEM*s.Quantity where s.ITEM_NO=i.ITEM_NO")
                            mycursor.execute("update inventory set Quantity=Quantity-'%d' where ITEM_NO='%s'"%(qn,ino))
                            mycursor.execute("select ITEM_NO, ITEM_NAME, CATEGORY, '%s', COST_PER_ITEM, COST_PER_ITEM*%s from INVENTORY where ITEM_NO='%s'"%(qn,qn,ino))
                            rows=mycursor.fetchall()
                            for i in rows:
                                ol.append(i)
                                oln.append(list(i))     # ADDING ORDER TO USER'S LIST
                            mydb.commit()
                            print("ORDER SUCCESSFULLY ADDED")
                            
                        except:
                            print("COULDN'T ADD THE ORDER")
        ans=input("ENTER DO YOU WANT TO ORDER MORE?(Y/N)")
        if ans=='y' or ans=='Y':
            continue
        elif ans=='n' or ans=='N':
            break
        else:
            print("INVALID CHOICE")
            break









#MODIFYING ITEMS FROM SALES TABLE(BY ADMIN)

def s_nmodify():
    while True:
        try:
            ino=input("ENTER THE ITEM NO OF THE ITEM TO BE MODIFIED:")
            found=0
            mycursor.execute("select * from sales where ITEM_NO='%s'"%(ino))
            result=mycursor.fetchall()
            if mycursor.rowcount<=0:
                print("\\#SORRY! NO MATCHING DETAILS AVAILABLE## CAN'T MODIFY")
                found=0
            else:
                found=1
        except:
            print("ERROR IN VALUE")
        if found==0:
            print("ITEM NOT AVAILABLE IN SALES TABLE.")
            ans2=input("WOULD U LIKE TO ADD?(Y/N)")
            if ans2=='y' or ans2=='Y':
                s_nins()
            else:
                break
        else:                    
            mycursor.execute("select * from sales where ITEM_NO='%s'"%(ino))
            result=mycursor.fetchall()
            if mycursor.rowcount<=0:
                print("\\#SORRY! NO MATCHING DETAILS AVAILABLE## CAN'T MODIFY")
            else:
                print("YOU CAN MODIFY ONLY QUANTITY")
                qn=int(input("ENTER THE QUANTITY"))
                ans=int(input("DO YOU WANT TO 1. ADD OR 2. DELETE THE QUANTITY"))
                if ans==1:
                    mycursor.execute("select Quantity from inventory where ITEM_NO='%s'"%(ino))
                    cty=mycursor.fetchall()
                    if int(cty[0][0])<0 or int(cty[0][0])==0:
                        mycursor.execute("update inventory set quantity=0 where ITEM_NO='%s'"%(ino))
                        print('ITEM NOT AVAILABLE')
                    elif qn>int(cty[0][0]):
                        print("QUANTITY AVAILABLE IS:",int(cty[0][0]))
                        new_qn=int(input("ENTER PROPER QUANTITY TO ADD"))
                        
                        mycursor.execute("update sales set QUANTITY=QUANTITY+'%d' where ITEM_NO='%s'"%(new_qn,ino))
                        mycursor.execute("update sales s , inventory i set s.ITEM_NO=i.ITEM_NO, s.ITEM_NAME=i.ITEM_NAME,s.DATE_OF_PURCHASE=curdate(), s.COST=i.COST_PER_ITEM, s.CATEGORY=i.CATEGORY,Total_cost=i.COST_PER_ITEM*s.Quantity where s.ITEM_NO=i.ITEM_NO")
                        mycursor.execute("update inventory set QUANTITY=QUANTITY-'%d' where ITEM_NO='%s'"%(new_qn,ino))
                        mydb.commit()
                        print("QUANTITY MODIFIED")
                                
                            
                    else:
                            
                        mycursor.execute("update sales set QUANTITY=QUANTITY+'%d' where ITEM_NO='%s'"%(qn,ino))
                        mycursor.execute("update sales s , inventory i set s.ITEM_NO=i.ITEM_NO, s.ITEM_NAME=i.ITEM_NAME,s.DATE_OF_PURCHASE=curdate(), s.COST=i.COST_PER_ITEM, s.CATEGORY=i.CATEGORY,Total_cost=i.COST_PER_ITEM*s.Quantity where s.ITEM_NO=i.ITEM_NO")
                        mycursor.execute("update inventory set QUANTITY=QUANTITY-'%d' where ITEM_NO='%s'"%(qn,ino))
                        mydb.commit()
                        print("QUANTITY MODIFIED")
                                
                                                      
                                
                elif ans==2:
            
                    mycursor.execute("update sales set QUANTITY=QUANTITY-'%d' where ITEM_NO='%s'"%(qn,ino))
                    mycursor.execute("update sales s , inventory i set s.ITEM_NO=i.ITEM_NO, s.ITEM_NAME=i.ITEM_NAME,s.DATE_OF_PURCHASE=curdate(), s.COST=i.COST_PER_ITEM, s.CATEGORY=i.CATEGORY, Total_cost=i.COST_PER_ITEM*s.Quantity where s.ITEM_NO=i.ITEM_NO")
                    mycursor.execute("update inventory set QUANTITY=QUANTITY+'%d' where ITEM_NO='%s'"%(qn,ino))
                    mydb.commit()
                    print("QUANTITY MODIFIED")
                            
                        
                else:
                    print("INVALID CHOICE!!")
        an=input("DO YOU WANT TO MODIFY MORE?")
        if an=='y' or an=='Y':
            continue
        else:
            break







#MODIFYING ITEMS FROM SALES TABLE (BY USER)
def s_umodifyy():
    while True:
        ino=input("ENTER THE ITEM NO OF THE ITEM TO BE MODIFIED:")
        found=0
        for i in range(len(oln)):
            if oln[i][0]==ino:
                found=1
                break
            else:
                found=0
        if not found:
            print("YOU HAVEN'T ORDERED THIS ITEM, PLS DO ORDER IT FIRST TO MODIFY")
            ans2=input("WOULD U LIKE TO ORDER?(Y/N)")
            if ans2=='y' or ans2=='Y':
                s_nuins()
                break
            else:
                break
        else:
            mycursor.execute("select * from sales where ITEM_NO='%s'"%(ino))
            result=mycursor.fetchall()
            if mycursor.rowcount<=0:
                print("\\#SORRY! NO MATCHING DETAILS AVAILABLE## CAN'T MODIFY")
            else:
                print("YOU CAN MODIFY ONLY QUANTITY")
                qn=int(input("ENTER THE QUANTITY"))
                ans=int(input("DO YOU WANT TO 1. ADD OR 2. DELETE THE QUANTITY"))
                if ans==1:
                    mycursor.execute("select Quantity from inventory where ITEM_NO='%s'"%(ino))
                    cty=mycursor.fetchall()
                    if int(cty[0][0])<0 or int(cty[0][0])==0:
                        mycursor.execute("update inventory set quantity=0 where ITEM_NO='%s'"%(ino))
                        print('ITEM NOT AVAILABLE')
                    elif qn>int(cty[0][0]):
                        print("QUANTITY AVAILABLE IS:",int(cty[0][0]))
                        new_qn=int(input("ENTER PROPER QUANTITY TO ADD"))
                        try:
                            mycursor.execute("update sales set QUANTITY=QUANTITY+'%d' where ITEM_NO='%s'"%(new_qn,ino))
                            mycursor.execute("update sales s , inventory i set s.ITEM_NO=i.ITEM_NO, s.ITEM_NAME=i.ITEM_NAME,s.DATE_OF_PURCHASE=curdate(), s.COST=i.COST_PER_ITEM, s.CATEGORY=i.CATEGORY,Total_cost=i.COST_PER_ITEM*s.Quantity where s.ITEM_NO=i.ITEM_NO")
                            mycursor.execute("update inventory set QUANTITY=QUANTITY-'%d' where ITEM_NO='%s'"%(new_qn,ino))
                            for i in range(len(oln)):
                                if oln[i][0]==ino:
                                    oln[i][3]=int(oln[i][3])+new_qn #modifying quantity and cost in the order list
                                    oln[i][5]=int(oln[i][3])*int(oln[i][4])
                            mydb.commit()
                            print("QUANTITY MODIFIED")
                            
                        except:
                            print("COULDN'T MODIFY THE ITEM")
                    else:
                        try:
                            mycursor.execute("update sales set QUANTITY=QUANTITY+'%d' where ITEM_NO='%s'"%(qn,ino))
                            mycursor.execute("update sales s , inventory i set s.ITEM_NO=i.ITEM_NO, s.ITEM_NAME=i.ITEM_NAME,s.DATE_OF_PURCHASE=curdate(), s.COST=i.COST_PER_ITEM, DATE_OF_PURCHASE=curdate(),s.CATEGORY=i.CATEGORY,Total_cost=i.COST_PER_ITEM*s.Quantity where s.ITEM_NO=i.ITEM_NO")
                            mycursor.execute("update inventory set QUANTITY=QUANTITY-'%d' where ITEM_NO='%s'"%(qn,ino))
                            for i in range(len(oln)):
                                if oln[i][0]==ino:
                                    oln[i][3]=int(oln[i][3])+qn #modifying quantity and cost in the order list
                                    oln[i][5]=int(oln[i][3])*int(oln[i][4])
                            mydb.commit()
                            print("QUANTITY MODIFIED")
                            
                        except:
                            print("COULDN'T MODIFY ITEM")
                elif ans==2:
                    for i in range(len(oln)):
                        if qn>int(oln[i][3]):
                            print("QUANTITY ORDERED IS:",oln[i][3])
                        ans=input("DO YOU WANT TO DELETE IT COMPLETELY??(Y/N)")
                        if ans=='Y':
                            oln[i][3]='0'
                        elif ans=='N' or ans=='n':
                            qnn=int(input("ENTER NEW QUANTITY TO DELETE"))
                            try:
                                mycursor.execute("update sales set QUANTITY=QUANTITY-'%d' where ITEM_NO='%s'"%(qnn,ino))
                                mycursor.execute("update sales s , inventory i set s.ITEM_NO=i.ITEM_NO, s.ITEM_NAME=i.ITEM_NAME,s.DATE_OF_PURCHASE=curdate(), s.COST=i.COST_PER_ITEM, s.CATEGORY=i.CATEGORY, Total_cost=i.COST_PER_ITEM*s.Quantity where s.ITEM_NO=i.ITEM_NO")
                                mycursor.execute("update inventory set QUANTITY=QUANTITY+'%d' where ITEM_NO='%s'"%(qnn,ino))
                                for i in range(len(oln)):
                                    if oln[i][0]==ino:
                                        oln[i][3]=int(oln[i][3])-qnn
                                        oln[i][5]=int(oln[i][3])*int(oln[i][4])
                                mydb.commit()
                                print("QUANTITY MODIFIED")
                                
                            except:
                                print("COULDN'T MODIFY ITEM")                       
                        else:
                            try:
                                mycursor.execute("update sales set QUANTITY=QUANTITY-'%d' where ITEM_NO='%s'"%(qn,ino))
                                mycursor.execute("update sales s , inventory i set s.ITEM_NO=i.ITEM_NO, s.ITEM_NAME=i.ITEM_NAME,s.DATE_OF_PURCHASE=curdate(), s.COST=i.COST_PER_ITEM, s.CATEGORY=i.CATEGORY, Total_cost=i.COST_PER_ITEM*s.Quantity where s.ITEM_NO=i.ITEM_NO")
                                mycursor.execute("update inventory set QUANTITY=QUANTITY+'%d' where ITEM_NO='%s'"%(qn,ino))
                                for i in range(len(oln)):
                                    if oln[i][0]==ino:
                                        oln[i][3]=int(oln[i][3])-qn
                                        oln[i][5]=int(oln[i][3])*int(oln[i][4])
                                mydb.commit()
                                print("QUANTITY MODIFIED")
                            except:
                                print("COULDN'T MODIFY ITEM")
                else:
                    print("INVALID CHOICE!!")
        an=input("DO YOU WANT TO MODIFY MORE?")
        if an=='y' or an=='Y':
            continue
        else:
            break







#DELETING ITEMS FROM SALES TABLE(ONLY ADMIN)
try:
    def s_del():
        while True:
            ino=input("ENTER THE ITEM NO OF THE ITEM TO BE DELETED:")
            mycursor.execute("select * from sales where ITEM_NO='%s'"%(ino))
            result=mycursor.fetchall()
            if mycursor.rowcount<=0:
                print("\\#SORRY! NO MATCHING DETAILS AVAILABLE##   CAN'T DELETE")
            else:
                print("------------------------------------------------------------------------------------------------------------------------------------")
                print('%5s'%"ITEM_NO",'%25s'%'ITEM_NAME','%20s'%"ITEM_TYPE",'%15s'%'QUANTITY','%12s'%'COST','%25s'%'DATE_OF_MANUFACTURE','%18s'%'EXPIRY_DATE')
                print("------------------------------------------------------------------------------------------------------------------------------------")
                for i in result:
                    print('%5s'%i[0],'%30s'%i[1],'%20s'%i[2],'%10s'%i[3],'%14s'%i[4],'%20s'%i[5],'%22s'%i[6])
                    print("------------------------------------------------------------------------------------------------------------------------------------")
                    dqty=i[4]
                    ans=input("ARE YOU SURE YOU WANT TO DELETE THIS ITEM??(y/n)")
                    if ans=='y':
                        try:
                            mycursor.execute("delete from sales where ITEM_NO='%s'"%(ino))
                            mycursor.execute("update inventory set quantity=quantity+'%d' where ITEM_NO='%s'"%(dqty,ino))
                            mydb.commit()
                            print("DELETED ITEM FROM SALES TABLE")
                        except:
                            print("ERROR IN DELETING FROM SALES TABLE")
                    else:
                        pass
            ans=input("DO WANT TO DELETE MORE ITEMS:(y/n)")
            if ans=='y':
                continue
            else:
                break
except:
    print("Error in deleting")







#PASSWORD CREATION
def passwd_creation():
    while True:
        try:
            u_name=input("PLS GIVE A PROPER USERNAME:")
            query='''select USERNAME from login;;'''
            mycursor.execute(query)
            row=mycursor.fetchall()
        except:
            print("AN ERROR HAS OCCURED!")
            break
        for i in row:
            if i==(u_name,):
                print("USERNAME ALREADY EXISTS, PLS GIVE AN ALTERNATIVE PASSWD")
                break
        else:
            while True:
                print("RULES FOR CREATING PASSWORD")
                print()
                print("1. Password length must be between 5-10 characters")
                print()
                print("2. There must not be any spaces.")
                print()
                print("3. There must be atleas 1 digit.")
                print()
                print("4. There must be atleast 1 special character.")
                print()
                passwd=passwordbox("ENTER PASSWORD:")
                query='''select passwd from login;'''
                mycursor.execute(query)
                rows=mycursor.fetchall()
                f=0
                for i in rows:
                    if i==(passwd,):
                        f=1
                new_psw=list(passwd)
                if f==0:
                    if ' ' in new_psw:
                        print("THERE IS A SPACE IN PASSWORD")
                        continue
                    if len(new_psw)>10:
                        print("EXCEEDING CHARACTER LIMIT. ONLY 10 CHARACTERS PERMITTED")
                        continue
                    if len(new_psw)<5:
                        print("PASSWORD SHOULD CONTAIN ATLEAST 5 CHARACTERS. PLS REENTER")
                        continue
                    found=0
                    for j in new_psw:
                        if j in '0123456789':
                            found=1
                    if found==0:
                        print("PASSWORD SHOULD CONTAIN ATLEAST ONE DIGIT. PLS RE-ENTER.")
                        continue
                    flag=0
                    for k in new_psw:
                        if k in '!@#$%^&*?':
                            flag=1
                    if flag==0:
                        print("PASSWORD SHOULD CONTAIN ATLEAST ONE SPECIAL CHARACTER. PLS RE-ENTER.")
                        continue
                    else:
                        query1='''insert into login values('%s','%s',1);'''%(u_name,passwd)
                        mycursor.execute(query1)
                        mydb.commit()
                        print("LOGIN SUCCESSFUL!")
                        return u_name,passwd
                        break
                else:
                    print("PASSWD ALREADY EXISTS")
                    print()
                    print("RULES FOR CREATING PASSWORD")
                    print()
                    print("1. Password length must be between 5-10 characters")
                    print()
                    print("2. There must not be any spaces.")
                    print()
                    print("3. There must be atleas 1 digit.")
                    print()
                    print("4. There must be atleast 1 special character.")
                    print()
                    new_pswd=passwordbox("ENTER NEW PASSWORD:")
                    new_psw=list(new_pswd)
                    if ' ' in new_psw:
                        print("THERE IS A SPACE IN PASSWORD")
                        continue
                    if len(new_psw)>10:
                        print("EXCEEDING CHARACTER LIMIT. ONLY 10 CHARACTERS PERMITTED")
                        continue
                    if len(new_psw)<5:
                        print("PASSWORD SHOULD CONTAIN ATLEAST 5 CHARACTERS. PLS REENTER")
                        continue
                    found=0
                    for j in new_psw:
                        if j in '0123456789':
                            found=1
                    if found==0:
                        print("PASSWORD SHOULD CONTAIN ATLEAST ONE DIGIT. PLS RE-ENTER.")
                        continue
                    flag=0
                    for k in new_psw:
                        if k in '!@#$%^&*?':
                            flag=1
                    if flag==0:
                        print("PASSWORD SHOULD CONTAIN ATLEAST ONE SPECIAL CHARACTER. PLS RE-ENTER.")
                        continue
                    else:
                        query1='''insert into login values('%s','%s',1);'''%(u_name,new_pswd)
                        mycursor.execute(query1)
                        mydb.commit()
                        print("LOGIN SUCCESSFUL!")
                        return u_name,new_pswd
                        break

    




#BILL CREATION(BY USER)
def s_bill():
    c=0
    if oln==[]:
        print('-----------------------------------------')
        print("SORRY! YOU HAVEN'T ORDERED ANYTHING")
        print('-----------------------------------------')
    else:
        print("------------------------------------------------------------------------------------------------------------------------------------")
        print("                                           LLYODS BAKERY                                               ")
        print("------------------------------------------------------------------------------------------------------------------------------------")
        print(datetime.datetime.now())
        if b[0]=='bonus_discount':
            print()
            print('%5s'%"ITEM_NO",'%25s'%'ITEM_NAME','%15s'%'CATEGORY','%15s'%'QUANTITY','%15s'%'COST_PER_ITEM','%20s'%'TOTAL_COST')
            print("------------------------------------------------------------------------------------------------------------------------------------")
            for i in oln:
                print('%5s'%i[0],'%25s'%i[1],'%15s'%i[2],'%15s'%i[3],'%15s'%i[4],'%20s'%i[5])
                c+=i[5]
            print('------------------------------------------------------------------------------------------------------------------------------------')
            print("TOTAL COST:               ",c,"Rs")
            print()
            vis=vis_list[0][0]-0.5
            discount=(int(vis)/100)*c
            print()
            print("TOTAL COST AFTER DISCOUNT:                  ",c-discount,"Rs")
        
        else:    
            print()
            print('%5s'%"ITEM_NO",'%25s'%'ITEM_NAME','%15s'%'CATEGORY','%15s'%'QUANTITY','%15s'%'COST_PER_ITEM','%20s'%'TOTAL_COST')
            print("------------------------------------------------------------------------------------------------------------------------------------")
            discount=0
            for i in oln:
                print('%5s'%i[0],'%25s'%i[1],'%15s'%i[2],'%15s'%i[3],'%15s'%i[4],'%20s'%i[5])
                c+=i[5]
            print('------------------------------------------------------------------------------------------------------------------------------------')
            print("TOTAL COST:               ",c,"Rs")
        query='''select * from sales;'''
        mycursor.execute(query)
        row=mycursor.fetchall()
        mydb.commit()
        if mycursor.rowcount==1:
            query1='''update sales
                   set SUM_OF_TOTAL_='%d';'''%(discount)
            mycursor.execute(query1)
            mydb.commit()
        else:
            query2='''select SUM_OF_TOTAL_ from sales
                   where SUM_OF_TOTAL_ is not null;'''
            mycursor.execute(query2)
            row=mycursor.fetchall()
            mydb.commit()
            c=0
            for i in row:
                for j in i:
                    c+=j
            query3='''update sales
                   set SUM_OF_TOTAL_='%d'+'%d';'''%(c,discount)
            mycursor.execute(query3)
            mydb.commit()
                
        
    

        




#REPORT(BY ADMIN)
def i_rept():
    try:
        rep=[]
        red=[]
        print()
        print()
        print(datetime.datetime.now())
        print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print()
        print('                                                          LLYODS_BAKERY                                                              ')
        print()
        print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print('%5s'%"ITEM_NO",'%30s'%'ITEM_NAME','%15s'%'CATEGORY','%25s'%'ORIGINAL_QUANTITY','%15s'%'QUANTITY_SOLD','%20s'%'REMAINING_QUANTITY','%15s'%'COST_PER_ITEM','%15s'%'TOTAL_COST')
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        query3='''update inventory
               set QUANTITY=0 where QUANTITY<0;'''
        mycursor.execute(query3)
        query1='''select * from inventory
                order by ITEM_NO;'''
        mycursor.execute(query1)
        result=mycursor.fetchall()
        query2='''select * from sales
               where DATE_OF_PURCHASE=curdate()
               order by ITEM_NO;'''
        mycursor.execute(query2)
        result2=mycursor.fetchall()
        fcost=[]
        for i in result:
            for j in result2:
                if j[0]==i[0]:
                    if j[3]==0:
                        continue
                    print('%5s'%j[0],'%30s'%j[1],'%15s'%j[2],'%25s'%i[3],'%15s'%j[3],'%20s'%(int(i[3])-int(j[3])),'%15s'%i[5],'%15s'%(int(i[5])*int(j[3])))
                    fcost.append(int(i[5])*int(j[3]))
        c=0
        for x in fcost:
            c+=x
        print('------------------------------------------------------------------------------------------------------------------------------------')
        print("TOTAL_COST:                         ",c,"Rs")
        print('-------------------------------------------------------------------------------------------------------------------------------------')
        query='''select SUM_OF_TOTAL_ from sales
              where DATE_OF_PURCHASE=curdate();'''
        mycursor.execute(query)
        row=mycursor.fetchall()
        mydb.commit()
        for i in row:
            for j in i:
                disco=0
                disco+=float(j)
                break
        print()
        print("TOTAL COST AFTER APPLYING DISCOUNT FOR PARTICULAR USERS:                         ",c-disco,"Rs")
        print()
        query4='''select sum(TOTAL_COST) from sales
               where DATE_OF_PURCHASE=curdate();'''
        mycursor.execute(query4)
        result3=mycursor.fetchall()
        for i in result3:
            z=i[0]
        print()
        print("TOTAL_COST FROM SALES MODULE:",z,"Rs")
        print()
        print('----------------------------------------------------------------------------------------------------------------------------------------------------')
    except:
        print("AN ERROR HAS OCCURED")
        
    
    



        
def sales_menu():
    while True:
        try:
            print('------------------------------------------------------')
            print("1. ADD ITEM")
            print()
            print("2. MODIFY ITEM")
            print()
            print("3. VIEW ORDER LIST")
            print()
            print("4. COME OUT OF SALES MENU")
            print('-----------------------------')
            print()
            ch=int(input("ENTER YOUR CHOICE:"))
            if ch==1:
                s_nuins()
            elif ch==2:
                s_umodifyy()
            elif ch==3:
                s_bill()
            elif ch==4:
                print("EXITING...")
                break
            else:
                print("INVALID CHOICE")
                break
        except:
            print('AN ERROR HAS OCCURED')
        


def sales_menu_admin():
    while True:
        print()
        print('-----------------------------')
        print("1. CREATE ITEMS")
        print()
        print("2. MODIFY ITEMS")
        print()
        print("3. DELETE ITEMS")
        print()
        print("4. REPORT GENERATION")
        print()
        print("5. EXIT")
        print('-----------------------------')
        print()
        ch=int(input("ENTER YOUR CHOICE"))
        if ch==1:
            s_nins()
        elif ch==2:
            s_nmodify()
        elif ch==3:
            s_del()
        elif ch==4:
            i_rept()
            break
        elif ch==5:
            print("EXITING...")
            break
        else:
            print("INAVALID CHOICE")
            break



def inventory_menu():
    while True:
        print()
        print('-----------------------------')
        print("1. ADD ITEMS")
        print()
        print("2. MODIFY ITEMS")
        print()
        print("3. DELETE ITEMS")
        print()
        print("4. SEARCH ITEMS")
        print()
        print("5. EXIT")
        print()
        print('------------------------------')
        ch=int(input("ENTER YOUR CHOICE:"))
        if ch==1:
            i_ins()
        elif ch==2:
            i_modify()
        elif ch==3:
            i_del()
        elif ch==4:
            i_search()
        elif ch==5:
            print("EXITING...")
            break
        else:
            print("INVALID CHOICE")
            break
        
        





u_name=input("Enter username:")
if u_name=='admin_llyodsb':
    for i in range(5):
        passwd=passwordbox("ENTER PASSWORD:")
        if passwd=="llyodsb9801":
            print("WELCOME ADMIN!")
            print("------------------------------------------------")
            try:
                while True:
                    print()
                    print("1. INVENTORY")
                    print()
                    print("2. SALES")
                    print()
                    print("3. COME OUT OF THE ENTIRE MENU")
                    print()
                    ans=int(input("WHAT WOULD YOU LIKE TO WORK ON:"))
                    if ans==1:
                        inventory_menu()
                    elif ans==2:
                        sales_menu_admin()
                    elif ans==3:
                        break
                    else:
                        print("INVALID CHOICE")
                        break
            except:
                print("AN ERROR HAS OCCURED")
                break
            break
            
        else:
            print("WRONG PASSWORD. TRY AGAIN. YOU HAVE",5-i,"CHANCE LEFT")
    else:
        print("WRONG PASSWORD. ACCESS DENIED")
else:
    while True:
        print("----------------------------------------------------")
        print("WELCOME TO LLYODS BAKERY")
        print("----------------------------------------------------")
        query='''select USERNAME from login;'''
        mycursor.execute(query)
        rows=mycursor.fetchall()
        fnd=0
        for i in rows:
            if i==(u_name,):
                    fnd=1
        if fnd==1:
            print('-------------------------------')
            print()
            print("WELCOME USER")
            print()
            print('-------------------------------')
            query2='''select passwd from login where USERNAME='%s';'''%(u_name)
            mycursor.execute(query2)
            row=mycursor.fetchall()
            passwd=passwordbox("ENTER UR PASSWD")
            flag="False"
            for i in row:
                if i==(passwd,):
                    flag="True"
            if flag=="True":
                query1='''update login
                       set VISITS=VISITS+1
                       where USERNAME='%s' and passwd='%s';'''%(u_name,passwd)
                mycursor.execute(query1)
                mydb.commit()
                vis_list=[]
                query2='''select VISITS from login where USERNAME='%s' and passwd='%s';'''%(u_name,passwd)
                mycursor.execute(query2)
                result=mycursor.fetchall()
                mydb.commit()
                for x in result:
                    vis_list.append(x)
                if vis_list[0][0]>10:
                    bonus='bonus_discount'
                    b.append(bonus)
                else:
                    bonus='no_discount'
                    b.append(bonus)            
                print("LOGIN SUCCESSFUL!")
                ans=input("WOULD YOU LIKE TO SEE THE MENU?:(Y/N)")
                if ans=='y' or ans=='Y':
                    query='''select * from inventory;'''
                    mycursor.execute(query)
                    results=mycursor.fetchall()
                    if mycursor.rowcount<=0:
                        print("\\#SORRY! NO MATCHING DETAILS AVAILABLE##")
                    else:
                        print("------------------------------------------------------------------------------------------------------------------------------------")
                        print('%5s'%"ITEM_NO",'%25s'%'ITEM_NAME','%20s'%"ITEM_TYPE",'%12s'%'COST')
                        print("------------------------------------------------------------------------------------------------------------------------------------")
                        for j in results:
                            print('%5s'%j[0],'%30s'%j[1],'%20s'%j[2],'%14s'%j[5])
                        print("------------------------------------------------------------------------------------------------------------------------------------")
                        print()
                        print()
                        print()
                elif ans=='n' or ans=='N':
                    pass
                else:
                    print("INVALID CHOICE")
                    break
                sales_menu()
                break
            else:
                query2='''select passwd from login where USERNAME='%s';'''%(u_name)
                mycursor.execute(query2)
                row=mycursor.fetchall()
                mydb.commit()
                flag="False"
                for j in row:
                    for i in range(5):
                        print("ENTERED WRONG PASSWORD. PLS RE-ENTER. YOU HAVE",5-i,"CHANCES LEFT")
                        new_psw=passwordbox("ENTER UR PASSWD")
                        if j==(new_psw,):
                            flag="True"
                            break
                    else:
                        print("YOUR CHANCES ARE OVER")
                if flag=="True":
                    query1='''update login
                           set VISITS=VISITS+1
                           where USERNAME='%s' and passwd='%s';'''%(u_name,new_psw)
                    mycursor.execute(query1)
                    mydb.commit()
                    vis_list=[]
                    query2='''select VISITS from login where USERNAME='%s' and passwd='%s';'''%(u_name,new_psw)
                    mycursor.execute(query2)
                    result=mycursor.fetchall()
                    mydb.commit()
                    for x in result:
                        vis_list.append(x)
                    if vis_list[0][0]>10:
                        bonus='bonus_discount'#applying discount if the user has visited more than 10 times
                        b.append(bonus)
                    else:
                        bonus='no_discount'
                        b.append(bonus)  
                    print("LOGIN SUCCESSFUL!")
                    ans=input("WOULD YOU LIKE TO SEE THE MENU?:(Y/N)")
                    if ans=='y' or ans=='Y':
                        query='''select * from inventory;'''
                        mycursor.execute(query)
                        results=mycursor.fetchall()
                        if mycursor.rowcount<=0:
                                print("\\#SORRY! NO MATCHING DETAILS AVAILABLE##")
                        else:
                            print("------------------------------------------------------------------------------------------------------------------------------------")
                            print('%5s'%"ITEM_NO",'%25s'%'ITEM_NAME','%20s'%"ITEM_TYPE",'%12s'%'COST')
                            print("------------------------------------------------------------------------------------------------------------------------------------")
                            for j in results:
                                print('%5s'%j[0],'%30s'%j[1],'%20s'%j[2],'%14s'%j[5])
                            print("------------------------------------------------------------------------------------------------------------------------------------")
                            print()
                            print()
                            print()
                    elif ans=='n' or ans=='N':
                        pass
                    else:
                        print("INVALID CHOICE")
                        break
                    sales_menu()
                    break
        else:
            u_name,passwd=passwd_creation()
            vis_list=[]
            query2='''select VISITS from login where USERNAME='%s' and passwd='%s';'''%(u_name,passwd)
            mycursor.execute(query2)
            result=mycursor.fetchall()
            mydb.commit()
            for x in result:
                vis_list.append(x)
            if vis_list[0][0]>10:
                bonus='bonus_discount'
                b.append(bonus)
            else:
                bonus='no_discount'
                b.append(bonus)            
            ans=input("WOULD YOU LIKE TO SEE THE MENU?:(Y/N)")
            if ans=='y' or ans=='Y':
                query='''select * from inventory;'''
                mycursor.execute(query)
                results=mycursor.fetchall()
                if mycursor.rowcount<=0:
                    print("\\#SORRY! NO MATCHING DETAILS AVAILABLE##")
                else:
                    print("------------------------------------------------------------------------------------------------------------------------------------")
                    print('%5s'%"ITEM_NO",'%25s'%'ITEM_NAME','%20s'%"ITEM_TYPE",'%12s'%'COST')
                    print("------------------------------------------------------------------------------------------------------------------------------------")
                    for j in results:
                        print('%5s'%j[0],'%30s'%j[1],'%20s'%j[2],'%14s'%j[5])
                    print("------------------------------------------------------------------------------------------------------------------------------------")
                    print()
                    print()
                    print()
            elif ans=='n' or ans=='N':
                pass
            else:
                print("INVALID CHOICE")
                break
            sales_menu()
            break
            
                    
                    
           
        
        







































