import mysql.connector as orc
def deleterecord():
    while(True):
        try:
            con=orc.connect(host="localhost",
                            user="root",
                            password="Root@123",
                            database="sakshi")
            cur=con.cursor()
            #get the employee number from KBD
            empno=int(input("\t Enter Employee Number to Delete:"))
            dq="delete from emp where eno=%d"%empno
            cur.execute(dq)
            con.commit()
            if(cur.rowcount>0):
                print("{} Record Deleted".format(cur.rowcount))
            else:
                print("\t Record Does not Exist")
            ch=input("\t Do u want to Delete another Record(yes/no):")
            if(ch.lower()=="no"):
                break
        except orc.DatabaseError as db:
            print("Problem with MySQL:",db)
        except ValueError:
            print("Don't enter alnums,strs and symbols for empno")
