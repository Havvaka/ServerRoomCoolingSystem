from design.model.humuditymodel import Humudity

def add_hum(deviceid,humudityvalue,humudity_time):
    """
    MQTT'den alınan değerlerin veritabanına kaydetme işlemi gerçekleşir.
    :param deviceid :Cihaz idsi oalrak kayıt edilir.
    :param humudityvalue:Nem değeri temsil eder.
    :param humudity_time:Ölçüm zamanını temsil eder.
    add_humu Fonksiyonu çağırılarak kayıt işlemi gerçekleştirilir.
    
    
    """
    deviceid=deviceid
    humudityvalue=humudityvalue
    humudity_time=humudity_time
    Humudity.add_humu(deviceid,humudityvalue,humudity_time)


