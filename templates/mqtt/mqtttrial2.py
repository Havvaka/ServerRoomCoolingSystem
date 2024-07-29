
from design.connection import mqtt
from api.temperature import addtemp
from api.humudity import add_hum
from flask import json,Blueprint ,jsonify,current_app
from design.connection import create_app
from datetime import datetime
from design.model.devicemodel import Device
from design.model.fanspeedmodel import FAN_SPEED
from api.alarms import add_alarms
import threading

@mqtt.on_connect()
def on_connect(client, userdata, flags, rc):
    """
    MQTT'ye bağlanma işlemi gerçekleşir ,gerekli kanallara abone olunur.
    """
    print("Bağlandı: " + str(rc))
    client.subscribe("topic") 
    #client.subscribe("topi")

@mqtt.on_message()
def on_message(client, userdata, msg):
    """
    MQTT'den alınan mesajlar payload edilir.Değişkenler ayrılır.
    :param payload:Mqtt den alınan değer.Sözlüğe çevrilir.
    :param devID:Mqtt den alına verinin devıd değerini temsil eder.
    :param temperaturevalue:Mqtt den alınan sıcaklık verisini temsil eder.
    :param humudityvalue:Mqtt den alınan nem değerlerini temsil eder.
    :param measurement_time:Alınan sıcaklık verisinin gönderilme zamanını temsil eder.
    :param humudity_time :Alınan nem verisinin ölçülme tarihini temsil eder.
    :param alarm_type:Henüz belirlenmediği için boş bir alarm tip değişkeni oluşturulur.
    ilgili cihazı bulmak için devID kullanılır ve ona göre filtreleme yapılır.
    addtemp,add_hum,add_alarms fonksiyonları çağırılıe sıcaklık nem alarm ekleme işlemleri yapılır.

    """
    payload = json.loads(msg.payload)
    devID=payload.get('devID')
    temperaturevalue=payload.get('temperaturevalue')
    humudityvalue=payload.get('humudityvalue')

    measurement_time = datetime.utcnow()  
    humudity_time=datetime.utcnow()

    alarm_type=""
    with create_app().app_context():
        device=Device.get_device_by_DevID(devID)
        addtemp(device.deviceid, temperaturevalue, measurement_time)
        add_hum(device.deviceid,humudityvalue,humudity_time)
        add_alarms(device.deviceid,temperaturevalue,humudityvalue,measurement_time,alarm_type)

@mqtt.on_publish()
def on_publish(client, userdata, mid):
    """
    Mqtt nin veritabanına kayıt edilip edilmediği kontrol edilir 
    mesaj yayınlanırsa termimal ekranından görüntülenmiş olur.

    """
    print("Yayınlandı.".format(mid))
    
def publish_data():

    """
    MQTT'yer veri gönderme işlemi gerçekleşir.
    :param topic:Abone olunan mqtt kanalını temsil eder.
    :param fanspeed:Kayıt edilen tüm istenilen sıcaklık verilerini  liste şeklinde kapsar.
    :param send_thread:Programın sonsuz döngüye girmemsi için thread oluşturulur .
    """
    try:
        topic="topi"
        with create_app().app_context():
             fanspeed=FAN_SPEED.get_all_speed()
             for speed in fanspeed:
                 device=Device.get_device_by_id(speed.deviceid)
                 payload={

                 "devID":device.devID,
                 "speed":speed.fan_speed_value

                 }
                 mqtt.publish("topi",json.dumps(payload))

    except Exception as e:
             print("error:",e)
send_thread=threading.Thread(target= publish_data)
send_thread.start()



