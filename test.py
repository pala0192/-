#!C:\Python38\python.exe

# -*- coding: euc-kr -*-
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
print("content-type:text/html; charset=UTF-8\n")

print()

import cgi, os, view

file= os.listdir('databox')


form = cgi.FieldStorage()

file_list = []
for files in file:
  file_list.append(files)


file_count_num=0
file_num_and_list={}
file_keys_list = []

for file in file_list:
  file_num_and_list[file]=file_count_num
  file_keys_list.append(file)
  file_count_num=file_count_num+1



if  'id' in form:
    pageId = form["id"].value
    description = open('databox/'+pageId, 'r',encoding='utf-8').read()
    description = description.replace("<","&lt;")
    description = description.replace(">","&gt;")

    delete_action='''
      <form action="process_delete.py" method="post">
        <input type="hidden" name="pageId" value="{0}">
        <input type="submit" value="delete" style="width:17%; height:60px; font-size:280%">
      </form>
    '''.format(pageId)
    file_num = file_num_and_list[pageId]
    if pageId==file_keys_list[0]:
      Previous_file_name=''
      next_file_name=file_keys_list[file_num+1]
    elif pageId==file_keys_list[-1]:
      Previous_file_name=file_keys_list[file_num-1]
      next_file_name=''
    else:
      Previous_file_name=file_keys_list[file_num-1]
      next_file_name=file_keys_list[file_num+1]
    if os.path.isfile('databox_image/{}'.format(pageId)) :
      image_link=open('databox_image/{}'.format(pageId), 'r',encoding='utf-8').read()
    else: image_link=''
    transmit_action='''
      <form action="process_transmit.py" method="post">
        <input type="hidden" name="pageId" value="{pageId}">
        <input type="hidden" name="description" value="{description}">
        <input type="hidden" name="image_link" value="{image_link}">
        <input type="submit" value="approval" style="width:17%; height:60px; font-size:280%">
      </form>
    '''.format(pageId,description,image_link)

else : 
    pageId = '현제 문서가 없습니다'
    description = '~ ~ ~'
    delete_action=''
    file_num = 0
    Previous_file_name=''
    next_file_name=file_keys_list[0]
    image_link=''
    transmit_action=''



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
      <h1 style="text-align: center;"><div style="color:rgb(87, 122, 205);font-size:280%">관리자 창</div>
      </h1>
    </div>
    <br>
    <br>
    
    <div style="margin:1%; padding:4%; background-color:  rgb(229, 229, 229);">
      
      <div style="border-bottom:solid 2px; padding:1%;">
        <h2 style="font-size:300%; background-color: yellow; display:inline;">{title}</h2>
      </div>
      
      <p style="font-size:300%">{desc}</p>
      <img src="{img_link}">
      <br>
      <br>
      <br>
      <br>
      
      <a href="index.py?id={Previous_file_name}" style="font-size:150%;background-color: rgb(246, 175, 88);">&lt;&lt;&lt;Previous file</a>
      <a href="index.py?id={next_file_name}" style="font-size:150%;background-color:orange">next file&gt;&gt;&gt;</a>
    </div>
    
    <div style="border:black solid 1px; padding:3%">
      <h3 style="font-size:300%;">contents</h3>
      <ol style="font-size:100%;padding:1%";>{listStr}</ol>
    </div>
    <br>
    
    <div style="padding:1%">
      <h4 style="font-size:200%; margin:0%">edit</h4>
      <br>
      <br>
      
      <h5 style="font-size:200%; margin:0%">delete</h5>
      {delete_action}{transmit_action}
      <br>
    </div>
</body>
</html>
      '''.format(title=pageId, desc= description, listStr=view.getList(), delete_action=delete_action,
      Previous_file_name=Previous_file_name,next_file_name=next_file_name,img_link=image_link,transmit_action=transmit_action))