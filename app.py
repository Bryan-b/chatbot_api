from flask import Flask ,jsonify
from flask_restful import Resource, Api
from route import CreateResource

app = Flask(__name__)
api = Api(app)

# API ENDPOINT RESOURCE INITIALIZED HERE
# GO TO /route DIRECTORY TO SEE MORE
CreateResource(api)

if __name__ == '__main__':
    app.run(debug=True)