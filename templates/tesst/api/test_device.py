
# from design.connection import create_app,db
# from api.device import apiDevice
# import unittest
# class Test_Device(unittest.TestCase):
#     def setUp(self):
#         self.app=create_app()
#         self.app.register_blueprint(apiDevice)

#         self.app_context=self.app.app_context()
#         self.app_context.push()
#         self.client=self.app.test_client()
#         db.create_all()    
#     def test_request_example(self):
#         response = self.client.get("/api/device/allDevice")

#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.content_type, "application/json")

#         data = response.get_json()

#         self.assertTrue(data["success"])

#         self.first_device = data["data"][0]
#         self.assertIn("deviceId", self.first_device)
#         self.assertIn("deviceName", self.first_device)
#         self.assertIn("devID", self.first_device)
    
#     def test_get_device_by_id(self):
#         device={
#             "deviceid":4,
#             "deviceName":"selma",
#             "devID":"es"
#         }
#         response=self.client.get("/api/device/4")
#         data=response.get_json()     

#         self.assertEqual(response.status_code,200)
#         self.assertEqual(response.content_type,"application/json")
#         self.assertTrue(data["success"])

#         self.assertEqual(data["data"]["deviceName"],device["deviceName"])
#         self.assertEqual(data["data"]["deviceId"],device["deviceid"])
#         self.assertEqual(data["data"]["devId"],device["devID"])

#     def test_request_addevice(self):
#         data={
#             "deviceName":"mustafa",
#             "deviceId":"rest",
#             "devthreshtemp":"34"
#         }
#         response=self.client.get("/api/device/addDevice",json=data)


#         self.assertEqual(response.status_code,200)
#         self.assertEqual(response.content_type,"application/json")
#         self.assertTrue(["success"])


#         self.assertEqual(data["deviceName"],"mustafa")
#         self.assertEqual(data["deviceId"],"rest")
#         self.assertEqual(data["devthreshtemp"],"34")




#     def test_device_update(self):
#         device={
#             "deviceId":3,
#             "deviceName":"beyza",
#             "deviceId":"432"
#         }
#         data={
#             "deviceName":"sevda",
#             "deviceId":"26"
#         }
#         response=self.client.put("/api/device/3",json=data)
#         data=response.get_json()
#         self.assertEqual(response.status_code,200)
#         self.assertEqual(response.content_type,"application/json")
#         self.assertTrue(data["success"])
#         self.assertEqual(data["message"],"device updated successfully")



#     def test_device_delete(self):
#         device={
#             "deviceid":5,
#             "deviceName":"elma ",
#             "devID":"esa"
#         }
#         response=self.client.delete("/api/device/5")

#         data=response.get_json()
#         self.assertEqual(response.status_code,200)
#         self.assertEqual(response.content_type,"application/json")
#         self.assertTrue(["success"])
#         self.assertEqual(data["message"],"device deleted successfully")
