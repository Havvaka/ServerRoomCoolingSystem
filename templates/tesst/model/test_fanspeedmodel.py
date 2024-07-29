import unittest

from design.connection import create_app,db
from design.model.fanspeedmodel import FAN_SPEED
from design.model.devicemodel import Device


class Test_Fanspeedmodel(unittest.TestCase):

    def setUp(self):
        self.app=create_app()
        self.app_context=self.app.app_context()
        self.app_context.push()

        self.client=self.app.test_client()
        db.create_all()


    # def tearDown(self):
    #     db.session.remove()
    #     db.drop_all()
    #     self.app_context.pop()

 

    def test_add_speed(self):
        fan_speed_value="32"
        # d1=Device(deviceid=18,devicename="devicename",devID="deviced")
        # d2= Device(deviceid=21,devicename="sevgi",devID="sağlam")
        # db.session.add_all([d1,d2])
        # db.session.commit()

        FAN_SPEED.add_speed(18,fan_speed_value)
        speed=FAN_SPEED.query.filter_by(deviceid=18).first()
        self.assertEqual(speed.deviceid,18)
        self.assertEqual(speed.fan_speed_value,"32")

    def test_get_speed_by_id(self):
        d1=Device(deviceid=18,devicename="devicename",devID="deviced")
        d2= Device(deviceid=21,devicename="sevgi",devID="sağlam")
        db.session.add_all([d1,d2])
        db.session.commit()
        FAN_SPEED.add_speed(18,"23")

        deger= FAN_SPEED.get_all_speed_by_id(18)

        self.assertTrue(deger)

    def test_cet_all_speed(self):

        # d1=Device(deviceid=18,devicename="devicename",devID="deviced")
        # d2= Device(deviceid=21,devicename="sevgi",devID="sağlam")
        # db.session.add_all([d1,d2])
        # db.session.commit()


        FAN_SPEED.add_speed(18,"21")
        FAN_SPEED.add_speed(21,"15")

        speed1=FAN_SPEED.get_all_speed()
        
        self.assertTrue(speed1)

    def test_delete_fan_speed(self):
        # d1=Device(deviceid=18,devicename="devicename",devID="deviced")
        # d2= Device(deviceid=21,devicename="sevgi",devID="sağlam")
        # db.session.add_all([d1,d2])
        # db.session.commit()
       # FAN_SPEED.add_speed(18,"23")


        FAN_SPEED.delete_speed(18)

        speed3=FAN_SPEED.query.filter_by(deviceid=18).first()

        self.assertIsNone(speed3)

    def test_update_fan_speed(self):
        try:
            d1=Device(deviceid=18,devicename="devicename",devID="deviced")
            d2= Device(deviceid=21,devicename="sevgi",devID="sağlam")
            db.session.add_all([d1,d2])
            db.session.commit()
            FAN_SPEED.add_speed(21,"18")
        
            FAN_SPEED.update_speed(21,"15")
            

            speed4=FAN_SPEED.query.filter_by(deviceid=21).first()
            self.assertEqual(speed4.deviceid,21)
            self.assertEqual(speed4.fan_speed_value,"15")

        except Exception as e :
           print(e)















