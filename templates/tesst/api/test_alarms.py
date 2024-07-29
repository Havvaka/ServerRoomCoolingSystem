# import unittest
# from api.alarms import apiAlarms
# from design.connection import create_app,db





# class alarms_test(unittest.TestCase):
#     def setUp(self):
#         self.app=create_app()
#         self.app.register_blueprint(apiAlarms)

#         self.app_context=self.app.app_context()
#         self.app_context.push()

#         self.client=self.app.test_client()
#         db.create_all()

#     def test_alarm(self):

#         responce=self.client.get("/api/alarms/getAlarms")

#         data=responce.get_json()

#         self.assertEqual(responce.status_code,200)
#         self.assertEqual(responce.content_type,"application/json")
#         self.assertTrue(data["success"])

#         self.first_alarm1=data["data"][0]

#         self.assertIn("device",self.first_alarm1)
#         self.assertIn("temperature",self.first_alarm1)
#         self.assertIn("humudity",self.first_alarm1)
#         self.assertIn("alarmtime",self.first_alarm1)

#         self.first_alarm2=data["data2"][0]
        
#         self.assertIn("device",self.first_alarm2)
#         self.assertIn("temperature",self.first_alarm2)
#         self.assertIn("humudity",self.first_alarm2)
#         self.assertIn("alarmtime",self.first_alarm2)

       








