import os

def getList():
    file= os.listdir('databox')
    listStr = ''
    for item in file:
        listStr = listStr+'<li><a href="test.py?id={it}">{it}</a></li>'.format(it=item)
    return listStr