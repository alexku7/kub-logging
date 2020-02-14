#!/usr/bin/python


import pymongo
import json
from datetime import datetime, timedelta
import glob
import os
import tempfile
import shutil
import time

mongo_host=os.getenv("MONGO_HOST")
mongo_port=os.getenv("MONGO_PORT")
mongo_db=os.getenv("MONGO_DB")
mongo_coll=os.getenv("MONGO_COLL")
days_to_subtract=7
root_folder="/etc/kub-logs/"

from bson.json_util import dumps
 
 

 
 
def create_mongoDB_conn():
   mongo_client= pymongo.MongoClient("mongodb://" + mongo_host + ":" + mongo_port  +"/")
   db = mongo_client[mongo_db]
   global coll
   coll = db[mongo_coll]
 
 
def extract_logs(cycle,days):
    print ("start select")
    if cycle:
      folder = tempfile.mkdtemp() + "/"
    else:
      folder=root_folder
    target_date = datetime.utcnow() - timedelta(days)
    print (target_date)
                   
    logs= coll.find({"time": {"$gt": target_date }})
    for x in logs:
        my_date=x["time"]
        my_name=x["tailed_path"]
        
        short_date="{:%Y-%m-%d}".format(my_date)
        my_name=short_date + "-" + my_name
        f = open(folder + my_name, "a")
        f.write(x["message"]+"\n")
        f.close()
    print(coll.count())
    print (target_date)  
    files = glob.glob(folder+"*")
    if cycle:
       for f in files:
          shutil.copy(f,root_folder)
          os.remove(f)
     

files = glob.glob(root_folder+"*")
for f in files:
   os.remove(f)


create_mongoDB_conn()
extract_logs(False,days_to_subtract)
 
while True:
    time.sleep(120)
    extract_logs(True,1)
