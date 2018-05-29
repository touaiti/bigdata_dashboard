from flask import Flask, request
from flask_restful import Resource, Api
import re
from pymongo import MongoClient
from bson.json_util import dumps

app = Flask(__name__)
api = Api(app)

client = MongoClient('mongodb://user:user@ds137650.mlab.com:37650/bigdata')
db = client.bigdata
class Objects(Resource):
    def get(self):
        data = []
        From = None
        To = None
        if request.args : 
            From = request.args['fromDate']+' '+request.args['fromTime']
            To = request.args['toDate']+' '+request.args['toTime']
            print(From)
            print(To)
        if From == None and To == None :
            collection = db.detections.find()
        else:
            collection = db.detections.find({'time' : {'$lt': To, '$gte': From}})
        return dumps(collection)

class Percents(Resource):
    def get(self):
        data = []
        From = None
        To = None
        if request.args : 
            From = request.args['fromDate']+' '+request.args['fromTime']
            To = request.args['toDate']+' '+request.args['toTime']
        if From == None and To == None :
            total = db.detections.find().count()
            collection = db.detections.aggregate(
                [
                    {
                        '$group' : {
                            '_id' : '$objecttype' ,
                            'count': { '$sum': 1 },
                            'percent': { '$sum': 1/total }
                        }
                    }
                ]
            )
        else:
            collection = db.detections.find({'time' : {'$lt': To, '$gte': From}})
        return dumps(collection)

class Statistics(Resource):
    def get(self):
        data = []
        From = None
        To = None
        if request.args : 
            From = request.args['date'] + ' 00:00:00'
            To = request.args['date'] + ' 24:00:00'
            print(From)
        if From == None and To == None :
            total = db.detections.find().count()
            collection = db.detections.aggregate(
                [
                    {
                        '$group' : {
                            '_id' : {"$substr" : ['$time',11,2]} ,
                            'count': { '$sum': 1 },
                            'percent': { '$sum': 1/total }
                        }
                    }
                ]
            )
        else:
            total = db.detections.find({'time' : {'$lt': To, '$gte': From}}).count()
            collection = db.detections.aggregate(
                [
                    {
                        '$match': {
                            'time': {
                                '$gte':  From ,
                                '$lte':  To  
                            }
                        }
                    },
                    {
                        '$group' : {
                            '_id' : {"$substr" : ['$time',11,2]} ,
                            'count': { '$sum': 1 },
                            'percent': { '$sum': 1 }
                        }
                    }
                ]
            )
        return dumps(collection)

#Rest Api Configuration
api.add_resource(Objects, '/objects') # Route_1
api.add_resource(Percents, '/objects/percents') # Route_2
api.add_resource(Statistics, '/objects/statistics') # Route_3

if __name__ == '__main__':
     app.run(port='5000')

