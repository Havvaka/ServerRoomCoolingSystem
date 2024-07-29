
from dataclasses import dataclass
from design.connection import db
from sqlalchemy import ForeignKey,Integer,Column
from sqlalchemy.orm import relationship
from datetime import datetime

"""
Bu sınıf,cihaz ile yapılan işlemleri temsil eder.
"""

@dataclass

class Device(db.Model):
    __tablename__="Device"
    deviceid=db.Column(db.Integer,primary_key=True)
    devicename=db.Column(db.String(180))
    devID= db.Column(db.String(180),nullable=False,unique=True)
   
    def __init__(self,deviceid,devicename,devID):
       self.deviceid=deviceid
       self.devicename=devicename
       self.devID=devID

    @classmethod
    def get_all_device(cls):
        """
        Veritabanına kayırt edilen tüm cihaz verilerini listeler
        :return:Kayıtlı tüm cihaz verilerini döndürür.
        
        """
        return cls.query.all()


    @classmethod
    def get_device_by_id(cls,deviceid):
        """
        İlgili cihaza ait tüm verileri getirir.
        :param deviceid:İlişkili cihazı bulmak için filtreleme işleminde kullanılır.
        :return:Cihazın filtreleme işlemini yapar ve verileri getirir,gösterir.

        """     
        return cls.query.filter_by(deviceid=deviceid).first()
    
    @classmethod 
    def get_dev_by_id(cls,devID):
        """
        Kullanıcıdan alınan veritabanında kayıtlı olan devID' ye ait cihaz verilerini getirir.
        :param devID:İlgili cihaz verilerini filtreme işleminde kullanılacak cihaz id'si.
        :return:Filtreleme işlemi yapılır ve veriler listelenir.   
        """
        return cls.query.filter_by(devID=devID).first()

    @classmethod
    def add_device(cls,devicename,devID):
        """
        Yeni eklenen cihazının kaydının yapılmasını sağlar.
        :param devicename:Veritabanına kaydı yapılan cihazadı verisini temsil eder.
        :param devID:Veritabanına kaydı yapılan cihaz id si verisini temsil eder.
       
        """
        device=cls(None,devicename,devID)
    
        db.session.add(device)
        db.session.commit()


    @classmethod
    def update_device(cls,deviceid,devicename,devID):
        """
        Seçilen veritabanına kayıtlı cihaz verilerinin güncellenmesini sağlar.
        :param deviceid:Güncellenecek cihazın veritabanına kayıtlı kimliğini temsil eder.
        :param devicename:İlişkili cihazın güncellenecek cihaz adını temsil eder.
        :param devID:Güncellenecek cihazın cihaz id sini temsil eder.
        
        """

        device=cls.query.filter_by(deviceid=deviceid).first()
        device.devicename=devicename
        device.devID=devID
        db.session.commit()

    @classmethod

    def delete_device(cls,deviceid):
        """
        Seçili cihaz verilerinin silme işlemi yapılır.
        :param deviceid:Filtreleme işleminde ulanılan cihaz id'si,ilgili cihazı bulup siler.        
        """
        device=cls.query.filter_by(deviceid=deviceid).first()

        db.session.delete(device)
        db.session.commit()

    @classmethod
    def device_name(cls,devicename):
       """
       Cihaz adına göre filtreleme işlemi yapılır.
       :param devicename:Filtreleme işlemini yapan cihaz adı değeri.
       :return:Filtrelenen cihaz adına göre veriler gönderilir.
       
       
       """
       return  cls.query.filter_by (devicename=devicename).first()
    
    
    @classmethod
    def get_device_by_DevID(cls,devID):
        try:
            """
            Kullanıcının belirlediği cihaz id'sine göre filtreleme işlemi yapılır.
            :param devID:Cihazid sine göre filtreleme işlemlerinde kullanılır.
            :return:Filtrelenen cihaz id'sine göre verileri gönderir.    
            """
         
            return cls.query.filter_by(devID=devID).first()
        except Exception as e:
            print(e)



