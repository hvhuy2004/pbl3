 myclient = pymongo.MongoClient("mongodb://localhost:27017/DACS2")
    print(myclient)
    mydb = myclient["DACS2"]
    mycol = mydb["careers"]
    myquery = {}
    mydoc = mycol.find(myquery)
    for c in mydoc:
        print(c)