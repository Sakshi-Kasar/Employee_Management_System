import mysql.connector as mc
def update():
    try:

        con=mc.connect(host="localhost",user="root",password="Root@123",database='sakshi')
        print("\t enter eno for update")
        eno=int(input("\t"))
        print("\tname sal comp to update")
        name=input("\t")
        sal=int(input("\t"))
        comp=input("\t")
        cur=con.cursor()
        qry="update  emp set name='%s' ,sal=%d ,comp='%s' where eno=%d"%(name,sal,comp,eno)
        cur.execute(qry)
        con.commit()
        if(cur.rowcount>0):
            print("update successfuly..")
        else:
            print("not update success. not fonund record try again...")

    except Exception as e:
        print(e)



