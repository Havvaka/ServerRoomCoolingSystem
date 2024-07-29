
from design.connection import db,create_app
from sqlalchemy import ForeignKey,Integer,Column
from datetime import datetime
from datetime import datetime,timedelta
from dataclasses import dataclass

"""
Bu sınıf,MQTT 'den alınan sıcaklık değerleriyle ilgili işlemlerin yapılacaklarını temsil eder.

"""
@dataclass
class Temperature(db.Model):
    __tablename__="Temperature"
    temperatureid=db.Column(db.Integer,primary_key=True)
    deviceid=db.Column(db.Integer,ForeignKey("Device.deviceid"))
    temperaturevalue= db.Column(db.String(10))
    measurement_time=db.Column(db.DateTime,default=datetime.utcnow)
    
    def __init__(self,temperatureid,deviceid,temperaturevalue,measurement_time):
        self.deviceid=deviceid
        self.temperatureid=temperatureid
        self.temperaturevalue=temperaturevalue
        self.measurement_time=measurement_time

    @classmethod
    def add_temp(cls,deviceid,temperaturevalue,measurement_time):
        """ 
        Sıcaklık değerlerini veritabanına ekler.
        :param deviceid: Eklenecek sıcaklığın ait olduğu id değeri.
        :param temperaturevalue: Veritabanına eklenecek sıcaklık değeri.
        :param measurement_time: Sıcaklık değerinin eklenme zamanı temsil eder.
        """
        temp=cls(None,deviceid,temperaturevalue=temperaturevalue,measurement_time=measurement_time)
        db.session.add(temp)
        db.session.commit()

    @classmethod
    def get_all_temp(cls):
        """
        Veritabanına kaydedilmiş tüm sıcaklık değerlerini getirir
        :return:Kaydedilmiş tüm sıcaklık verileri listesi.

        """
        return cls.query.all()
 
    @classmethod
    def get_all_temp_dev_id(cls,deviceid):
        """
        İlgili cihaza ait tüm sıcaklık verilerini getirir.
        :param deviceid:Cihaza ait filtreleme işlemi için kullanılır.
        :return: İlişkili cihaza ait tüm sıcaklık verilerinin listesi.
        
        """
            
        return cls.query.filter_by(deviceid=deviceid).all() 

    @classmethod
    def get_temp_by_measurement_time(cls,measurement_time):
        """
        Kaydedilen zamana göre sıcaklık verilerini gösterir.
        :param measurement_time: Filtreleme yapılacak ölçüm zamanı.
        :return:Filtrelenen ölçüm zamanına ait verileri listeler.
        """
        return cls.query.filter_by(measurement_time)
    
    @classmethod
    def last_temp_value(cls):
        try:
           with create_app().app_context():
                """
                Create app fonsiyonu  çağırılarak gerekli uygulama bağlamı yapılır.
                En son ölçüm yapılan sıcaklık  değeri elde edilir.
                :param last_temp:En son ölçülen sıcaklık değerlini temsil eder.
                :return:En son ölçüm yapılan sıcaklık verisinin sıcaklık değeri gösterilir

                """
                last_temp = cls.query.order_by(cls.temperatureid.desc()).first()
                return last_temp.temperaturevalue if last_temp else None
        except Exception as e:
            print("error",e)

    @classmethod
    def get_tem_by_mea(cls,deviceid):
        try:
           """
           İlişkili cihazın bir gün önceki tüm ölçüm verileri gösterilir.
           :param today:Şu anki zamanı temsil eder.
           :param yesterday:Şu anki zaman ve dünün filtreleme işlemi için kullanılır.
           :param temp:deviceid ile filtreleme yapılarak belirtilen tarihker arasındaki tüm sıcaklık verilerini getiri.
           """
           today=datetime.utcnow().date()
           yesterday=today-timedelta(days=1)
           temp=cls.query.filter(cls.deviceid==deviceid,cls.measurement_time.between(yesterday,today).all())
           return temp
        except Exception as e: 
            print("error",e)  
    
                              


    
  
    
