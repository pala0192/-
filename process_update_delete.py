#!C:\Python38\python.exe
import cgi, os
form = cgi.FieldStorage()
pageId=form["pageId"].value

os.remove('update/'+pageId)
print("Location: update_check.py")
print()
