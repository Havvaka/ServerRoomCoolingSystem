from flask import Blueprint,request,json,jsonify
from design.model.fanspeedmodel import FAN_SPEED
from design.model.devicemodel import Device


apiSpeed=Blueprint("apiSpeed",__name__,url_prefix="/api/speed")

@apiSpeed.route("/<int:deviceid>",methods=["GET"])

def speed(deviceid):
    try:
        """
        İlgili cihaz id'sine göre fan hızı verilerini getirir.
        :param speed: İlgili cihaz fan hızı verilerini içerir.
        :param device: İlgili cihaza ait cihaz verilerini içerir.
        :return: Cihaz bulunamadıysa gönderilecek mesaj verilerini içerir.
        :param speedobj: İLgili cihaza ait fan hızı verilerini json formatında içerir.
        :return: İlgili cihaza ait verileri ve işlemin başarılı bir şekilde gerçekleştiğinin bilgisini içerir.
        
        """
        speed=FAN_SPEED.get_all_speed_by_id(deviceid)
        device=Device.get_device_by_id(deviceid)
        
        if device==None:
            return jsonify({"success":False,"message":"specified value not found"})

        if request.method=="GET":
           speedobj=({"device name":device.devicename,"taken temperature":speed.fan_speed_value})
           return jsonify ({"success":True,"message":"success","data":speedobj})
    except Exception as e:
          return jsonify({"success":False,"message":"error"})
       

@apiSpeed.route("/delete/<int:deviceid>",methods=["DELETE"])
def delete_speed(deviceid):
    """
    İlgili cihazın fan hızı verilerinin silinme işlemini yapar.
    :return:İşlemin başarıyla gerçekleştiği bildirimini gönderir.
    
    """
    FAN_SPEED.delete_speed(deviceid)
    return jsonify({"success":True,"message":"the specified temperature value has been deleted successfully"})

@apiSpeed.route("/update/<int:deviceid>",methods=["PUT"])
def update_speed(deviceid):
    """
    ilgili cihaza ait fan hızı verilerinin güncellenme işlemini yapar.
    :param new_fan_speed: Yen alınan fan hızı verilerini içerir.
    :return:İŞlemin başarılı bir şekilde gerçekleştiği bilgisini gönderir.
    """
    new_fan_speed=request.json["fans"]

    FAN_SPEED.update_speed(deviceid,new_fan_speed)
    
    return jsonify({"success":True,"message":"the specified temperature value has been successfully updated"})

@apiSpeed.route("/addspeed/<int:deviceid>",methods=["GET"])
def addspeed(deviceid):
    """
    Kullanıcıdan alınan fan hızı verilerini veritabanına kaydetme işlemini yapar.
    :param device:İlgili cihaza ait cihaz verilerini içerir.
    :param fan_speed_value: Json olarak alınan fan hızı verisini içerir.
    :return: İşlemin başarıyla gerçekleştiği bilgisini içerir.

    """
    device=Device.get_device_by_id(deviceid)
    fan_speed_value=request.json["fanspeedvalue"]
    FAN_SPEED.add_speed(device.deviceid,fan_speed_value)
    return jsonify({"success":True,"message":"successfully added"})


# @apiSpeed.route("/addSpeed",methods=["POST"])

# def add_speed():
#     try:

        
#         fan_speed_value=request.json["fanspeedvalue"]
#         device=Device.device_name(devicename)
#         FAN_SPEED.add_speed(device.deviceid,fan_speed_value)
#         return jsonify({"success":True,"message":"successfully added"})

#     except Exception as e:
#         return jsonify({"success":False,"message":"error"})

