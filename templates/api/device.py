from flask import Blueprint,request,jsonify ,json
from design.model.devicemodel import Device
from design.model.alarmlogmodel import AlarmLog


apiDevice=Blueprint("apiDevice",__name__,url_prefix="/api/device")
@apiDevice.route("/allDevice",methods=["GET"])

def All_device():
    """
    Tüm cihazlar listelenir.
    :param devices:Cihazların kaydedileceği listeyi temsil eder.
    :return:İşlemin başarıyle gerçekleştiğine dair bildirim ve cihaz verileri gönderilir.
    
    """
    try:
        alldevice=Device.get_all_device()
        devices=[]
        for device in alldevice:
            devices.append({"deviceId":device.deviceid,"deviceName":device.devicename,"devID":device.devID})            
        return jsonify({"success": True,"data":devices,"count":len(devices)})
    except Exception as e:
        print("error:",e)
        return jsonify({"success":False,"message":"there is an error"})
    
@apiDevice.route("/addDevice",methods=["GET"])
def add_Device():
    try:
        """
        Yeni cihaz ve eşik sıcaklık ekleme işlemi yapılır.
        :param devicename:Eklenen cihazın adı.
        :pram devID:Eklenen cihazın cihaz id'si.
        :param devthreshtemp:Eklenecek cihaza ait eşik sıcaklık derecesi.

        """
        devicename=request.json["deviceName"]
        devID=request.json["deviceId"]
        devthreshtemp=request.json["devthreshtemp"]

        Device.add_device(devicename,devID)
        device=Device.get_device_by_DevID(devID)
        AlarmLog.addalarmslog(device.deviceid,devthreshtemp)
        return jsonify({"success":True,"message":"Device name added successfully.."})
    
    except Exception as e:
        return jsonify({"success":False,"message":"there is an error"})
    
@apiDevice.route("/<int:deviceid>",methods=["GET","PUT","DELETE"])   
def device(deviceid):
    try:
        """
        Belirtilen methoda göre cihaz listesi ,güncelleme ,silme işlemleri gerçeklerşir.
        :param device:İstenilen cihaza ait cihaz verileri.
        :param deviceobj:Cihaz verilerinin eklendiği liste .
        
        """
        device=Device.get_device_by_id(deviceid)
        if device==None:
            return jsonify({"success":False,"message":"device not found"})
        if request.method=="GET":
            deviceobj=({"deviceId":device.deviceid,"deviceName":device.devicename,"devId":device.devID})
            return jsonify({"success":True,"data":deviceobj})
        elif request.method=="DELETE":
            Device.delete_device(deviceid)
            return jsonify({"success":True,"message":"device deleted successfully"})
        elif request.method=="PUT":   
            devicename=request.json["deviceName"]
            devID=request.json["deviceId"]
            Device.update_device(deviceid,devicename,devID)

            return jsonify({"success":True,"message":"device updated successfully"})
        
    except Exception as e:
          print("error:",e)
          return jsonify({"success":False,"message":"transaction failed"})
    



# @apiDevice.route("/<int:deviceid>/" ,methods=["GET"])
    
# def temp_hum(deviceid):


  





