from flask import Flask, request
from flask_restful import Resource, Api
import re

app = Flask(__name__)
api = Api(app)




class _RegExLib:
    """Set up regular expressions"""
    _reg_defaultdict = re.compile(r'defaultdict(.*)\n')
    __slots__ = ['defaultdict']

    def __init__(self, line):
        self.defaultdict = self._reg_defaultdict.match(line)


#Routers
class Objects(Resource):
    def get(self):
        data = []
        From = None
        To = None
        if request.args : 
            From = request.args['From']
            To = request.args['To']
        with open('f', 'r') as file:
            line = next(file)
            while line:
                reg_match = _RegExLib(line)
                if reg_match.defaultdict:
                    d = reg_match.defaultdict.group(1).strip('()').split('<class \'list\'>, ')[1].strip('{}')
                    objectId = d.split(': [\'')[0]
                    d = d.split(': [\'')[1].strip('\']').split(',')
                    objectType = d[0].split(':')[0]
                    objectAccurency = d[0].split(':')[1]
                    objectTime = d[1].split(' : ')[1]
                    if From == None and To == None :
                        dict_of_data = {
                                'ID': objectId,
                                'Type': objectType,
                                'Accurency': objectAccurency,
                                'Time': objectTime
                        }
                        data.append(dict_of_data)
                    elif objectTime >= From and objectTime <= To:
                        dict_of_data = {
                                'ID': objectId,
                                'Type': objectType,
                                'Accurency': objectAccurency,
                                'Time': objectTime
                        }
                        data.append(dict_of_data)               
                line = next(file, None)
        return data 




#Rest Api Configuration
api.add_resource(Objects, '/objects') # Route_1


if __name__ == '__main__':
     app.run(port='5000')