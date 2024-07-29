import unittest
from design.connection import create_app,db

from api.speed import apiSpeed


class Test_Speed(unittest.TestCase):

    def setUp(self):

        self.app=create_app()
        self.app.register_blueprint(apiSpeed)
        self.app_context=self.app.app_context()
        self.app_context.push()
        self.client=self.app.test_client()
        db.create_all()

    def test_add_speed(self):
        fan_speed_value={"fanspeedvalue":"23"}

        responce=self.client.get("/api/speed/addspeed/7",json=fan_speed_value)

        data=responce.get_json()

        self.assertEqual(responce.status_code,200)
        self.assertEqual(responce.content_type,"application/json")

        self.assertTrue(data["success"])
        self.assertEqual(data["message"],"successfully added")
        
        self.assertEqual(fan_speed_value["fanspeedvalue"],"23")

    def test_update_speed(self):

        fan={"fans":"45"}


        responce=self.client.post("/api/speed/update/7",json=fan)

        data =responce.get_json()
        self.assertEqual(responce.status_code,200)
        self.assertEqual(responce.content_type,"application/json")
        self.assertTrue(data["success"])
        self.assertEqual(data["message"],"the specified temperature value has been successfully updated")


    def test_get_speed(self):

        responce=self.client.post("/api/speed/7")

        data =responce.get_json()
        self.assertEqual(responce.status_code,200)
        self.assertEqual(responce.content_type,"application/json")
        self.assertTrue(data["success"])
    


    def test_delete_speed(self):

        responce=self.client.post("/api/speed/delete/7")

        data =responce.get_json()

        self.assertEqual(responce.status_code,200)
        self.assertEqual(responce.content_type,"application/json")
        self.assertTrue(data["success"])


   

