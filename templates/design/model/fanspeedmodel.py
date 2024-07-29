
from design.connection import db,create_app
from sqlalchemy import ForeignKey, Integer, Table,Column
from sqlalchemy.orm import relationship, declarative_base
from dataclasses import dataclass
from design.model.devicemodel import Device

"""
Bu sını,Kullanıcıdan alınan belirlediği cihaz sıcaklık değerini alır.
"""
Base = declarative_base()
@dataclass
class FAN_SPEED(db.Model):
    __tablename__="Fanspeed"
    fanspeedid=db.Column(db.Integer,primary_key=True)
    deviceid=db.Column(db.Integer,ForeignKey("Device.deviceid"))
    fan_speed_value=db.Column(db.String(180),nullable=False)
    device = relationship("Device", backref="fan_speeds")


    def __init__(self,fanspeedid,deviceid,fan_speed_value):
        self.fanspeedid=fanspeedid
        self.deviceid=deviceid
        self.fan_speed_value=fan_speed_value
    

    @classmethod
    def add_speed(cls,deviceid,fan_speed_value):
        """
        Kullanıcıdan alınan istediği fan hızı değerlerini veritabanına kaydetme işlemi yapar.
        :param devicedi: Hangi cihaza ait olduğu bilgisini içerir.
        :param fan_speed_value: Sabit olarak cihazın kalmasını istediği sıcaklık verisini içerir.

        """
        speed=cls(None,deviceid,fan_speed_value)
        db.session.add(speed)
        db.session.commit()

    @classmethod
    def get_all_speed_by_id(cls,deviceid):

        """
        Veritabanında kayıtlı ilgili cihazaait tüm fan hızı verilerini getirir.
        :param deviceid: Hangi cihaz olduğunun bilgisini içerir.
        :return: Filtrelenen cihaza ait fan hızı verilerini gönderir.
        
        """
        try:
            return cls.query.filter_by(deviceid=deviceid).first()
        except Exception as e:
            print (e)

    @classmethod
    def get_all_speed(cls):
            """
            Veritabanına kayıtlı tüm fan hızı verilerini getirir.
            :return: Tüm fan hızı verilerini içerir.
            """
            try:
            
                return cls.query.all()
            except Exception as e:
                 print ("er:",e)
    
    @classmethod
    def delete_speed(cls,deviceid):
        """
        İlgili cihaza ait verileri silme işlemi yapar.
        :param deviceid: hangi cihaz olduğu bilgisini içerir.

        
        """
        speed=cls.query.filter_by(deviceid=deviceid).first()

        db.session.delete(speed)
        db.session.commit()

    @classmethod
    def update_speed(cls,deviceid,fan_speed_value):
        """
        ilgili cihaza ait fan hızı verileri güncelleme işlemini yapar.
        :param speed: Filtrelenen cihaz verilerini içerir.
        
        """
        speed=cls.query.filter_by(deviceid=deviceid).first()
        speed.fan_speed_value=fan_speed_value
        
        db.session.commit()



