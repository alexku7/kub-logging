#!/usr/bin/python


import pymongo
import json
from datetime import datetime, timedelta
import glob
import os

#print(os.environ['HOME'])
mongo_host="10.152.183.139"
mongo_port="27017"
mongo_db="imubit"
mongo_coll="logs"
days_to_subtract=7
root_folder="/etc/kub-logs/"

from bson.json_util import dumps
 
 

 
 
def create_mongoDB_conn():
   mongo_client= pymongo.MongoClient("mongodb://" + mongo_host + ":" + mongo_port  +"/")
   db = mongo_client[mongo_db]
   global coll
   coll = db[mongo_coll]
 
 
def extract_logs():
    print ("start select")
    
    target_date = datetime.utcnow() - timedelta(days_to_subtract)
    print (target_date)
                   
    logs= coll.find({"time": {"$gt": target_date }})
    for x in logs:
        my_date=x["time"]
        my_name=x["tailed_path"]

        short_date="{:%Y-%m-%d}".format(my_date)
        my_name=short_date + "-" + my_name
        f = open(root_folder + my_name, "a")
        f.write(x["message"])
        f.close()
    print(coll.count())
    print (target_date)  


files = glob.glob(root_folder+"*")
for f in files:
   os.remove(f)


create_mongoDB_conn()
extract_logs()
 
