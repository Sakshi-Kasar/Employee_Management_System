import mysql.connector as mc
def search():
    try:

        con=mc.connect(host="localhost",user="root",password="Root@123",database='sakshi')
        print("\t enter eno for search..")
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
