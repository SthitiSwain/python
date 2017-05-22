'''
Created on 21-May-2017

@author: sbig
'''
'''
Created on 20-May-2017

@author: sbig
'''

import sqlite3
import os.path
from os import listdir, getcwd

# 
# def get_picture_list(rel_path):
#     abs_path = os.path.join(os.getcwd(),rel_path)
#     print ('abs_path =', abs_path)
#     dir_files = os.listdir(abs_path)
#     #print dir_files
#     return dir_files
# 
#     
# picture_list = get_picture_list('pic')
# print (picture_list)


def create_or_open_db(db_file):
    db_is_new = not os.path.exists(db_file)
    conn = sqlite3.connect(db_file)
    if db_is_new:
        print ('Creating schema')
        sql = '''create table if not exists PICTURES(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        PICTURE BLOB,
        FILE_NAME TEXT);'''
        conn.execute(sql) # shortcut for conn.cursor().execute(sql)
    else:
        print ('Schema exists\n')
    return conn


    
def insert_picture(conn, picture_file):
    with open(picture_file, 'rb') as input_file:
        ablob = input_file.read()
        base=os.path.basename(picture_file)
        afile, ext = os.path.splitext(base)
        sql = '''INSERT INTO PICTURES
        (PICTURE, FILE_NAME)
        VALUES(?,?);'''
        conn.execute(sql,[sqlite3.Binary(ablob), afile]) 
        conn.commit()
        
conn = create_or_open_db('pic.db')
conn.execute("DELETE FROM PICTURES")
# for fn in picture_list:
#     picture_file = "./pic/"+fn
insert_picture(conn, picture_file)
conn.commit() 
for r in conn.execute("SELECT FILE_NAME FROM PICTURES"):
    print (r[0])
 
conn.close()
    
