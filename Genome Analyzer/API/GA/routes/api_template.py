from flask_restful import Resource
from GA import cors

class Api_template(Resource):
    # Write method which will be executed via GET request
    def get(self):
        return {'success': True, 'message': 'CI/CD deployment through backend branch is successful'}, 200

    # Write method which will be executed via POST request
    def post(self):
        return {'poost': 'post req'}, 200

    # Write method which will be executed via PUT request
    def put(self):
        return {'puut': 'put req'}, 200

     # Write method which will be executed via DELETE request
    def delete(self):
        return {'deel': 'del req'}, 200
    

    
