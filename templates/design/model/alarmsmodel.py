
from design.connection import db
from sqlalchemy import ForeignKey,Integer,Column
from sqlalchemy.orm import relationship
from dataclasses import dataclass
from sqlalchemy.sql import func

"""
Kullanıcının belirlediği eşik değer cihaz sıcaklığından daha 
yüksek olduğunda bildirim gönderen tabloyu temsil eder.
"""

@dataclass
class Alarms(db.Model):

    __tablename__="alarms"
    alarmid=db.Column(db.Integer,primary_key=True)
    deviceid=db.Column(db.Integer,ForeignKey("Device.deviceid"))
    tempalarm=db.Column(db.String(180))
    humalarm=db.Column(db.String(180))
    alarm_time = db.Column(db.TIMESTAMP, default=func.now())
    alarm_type=db.Column(db.String(200))

    def __init__(self,alarmid,deviceid,humalarm,tempalarm,alarm_type,alarm_time):
        self.alarmid=alarmid
        self.deviceid=deviceid
        self.humalarm=humalarm
        self.tempalarm=tempalarm
        self.alarm_time=alarm_time
        self. alarm_type=alarm_type

    @classmethod

    def add_alarm(cls,deviceid,tempalarm,humalarm,alarm_time,alarm_type):
        """
        Veritabanına yeni alarm ekler.
        :param deviceid:İlişkili cihaza ait cihaz belireleyicisi grevinderdir.
        :param tampalarm:Alarm oluştuğunda eklenecek olan o ana ait sıcaklık değeri.
        :param humalarm:Yeni alarm oluştuğunda eklenecek olan nem değerini temsil eder.
        :param alarm_type:Oluşan alarm tipini temsil eder.
        :param alarm_time:Oluşan alarmın zamanını temsil eder.  
        
        """
        alarm=cls(None,deviceid,tempalarm,humalarm,alarm_type,alarm_time)
        db.session.add(alarm)
        db.session.commit()

    @classmethod
    def all_alarms(cls):
        """
        Veritabanına eklenmiş tüm alarmlar listelenir.
        :return:Tüm alarmları gösterir.
        
        """
        return cls.query.all()






 
        


    
