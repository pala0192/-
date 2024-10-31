#!C:\Python38\python.exe
import cgi, os
form = cgi.FieldStorage()
pageId=form["pageId"].value
title=form["title"].value
description=form["description"].value
    
opened_file=open('update/'+pageId,'w',encoding='utf-8')
opened_file.write('바꾸고 싶은 제목:' + title)
opened_file.write('바꾸고 싶은 내용:' + description)
opened_file.close()

print("Location: index.py")
print()
