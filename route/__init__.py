from controller import *

# This createResource class is used to add defined resources to end point 
# GO TO /controller TO SEE MORE
class CreateResource:
    def __init__(self,api):
        api.add_resource(BotController, '/<string:message>')
        api.add_resource(BotStarter, '/start')
        api.add_resource(BotDefault, '/')
        api.add_resource(Help, '/help')