class pwdchk(Exception):
    pass
def checkpwd():
    pwd="vinayak@123"
    upwd=input("Enter password==")
    try:
        if(pwd!=upwd):
            raise pwdchk("WRONG PASSWORD EXCEPTION!")
        print("CORRECT PASSWORD")
    except pwdchk as obj:
        print(obj) 
checkpwd()
