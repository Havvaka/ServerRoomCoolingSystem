import unittest
from design.connection import create_app,db
from design.model.devicemodel import Device

class Test_Device_Model(unittest.TestCase):

    def setUp(self):
        self.app=create_app()
        self.app_context=self.app.app_context()
        self.app_context.push()
        self.client=self.app.test_client()
        db.create_all()

    def test_get__all_device(self):

        device1=Device(deviceid=15,devicename="sevim",devID="defb")
        device2=Device(deviceid=16, devicename="özge",devID="rısc")

        db.session.add_all([device1,device2])
        db.session.commit()
        
        devicees=Device.get_all_device()
        self.assertTrue(devicees)

    def test_get_device_by_id(self):

        device=Device(deviceid=19,devicename="filtre",devID="filtre")
        db.session.add(device)
        
        db.session.commit()

        found_device=Device.get_device_by_id(17)

        self.assertEqual(found_device.deviceid,17)
        self.assertEqual(found_device.devicename,"filter")
        self.assertEqual(found_device.devID,"asdffg")

    def test_gt_dev_by_id(self):
        device=Device(deviceid=18,devicename="filter",devID="sadf")
        db.session.add(device)

        db.session.commit()

        found_dev=Device.get_dev_by_id("sadf")

        self.assertEqual(found_dev.deviceid,18)
        self.assertEqual(found_dev.devicename,"filter")
        self.assertEqual(found_dev.devID,"sadf")

    def test_add_device(self):

        Device.add_device("sevgi","deste")

        last_device=Device.query.order_by(Device.deviceid.desc()).first()

        self.assertEqual(last_device.devicename,"sevgi")
        self.assertEqual(last_device.devID,"deste")

    def test_update_device(self):
        device=Device(deviceid=18,devicename="love",devID="me")
        db.session.add(device)
        db.session.commit()

        Device.update_device(18,"love","me")
        updated_device = Device.query.filter_by(deviceid=18).first()

        self.assertEqual(updated_device.deviceid,18)
        self.assertEqual(updated_device.devicename,"love")
        self.assertEqual(updated_device.devID,"me")
    

    def test_delete_device(self):
        device=Device(deviceid=21,devicename="deniz",devID="yelken")

        db.session.add(device)
        db.session.commit()

        Device.delete_device(21)

        deletedevice=Device.query.filter_by(deviceid=21).first()

        self.assertIsNone(deletedevice)


    def test_get_devicename(self):

        device=Device(deviceid=20,devicename="sevim",devID="delibudak")
        
        db.session.add(device)
        db.session.commit()

        Device.device_name("sevim")

        get_devicename=Device.query.filter_by(deviceid=20).first()

        self.assertEqual(get_devicename.deviceid,20)
        self.assertEqual(get_devicename.devicename,"sevim")
        self.assertEqual(get_devicename.devID,"delibudak")





        



