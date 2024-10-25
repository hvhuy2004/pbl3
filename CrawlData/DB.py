import pymongo
from venv import logger
from bson import ObjectId
import random
from datetime import datetime

def save_data_into_DB(data):
    try:
        myclient = pymongo.MongoClient("mongodb://localhost:27017/DACS2")
        mydb = myclient["DACS2"]
        mycol = mydb["recruiments"]

        writer_id = ObjectId("663b72898866d1018c15f7c1")
        city_ids = [ObjectId("663302953889603b78d014fe"), ObjectId("663302953889603b78d014f0"), ObjectId("663302953889603b78d01502"), ObjectId("663302953889603b78d014f5"), ObjectId("663302953889603b78d014f2")]
        it_id = ObjectId("663302953889603b78d014d6")
        for i in data:
            random_city = random.choice(city_ids)
            date = datetime.strptime(i[1], "%m/%d/%Y").date()
            mydict = {
            "status": True,
            "img": [i[4]],
            "cv":[],
            "email": "admin@gmail.com",
            "sdt": "1234567",
            "contact": "nhà tuyển dụng",
            "salary": i[2],
            "title": i[0],
            "description": i[3],
            "writer": writer_id,
            "city": random_city,
            "career": it_id,
            "createdAt": date,
            "__v": 0
            }

            mycol.insert_one(mydict)
            
        myclient.close()
    except Exception as e:
        logger.error(f"Error occured while saving data to DB: {e}")

def get_data_from_DB():
    try:
        myclient = pymongo.MongoClient("mongodb://localhost:27017/DACS2")
        
    except Exception as e:
        print(f"Error occurred while retrieving data from database: {e}")
        return []