import unittest

from design.connection import create_app,db
from design.model.alarmsmodel import Alarms


class Test_Alarms_Model(unittest.TestCase):
    def setUp(self):
        self.app=create_app()
        self.app_context=self.app.app_context()
        self.app_context.push()

        self.client=self.app.test_client()
        db.create_all()


    def test_addalarms(self):
        deviceid=21
        tempalarm="34"

        humalarm=12
        alarm_time="31-08-2023 16:02:00"
        alarm_type="temp"
        Alarms.add_alarm(deviceid,tempalarm,humalarm,alarm_time,alarm_type)

     




