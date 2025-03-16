import mysql.connector as mc
def addemp():
    try:
        con=mc.connect(host="localhost",user="root",password="Root@123",database="sakshi")
        while(True):
            print("\t enter eno name salary compname ")
            eno=int(input("\t"))
            ename=input("\t")
            sal=int(input("\t"))
            cmp=input("\t")
            cur=con.cursor()
            qry="insert into emp values(%d,'%s',%d,'%s')"%(eno,ename,sal,cmp)
            cur.execute(qry)
            con.commit()
            print("*"*50)
            print("\t row count={}".format(cur.rowcount))
            print("\t do you want to continue..yes/no")
            ch=input("\t")
            if(ch=='no'):
                break

    except Exception as e:
        print(e)

