import unittest
from unittest import TextTestRunner,TestLoader

#from tesst.api.test_alarms import alarms_test
##from tesst.api.test_speed import Test_Speed
#from tesst.model.test_devicemodel import Test_Device_Model
#from tesst.model.test_alarmlogmodel import Test_Alarmlogmodel
#from api.alarmlog import apialarms_log
#from tesst.test_device import Test_Device
#from tesst.test_alarm_log import Test_Alarm_Log
#from tesst.model.test_fanspeedmodel import Test_Fanspeedmodel
from tesst.mqtt.test_mqtttrial import Test_Mqtt


#from design.connection import create_app,db
#from api.alarmlog import apialarms_log

# class Test_Alarm_Log(unittest.TestCase):  # class Test_Device(unittest.TestCase):
#     def setUp(self):
#         self.app=create_app()
#         self.app.register_blueprint(apialarms_log)

#         self.app_context=self.app.app_context()
#         self.app_context.push()
#         self.client=self.app.test_client()
#         db.create_all()


#     def test_update_alarm(self):
#         veri={
#             "devthreshtemp":"29"

#         }
#         response=self.client.put("api/alarms/log/3",json=veri)
#         data=response.get_json()


#         self.assertEqual(response.status_code,200)
#         self.assertEqual(response.content_type,"application/json")
#         self.assertTrue(data["success"])

#         self.assertEqual(data["message"],"alarm log successfully updateded")




loder=TestLoader()


# #suide=loder.loadTestsFromTestCase(Test_Device)
#suide=loder.loadTestsFromTestCase(Test_Alarm_Log)
#suide2=loder.loadTestsFromTestCase(alarms_test)
#suide3=loder.loadTestsFromTestCase(Test_Speed)
#suide3=loder.loadTestsFromTestCase(Test_Device_Model)

#suide4 =loder.loadTestsFromTestCase(Test_Alarmlogmodel)
#suide5 =loder.loadTestsFromTestCase(Test_Fanspeedmodel)
suide6=loder.loadTestsFromTestCase(Test_Mqtt)


# #devi=loder.loadTestsFromTestCase(Test_Device)
runner=TextTestRunner(verbosity=2)
result=runner.run(suide6)



    # def tearDown(self):
    #     db.session.remove()
    #     db.drop_all()
    #     self.app_context.pop()

      
if __name__ == '__main__':
    unittest.main()
