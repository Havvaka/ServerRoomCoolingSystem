
import eventlet
eventlet.monkey_patch()
from design.connection import create_app
from design.connection.initialize import createdb
from api.device import apiDevice
from api.alarms import apiAlarms
from api.temperature import apiTemp
from flask_socketio import SocketIO
from api.speed import apiSpeed
from api.alarmlog import apialarms_log
from mqtt.mqtttrial2 import on_message,on_connect,on_publish,publish_data
from design.model.tempmodel import Temperature


"""
Gerekli kütüphaneler programa dahil edilir.
Create_app fonksiyonu çağırılır.Socketio app ile bağlanır.


"""
app=create_app()
createdb(app)

"""
    Veritabanına kayıtlı en son sıcaklık değeri çağırılır lastemp değişkenine atanır.
    socket parametresini ve emit fonksiyonunu kullanarak istemcideki veri olayına gönderilir.
    
"""


socket = SocketIO(app, logger=True, engineio_logger=True,namespace="/test")


@socket.on('connect',namespace="/test")
def handle_connect():
    #istemciye bağlanmak test edilir.
    print('Bir istemci bağlandı!')

def emit_():
    
    last_temp=Temperature.last_temp_value()
    socket.emit("veri",last_temp,namespace="/test")
"""
    Döngü içerisinde kesintisi veri gönderilir.Eventlet module kullarak yapılır.
    Bu iişlemi 10 saniyede bir tekrarlanması sağlanır.
    

"""

def send_temp():
   
    while True:
        emit_()
        eventlet.sleep(10)
eventlet.spawn(send_temp)



publish_data()

app=create_app()
app.register_blueprint(apiSpeed) 
app.register_blueprint(apiDevice)      
app.register_blueprint(apiAlarms)     
app.register_blueprint(apiTemp)        
app.register_blueprint(apialarms_log)


if __name__=='__main__':
    socket.run(app, host='0.0.0.0', port=5000)
   # app.run(host="0.0.0.0")
   

