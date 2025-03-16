import mysql.connector as mc
def selectone():
    try:

        con=mc.connect(host="localhost",user="root",password="Root@123",database='sakshi')
        print("\t enter eno for select")
        eno=int(input("\t"))
        cur=con.cursor()
        qry="select * from emp"
        cur.execute(qry)
        for col in cur.description:
            print("\t{}".format(col[0]),end=" ")
        res=cur.fetchall()
        k=0
        for row in res:
            if row[0]==eno:
                print("\t")
                print(row)
                k=1
        if k==0:
            print("\t not found..")

    except Exception as e:
        print(e)

def selectall():
    try:

        con=mc.connect(host="localhost",user="root",password="Root@123",database='sakshi')
        cur=con.cursor()
        qry="select * from emp"
        cur.execute(qry)
        for col in cur.description:
            print("\t{}".format(col[0]),end="")
        res=cur.fetchall()
        for row in res:
            print("\t")
            print(row)
    except Exception as e:
        print(e)




