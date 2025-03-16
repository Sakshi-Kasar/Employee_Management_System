from addemp import addemp
from selectall import selectone,selectall
from empupdate import update
from delemp import deleterecord
from search_emp import search
while(True):
    print("*"*50)
    print("\t 1-add emp details. ")
    print("\t 2-select all  ")
    print("\t 3-select one ")
    print("\t 4-update emp ")
    print("\t 5-delete emp")
    print("\t 6-search emp")
    print("\tenter choice::")
    ch=int(input("\t"))
    print("*"*50)
    match(ch):
        case 1:addemp()
        case 2:selectall()
        case 3:selectone()
        case 4:update()
        case 5:deleterecord()
        case 6:search()
        case _:print("\t enter valid..")








