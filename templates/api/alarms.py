from design.model.alarmsmodel import Alarms
from flask import Blueprint,request,jsonify
from design.model.alarmlogmodel import AlarmLog

def add_alarms(deviceid,temperaturevalue,humudityvalue,measurement_time,alarm_type):
    """
    Alarm kaydetme işlemleri buradan yapılır.veritabanından alından
    deviceid ' ye göre filtrelenmiş cihazın eşik sıcaklığı getirilir.
    :param all_alarmlog :İlgili cihaz id'ye göre eşik sıcaklığı getirir.
    :param temp_value:Sıcaklık değerini int hala getirir.
    :param hum_value:nem değerini int hala getirir.
    :param altemvalue:İlgili cihaza ait kaydedilen eşik sıcaklık değerini temsil eder.
    :return:Kontreol işlemleri yapıldıktan sonra işlemin gerçekleştiğine dair mesaj gönderir.
    """
    all_alarmlog=AlarmLog.get_alarms_by_id(deviceid)
    temp_value=int(temperaturevalue)
    hum_value=int(humudityvalue)
    altempvalue=int(all_alarmlog.devthreshtemp)
    if (temp_value>altempvalue):
        temp_alarm=temp_value
        hum_alarm=hum_value
        if(temp_value>altempvalue):
            alarm_time=measurement_time
            alarm_type="temperature"
            Alarms.add_alarm(deviceid,temp_alarm,hum_alarm,alarm_time,alarm_type)
    elif((temp_value+5)>altempvalue):
        temp_alarm=temp_value
        hum_alarm=hum_value
        if((temp_value+5)>altempvalue):
            alarm_time=measurement_time
            alarm_type="temperature5"
            Alarms.add_alarm(deviceid,temp_alarm,hum_alarm,alarm_time,alarm_type)  

"""
Alarmla ilgili yapılacak işlemler için Blueprint oluşturulur./api/alarms eki belirlenir.
GET methodu seçildiğinde ve getAlarms url' de eklendiğinde oluşacak işlemleri sağlar.
"""
apiAlarms=Blueprint("apialarms",__name__,url_prefix="/api/alarms")
@apiAlarms.route("/getAlarms",methods=["GET"])

def show_message_to_user():
    try:
        
        """
        Tüm alarmlar çağırılır ve iki ayrı listede olacak şekilde kategoriye ayrılır.
        :param alarmss:Her cihaz için listelenen alarmları turar.
        :param tem:Sıcaklık değeri eşik değeri aştığında oluşacak alarmın tipini belirtir.
        :param temp5:Sıcaklık değeri eşik değere 5 derece yaklaştığında oluşacak alarmın türünü temsil eder.
        :return:Başarılı işlem gerçekleştiğini ve listelenen verileri gönderir.      
        
        """  
        alarmss=Alarms.all_alarms()
        tem=[]
        temp5=[]
        for alarm in alarmss:         
            if alarm.alarm_type=="temperature":  
               tem.append({"device":alarm.deviceid,"temperature":alarm.tempalarm,"humudity":alarm.humalarm,"alarmtime":alarm.alarm_time})
            elif alarm.alarm_type=="temperature5":
               temp5.append({"device":alarm.deviceid,"temperature":alarm.tempalarm,"humudity":alarm.humalarm,"alarmtime":alarm.alarm_time})
        return jsonify({"success":True,"message":"temperature value is above the specified value","data":tem,"data2":temp5})
    except Exception as e:
        return jsonify ({"susses":False,"message":"error message"})
    



#Alarm kaydetme işlemlerini buradan yapıyoruz ,herhangi bir routa gerek duymuyoruz .Veritanında oluşmuş deviceid'sine göre filtrelenmiş cihazın eşik sıcaklığını getiriyoruz.
#Sıcaklık ve nem değerlerini ayrı ayrı integer'a çeviriyoruz.Ayrıca kullanıcıdan alınmış ilgili cihazın sıcaklık değerini de integer a çeviriyoruz.
#Öncelikle sıcaklık eşik değerden yüksek mi diye kontrol ediyorum.Eğer yüksekse değeri tempalarm değişkenine atıyorum.Alarm tipini de sıcaklık olarak belirliyorum.
#Bu eşik değerinden yukuarıda sıcaklık olduğunu belirtiyor.
#Veritabanına kadetme işlemini yapıyorum.
#Aynı işlemi sıcaklık eşik değere 5 derece yaklaştığında da yapıyorum ,elif kod bloğu bu işlemi gerçekleştiriyor.


