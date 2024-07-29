from flask import Blueprint,request,jsonify,current_app
from design.model.tempmodel import Temperature
from design.model.humuditymodel import Humudity
from design.model.devicemodel import Device

def addtemp(deviceid,temperaturevalue,measurement_time):
          """
          MQTT'den alınan sıcaklık verilerinin veritabanına eklenme işlemi gerçekleşir.
          :param temperaturevalue:Mqtt den alınan sıcaklık değerinin yeni değere atanması.
          :param measurement_time:Ölçüm zamanının yeni alınması ve bu değre atanmasını temsil eder.
          add_temp fonksiyonunu kullanarak yeni sıcaklık değeri eklenir.Bu değer Temperature sınıfından alınır.
          :return:İşlemin gerçekleştiğine dair bir geribildirim gönderilir.

         """

          try:
              temperaturevalue=temperaturevalue
              deviceid=deviceid
              measurement_time=measurement_time
              Temperature.add_temp(deviceid,temperaturevalue,measurement_time)
          
          except Exception as e:
               return jsonify({"success":True,"message":"error"})
          




apiTemp=Blueprint("apiTemp",__name__,url_prefix="/api/temperature") 
@apiTemp.route("/gettemp/<int:deviceid>",methods=["GET"])
def get_temp(deviceid):
     """
     Get methodu kullanıldığında ilgili cihaz id ye ait ilgili tarihler aralığındaki 
     ölçülmüş değerer alınır.  
     """
     filter_mea=Temperature.get_tem_by_mea(deviceid)
     list=[]
     for mea in filter_mea:
          list.append(mea)

     return jsonify({"success":True,"data":list})













# @apiTemp.route("/<int:deviceid>",methods=["GET","PUT","POST"])
# def get_alltemp(deviceid):   
#         """
#         Belirtilen cihaz id sine göre sıcaklık ve nem değerlerini listeye ekleyip kullanıcıya gösterir
        
        
#         """
#         temperature=Temperature.get_all_temp_dev_id(deviceid) 
#         humudity=Humudity.get_all_by_id(deviceid)
#         device=Device.get_device_by_id(deviceid)   
#         liste=[]
#         if temperature==None or humudity==None:
#             return jsonify({"success":False,"message":"device not found"}) 
#         elif(request.method=="GET" ):
#             for temp in temperature:
#                 for hum in humudity:
#                     if hum.humudityid:      
#                         tempobj=({"DEVİCE":device.devicename,"TEMPERATURE":temp.temperaturevalue,"HUMUDİTY":hum.humudity_value})
#                         liste.append(tempobj)
            
#                 return jsonify({"success":True,"data":liste})



# def temperature_humudity_update(temperature,humudity,device):
#     while True:
#          for temp in temperature:
#             for hum in humudity:
                   
#                     temp_value=temp.temperaturevalue
#                     hum_value=hum.humudity_value
#                     devicenam_e=device.devicename
#                     dataobj={
#                             "DEVİCENAME":devicenam_e,
#                             "YEMPERATURE":temp_value,
#                              "HUMUDİTY":hum_value
#                        }
#             with data_lock:
#                 data.append(dataobj)

#          time.sleep(5)



#data_lock=threading.Lock()
