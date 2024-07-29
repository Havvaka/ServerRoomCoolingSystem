from design.model.tempmodel import Temperature
from flask import Blueprint,request,jsonify,json
from design.model.alarmlogmodel import AlarmLog
from design.model.devicemodel import Device
"""
Eşik alarm değerleriyle ilgili işlemler gerçekleştirilir.

"""

apialarms_log=Blueprint("apialarms_log",__name__,url_prefix="/api/alarms/log")
@apialarms_log.route("/<int:deviceid>",methods=["PUT"])

def update_alarm(deviceid):
    """
    Kullanıcının seçtiği cihaza göre eşik sıcaklık değeri güncellenir.
    :param devthreshtemp:Yeni alınan sıcaklık ölçü değeri temsil eder.
    Alarmog sınıfı içerisindeki update_alarmlog fonksiyonu sayesinde güncelleme işlemi greçekleşir
    
    
    """#Kulanıcının deviceid sine göre belirlediği eşik sıcaklığı buradan güncelleme işelemi yapan fonksiyon.
    try :
        device=Device.get_device_by_id(deviceid)
        if device is not None:
            devthreshtemp=request.json["devthreshtemp"]
            if deviceid.devthreshtemp is not None:
               return ({"success":False,"message":"there is a threshold value"})
           
            AlarmLog.update_alarmlog(deviceid,devthreshtemp)
        return jsonify ({"success":True,"message":"alarm log successfully updateded"})
    except Exception as e :
        return jsonify ({"success":False,"message":"error "})
    

























# @apialarms_log.route("/addAlarmlog/<int:deviceid>",methods=["GET"])

# def add_alarmlog(deviceid):
#     try: 
#         #devicename=request.json["devicename"]
#         devthreshtemp=request.json["devthreshtemp"]
        

#         #device=Device.device_name(devicename)

#         AlarmLog.addalarmslog(deviceid,devthreshtemp)
#         return jsonify({"success":True,"message":"true"})

#     except Exception as e:
#         print("error:",e)

#         return jsonify({"success":False,"message":"error"})



