from dataclasses import dataclass
from design.connection import db
from sqlalchemy import ForeignKey,Integer,Column
from flask import json

"""
Bu sınıf ,kullanıcının girdiği eşik sıcaklık değerlerini içerir

"""
@dataclass
class AlarmLog(db.Model):
    __tablename__="alarmlog"
    alarmlogid=db.Column(db.Integer,primary_key=True)
    deviceid=db.Column(db.Integer,ForeignKey("Device.deviceid"))
    devthreshtemp=db.Column(db.String(180))
    
    def __init__(self,alarmlogid,deviceid,devthreshtemp):
        self.alarmlogid=alarmlogid
        self.deviceid=deviceid
        self.devthreshtemp=devthreshtemp
    
    @classmethod
    def get_all_alarmlog(cls):
        """
        Kullanıcadan alınan tüm eşik sıcaklık değer verilerini gösterir.
        :return:Alınan sıcaklık verilerini döndürür.
        
        """
        return cls.query.all()
      
    @classmethod
    def get_alarms_by_id(cls,deviceid):
        """
        İlgili cihaza ait eşik alarm değerini getirir.
        :param deviceid:İlişkili cihaz için filtrelemeişleminde kullanılan parametre.
        :return:ilgili cihaza it filtreleme işlemi yapılır ve veriler gösterilir
        
        """
        return cls.query.filter_by(deviceid=deviceid).first()
    
    @classmethod
    def addalarmslog(cls,deviceid,devthreshtemp):
        """
        Kullanıcıdan alınan eşik alarm değerini veritabanına kaydeder.
        :param deviceid:HanGİ cihaz verisi olduğunu belirtir.
        :param devthreshtemp:Kullanıcıdan alınan eşik alarm sıcaklık değerini belirtir.
        
        """
        alarm=cls(None,deviceid,devthreshtemp)
        db.session.add(alarm)
        db.session.commit()

    @classmethod
    def update_alarmlog(cls,deviceid,devthreshtemp):
        """
        Kaydedilen eşik değini günceller.
        :param deviceid:İlgili cihaza ait fitreleme işleminde kullanılır.
        :param alarmlog:İlgili cihaza ait alarmlog değerleri.
        :param devthreshtemp:eşik değerini belirten parametre.
        
        """
        alarmlog=cls.query.filter_by(deviceid=deviceid).first()
        alarmlog.devthreshtemp=devthreshtemp 
    
        db.session.commit()




    













