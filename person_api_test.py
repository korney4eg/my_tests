from person_api import *
from datetime import date, datetime
import unittest

class TestHelperAPI(unittest.TestCase):
    def test_message_making(self):
        pa =  HelperAPI()
        self.assertEqual(pa.send_resp(200, 'good'), {'message': 'good'})

    def test_error_making(self):
        pa =  HelperAPI()
        self.assertEqual(pa.send_resp(400, 'bad'), {'error': 'bad'})

    def test_days_difference_minus(self):
        pa =  HelperAPI()
        self.assertEqual(pa.difference_in_days(date(2018,2,13),date(2019,3,15)), -30)

    def test_days_difference_plus(self):
        pa =  HelperAPI()
        self.assertEqual(pa.difference_in_days(date(2018,2,13),date(2013,2,12)), 1)

    def test_days_difference_today(self):
        pa =  HelperAPI()
        self.assertEqual(pa.difference_in_days(datetime.today().date()), 0)

    def test_was_message(self):
        pa =  HelperAPI()
        self.assertEqual(pa.generate_birhtday_message(-30), 'Your birthday was 30 days ago')

    def test_will_message(self):
        pa =  HelperAPI()
        self.assertEqual(pa.generate_birhtday_message(1), 'Your birthday is in 1 days')

    def test_happy_birthday_message(self):
        pa =  HelperAPI()
        self.assertEqual(pa.generate_birhtday_message(0), 'Happy Birthday!')

    def test_parse_invalid_json(self):
        pa =  HelperAPI()
        self.assertEqual(pa.parse_json('{"I am ":"Invalid json"'), None)

    def test_parse_valid_json(self):
        pa =  HelperAPI()
        self.assertEqual(pa.parse_json('{"I am":"Valid json"}'), {'I am':'Valid json'})   

    def test_parse_invalid_date(self):
        pa =  HelperAPI()
        self.assertEqual(pa.parse_date('2008-06-56'), None)

    def test_parse_valid_date(self):
        pa =  HelperAPI()
        self.assertEqual(pa.parse_date('2008-06-26'), datetime(2008, 6, 26, 0, 0))