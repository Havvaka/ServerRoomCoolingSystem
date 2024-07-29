import unittest
from design.connection import create_app,db
from design.model.alarmlogmodel import AlarmLog
from design.model.devicemodel import Device



class Test_Alarmlogmodel(unittest.TestCase):

    def setUp(self):
        self.app=create_app()
        self.app_context=self.app.app_context()
        self.app_context.push()

        self.client=self.app.test_client()
        db.create_all()

    def test_addAlarmlog(self):
        # device=Device(deviceid=21,devicename="denis",devID="çorum")
        # db.session.add(device)
        # db.session.commit()
        
    
        AlarmLog.addalarmslog(18,"34")
        last_alarmlog=AlarmLog.query.filter_by(deviceid=18).first()

        self.assertEqual(last_alarmlog.deviceid,18)
        self.assertEqual(last_alarmlog.devthreshtemp,"34")
    
    def test_get_alarmlog(self):

        AlarmLog.addalarmslog(11,"24")
        AlarmLog.addalarmslog(13,"47")

        alarms=AlarmLog.get_all_alarmlog()
        self.assertTrue(alarms)

    def test_get_alamlog_by_id(self):

        alarm2=AlarmLog.get_alarms_by_id(21)
        self.assertTrue(alarm2)


    def test_update_alarmlog(self):

        AlarmLog.update_alarmlog(11,"23")

        alarmlog=AlarmLog.query.filter_by(deviceid=11).first()
        self.assertEqual(alarmlog.deviceid,11)
        self.assertEqual(alarmlog.devthreshtemp,"23")



    






        




    




