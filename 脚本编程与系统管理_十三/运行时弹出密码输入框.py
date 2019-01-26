import getpass



def svc_login(user,passwd):
    pass


user = getpass.getuser()
passwd = getpass.getpass()

if svc_login(user,passwd):
    print('1')
else:
    print('2')
