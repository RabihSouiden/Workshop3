import datetime
import pymongo
from flask import Flask, request, jsonify
from pymongo import mongo_client
import dns
import redis
from MicrochipModel import Microchip

# Flask constructor takes the name of
# current module (__name__) as argument
app = Flask(__name__)

# Get the Redis connection
def get_mongo_conn():
    client = pymongo.MongoClient("localhost")
    return client

def addRedis(microChip, id):
    microChip = Microchip()
    r = get_redis_conn()
    data_old = [x.decode("utf-8") for x in r.lrange(id+':fecha', 0, -1)]
    r.rpush(id+':fecha', microChip.timestamp)
    r.rpush(id+':Location', microChip.geolocation)

def get_redis_conn():
    return redis.Redis(host = "127.0.0.1", port = 6379)

@app.route("/archive/location/<id>")
def consultar_redis(id):
    r = get_redis_conn()
    record = request.json
    record["id"] = id
    data_old = [x.decode("utf-8") for x in r.lrange(id+':fecha', 0, -1)]
    print(data_old)
    return {"result:": data_old}

@app.route("/microchipdata/")
def get_Microchip():
    m = get_mongo_conn()
    db = m["PPYDB"]
    col = db["Microchips"]
    cursor = col.find({})
    microchips = []
    for micro in cursor:
        print(micro)
        microchips.append(micro)
    #addRedis(microchips)
    return { "result": microchips }

@app.route("/microchipdata/<microId>")
def microchipdata(microId):
    m = get_mongo_conn()
    db = m["PPYDB"]
    col = db["Microchips"]
    record = request.json
    print(record)
    record["microId"] = microId
    cursor = col.find({"microchip": microId})[0]
    micro = cursor
    microP = Microchip()
    microP.timestamp = micro['timestamp']
    microP.microchip = micro['microchip']
    microP.pet_name = micro['pet-name']
    microP.owner_name = micro['owner-name']
    microP.species = micro['species']
    microP.geolocation.latitude = micro['geolocation']['latitude']
    microP.geolocation.longitude = micro['geolocation']['longitude']
    microP.vital_signs.temperature = micro['vital-signs']['temperature']
    microP.vital_signs.heart_rate = micro['vital-signs']['heart-rate']
    microP.vital_signs.breathing_frecuency = micro['vital-signs']['breathing-frecuency']
    addRedis(microP, micro['_id'])
    return { "result":  micro}

@app.route("/microchip/<id>/record", methods = ["POST"])
def record(id):
    m = get_mongo_conn()
    db = m["PPYDB"]
    col = db["Microchips"]
    record = request.json
    record["id"] = id
    record["datetime"] = datetime.datetime.now()
    col.insert_one(record)
    return "Record for microchip {id} created successfully".format(busId = id), 201

    
if __name__ == "__main__":
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()