#!C:\Python38\python.exe

# -*- coding: euc-kr -*-
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
print("content-type:text/html; charset=UTF-8\n")

print()

import cgi, os

file= os.listdir('message')
listStr = ''
for item in file:
    listStr = listStr+'<li><a href="message.py?id={it}">{it}</a></li>'.format(it=item)

form = cgi.FieldStorage()

if  'num_name' in form:
    num_name = form["num_name"].value
    message = open('message/'+num_name, 'r',encoding='utf-8').read()
    message = message.replace("<","&lt;")
    message = message.replace(">","&gt;")

    delete_action='''
      <form action="process_message_check.py" method="post">
        <input type="hidden" name="num_name" value="{0}">
        <input type="submit" value="delete" style="width:17%; height:60px; font-size:280%">
      </form>
    '''.format(num_name)
else : 
    num_name = '현제 고객 메시지가 없습니다'
    message = '~ ~ ~'
    delete_action=''

print('''<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hanmin wiki making practice</title>
  <link rel="stylesheet" href="front.css">
</head>

<body>
    <div style="margin:12%; background-color: rgb(186, 210, 218);">
      <h1 style="text-align: center;"><div style="color:rgb(87, 122, 205);font-size:280%">고객의 소리 관리창</div>
      </h1>
    </div>
    <br>
    <br>
    
    <div style="margin:1%; padding:4%; background-color:  rgb(229, 229, 229);">
      
      <div style="border-bottom:solid 2px; padding:1%;">
        <h2 style="font-size:300%; background-color: yellow; display:inline;">{num_name}</h2>
      </div>
      
      <p style="font-size:300%">{message}</p>
      
    </div>
    
    
    <div style="border:black solid 1px; padding:3%">
      <h3 style="font-size:300%;">고객의 소리</h3>
      <ol style="font-size:100%;padding:1%";>{listStr}</ol>
    </div>
    <br>
</body>
</html>
      '''.format(num_name=num_name, message= message, listStr=listStr, delete_action=delete_action))

