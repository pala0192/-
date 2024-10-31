#!C:\Python38\python.exe
import cgi, os
form = cgi.FieldStorage()
pageId=form["pageId"].value
description=form["description"].value
if 'image_link' in form:
    image_link=form["image_link"].value
    
else:
    image_link=''

opened_file=open('passed_image/'+pageId,'w',encoding='utf-8')
opened_file.write(image_link)
opened_file.close()

opened_file=open('passed_document/'+pageId,'w',encoding='utf-8')
opened_file.write(description)
opened_file.close()

os.remove('databox/'+pageId)
os.remove('databox_image/'+pageId)
print("Location: test.py")
print()

