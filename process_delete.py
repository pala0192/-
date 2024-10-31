#!C:\Python38\python.exe
import cgi, os
form = cgi.FieldStorage()
pageId=form["pageId"].value

os.remove('databox/'+pageId)
os.remove('databox_image/'+pageId)
print("Location: index.py")
print()
