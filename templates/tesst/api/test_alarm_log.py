import unittest
from api.alarmlog import apialarms_log
#from tesst.test_device import Test_Device
#from tesst.test_alarm_log import Test_Alarm_Log
from design.connection import create_app,db
from api.alarmlog import apialarms_log

class Test_Alarm_Log(unittest.TestCase):  # class Test_Device(unittest.TestCase):
    def setUp(self):
        self.app=create_app()
        self.app.register_blueprint(apialarms_log)

        self.app_context=self.app.app_context()
        self.app_context.push()
        self.client=self.app.test_client()
        db.create_all()


    def test_update_alarm(self):
        data={
            "devthreshtemp":"29"

        }
        response=self.client.put("/api/alarms/log/3",json=data)
        data=response.get_json()


        self.assertEqual(response.status_code,200)
        self.assertEqual(response.content_type,"application/json")
        self.assertTrue(data["success"])

        self.assertEqual(data["message"],"alarm log successfully updateded")

  