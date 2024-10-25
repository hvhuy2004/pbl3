import pymongo
from venv import logger
from bson import ObjectId
import random
from datetime import datetime
import csv

def save_data_into_DB(data):
    try:
        myclient = pymongo.MongoClient("mongodb://localhost:27017/DACS2")
        mydb = myclient["DACS2"]
        mycol = mydb["recruitments"]

        writer_id = ObjectId("663b72898866d1018c15f7c1")
        city_ids = [ObjectId("663302953889603b78d014f0"), ObjectId("663302953889603b78d014f1"), 
                    ObjectId("663302953889603b78d014f2"), ObjectId("663302953889603b78d014f3"), 
                    ObjectId("663302953889603b78d014f4"), ObjectId("663302953889603b78d014f5"), ObjectId("663302953889603b78d014f6"),
                    ObjectId("663302953889603b78d014f7"), ObjectId("663302953889603b78d014f8"), ObjectId("663302953889603b78d014f9"),
                    ObjectId("663302953889603b78d014fa"), ObjectId("663302953889603b78d014fb"), ObjectId("663302953889603b78d014fc"),
                    ObjectId("663302953889603b78d014fd"), ObjectId("663302953889603b78d014fe"),ObjectId("663302953889603b78d014ff"),
                    ObjectId("663302953889603b78d01500"), ObjectId("663302953889603b78d01501"), ObjectId("663302953889603b78d01502")]
        it_id = ObjectId("663302953889603b78d014ec")
        for i in data:
            random_city = random.choice(city_ids)
            date = datetime.strptime(i[2], "%d/%m/%Y")
            new_date = date.replace(day=date.day, month=date.month)
            new_date_mongodb_format = new_date.strftime("%m/%d/%Y")

            mydict = {
            "status": True,
            "img": [i[4]],
            "cv":[],
            "email": "admin@gmail.com",
            "sdt": "1234567",
            "contact": "nhà tuyển dụng",
            "salary": i[1],
            "title": i[0],
            "description": i[3],
            "writer": writer_id,
            "city": random_city,
            "career": it_id,
            "createdAt": new_date_mongodb_format,
            "__v": 0
            }

            mycol.insert_one(mydict)
            
        myclient.close()
    except Exception as e:
        logger.error(f"Error occured while saving data to DB: {e}")

def save():
    # 663302953889603b78d014e4 >> maketing
    # 663302953889603b78d014d6 >> it
    # 663302953889603b78d014dc >> ke toan
    file_path = 'C:\\Users\\ASUS\\OneDrive\\Máy tính\\pbl3_source_code\\ProjectTuyenDung\\QLVLCrawlData\\finance.csv'
    data = []
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            data.append(row)
    return data


if __name__ == '__main__':
    data = save()
    save_data_into_DB(data)
    print(">>> done")
    

    