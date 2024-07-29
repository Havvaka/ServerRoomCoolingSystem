
from design.connection import db
from sqlalchemy import ForeignKey,Integer,Column
from datetime import datetime
from dataclasses import dataclass
"""
Bu sınıf ,MQTT'den alınan nem değerlerini saklamak ve veriler üzerine gerekli işlemler
yapmak için tabloyu temsil eder.

"""
@dataclass
class Humudity(db.Model):
    __tablename__="Humudity"
    humudityid=db.Column(db.Integer,primary_key=True)
    deviceid=db.Column(db.Integer,ForeignKey("Device.deviceid"))
    humudity_value=db.Column(db.String(10))
    humudity_time=db.Column(db.DateTime,default=datetime.utcnow)

    def __init__(self,humudityid,deviceid,humudity_value,humudity_time):
        self.deviceid=deviceid
        self.humudityid=humudityid
        self.humudity_time=humudity_time
        self.humudity_value=humudity_value
        
    @classmethod
    def add_humu(cls,deviceid,humudity_value,humudity_time):
        """
        Nem değerlerini veritabanına ekler.
        :param humudity_value:Eklenmek istenen nem değeri.
        :param humudity_time:Nem verisinin kaydedildiği zaman.
        """

        hum=cls(None,deviceid,humudity_value,humudity_time)
        db.session.add(hum)
        db.session.commit()

    @classmethod
    def get_all_humu(cls):
        """
        Kaydedilen tüm nem verilerini getirir.
        :return :tüm verilerin kayıtlarının listesi.

        """
        return cls.query.all()
  
    @classmethod
    def get_all_by_id(cls,deviceid):
        """
        Belirli bir cihaz için tüm verileri getirir.
        :param deviceid:Filtreleme yapamak için cihaz id'si.
        :return:Belirtilen cihaz için nem verisisnin listesi.
        """
        return cls.query.filter_by(deviceid=deviceid).all()
    
    @classmethod
    def get_hum_by_humudity_time(cls,humudity_time):
        """
        Kaydedilen zamana göre nem verilerini getirir.
        :param humudity_time:Nem verilerini filtrelemek için kullanılır.
        :return:Filtrelenen zamana ait nem verilerini getirir.
        
        """
        return cls.query.filter_by(humudity_time)
    
    


