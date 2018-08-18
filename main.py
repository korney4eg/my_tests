from person_api import *
from person_registry import * 
from bottle import get, run, request, put,  response,error, abort
from datetime import date

person_registry = PersonRegistry()
helper_api = HelperAPI()
@error(500)
def error_handler_500(error): 
    message = 'Database Error'
    return message

@get('/hello/<name>')
def hello(name):
    response.status = 400
    user_birhday = person_registry.get_birh_date(name)    
    if user_birhday == None:
        return helper_api.send_resp(400, "Couldn't find user: " + name)
    time_delta = helper_api.difference_in_days(user_birhday)
    response.status = 200
    return {'message':'Hello '+ name + '! '+ helper_api.generate_birhtday_message(time_delta)}


@put('/hello/<name>')
def greet(name):
    response.status = 400
    data = request.body.read().decode("utf-8")
    # Checking that user provided proper json
    parsed_data = helper_api.parse_json(data)
    if parsed_data == None:
        return {'error': "Proper json wasn't provided"}
    if 'dateOfBirth' not in parsed_data.keys():
        return {'error':  "dateOfBirth field wasn't provided"}
    parsed_date = helper_api.parse_date(parsed_data['dateOfBirth'])
    if parsed_date == None:
        return send_resp(400, "'YYYY-mm-dd' date format required")       
    person_registry.add_person(name, date(parsed_date.year, parsed_date.month, parsed_date.day))
    response.status = 201
    return ''
        

run(host='0.0.0.0', port=8080, debug=True)
