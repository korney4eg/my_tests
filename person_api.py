from datetime import date, datetime
import json


class HelperAPI():
    def send_resp(self, status_code, message):
        if status_code > 201:
            message_type = 'error'
        else:
            message_type = 'message'
        return {message_type: message}

    def difference_in_days(self, date1, date2 = datetime.today()):
        parsed_date = self.parse_date(date1)

        if parsed_date == None:
            return None
        this_year_birth = datetime(date2.year,parsed_date.month,parsed_date.day,0,0)
        return (this_year_birth - date2).days
    
    def generate_birhtday_message(self, time_delta):
        if time_delta > 0:
            birhtday_message = 'Your birthday is in '+ str(time_delta) +' days'
        elif time_delta < 0:
            birhtday_message = 'Your birthday was '+ str(-time_delta) +' days ago'
        else:
            birhtday_message = 'Happy Birthday!'
        return birhtday_message

    def parse_json(self, json_data):
        try:
            return json.loads(json_data)
        except json.decoder.JSONDecodeError:
            return None

    def parse_date(self, requested_date):
        if type(requested_date) == date:
            return requested_date
        try:
            return datetime.strptime(requested_date,'%Y-%m-%d')
        except ValueError:
            return None
         
