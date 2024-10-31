#!C:\Python38\python.exe
import cgi, os
form = cgi.FieldStorage()
pageId=form["pageId"].value
title=form["title"].value
description=form["description"].value

opened_file=open('passed_document/'+title,'w',encoding='utf-8')
opened_file.write(description)
opened_file.close()
os.rename('passed_document/'+pageId, 'passed_document/'+title)
os.remove('update/'+pageId)

print("Location: update_check.py")
print()
