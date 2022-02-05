from flask import Flask
from flask_restful import Resource, Api
import os

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    @staticmethod
    def is_prime(num):
        for i in range(2,num//2):
            if num % i ==0:
                return False
        return True
    def get(self):
        primes = [2]
        num = 20
        i = 3
        while num > 0:
            if HelloWorld.is_prime(i):
                primes.append(i)
                num-=1
            i+=1 
        return {'hello': primes}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)