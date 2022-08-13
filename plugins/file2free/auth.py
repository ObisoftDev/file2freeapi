import os
def auth(username):
    list = []
    try:
        path = os.getcwd() +'/plugins/file2free/auth.txt'
        fo = open(path)
        list = str(fo.read()).split('\n')
        fo.close()
    except Exception as ex:pass
    return username in list