import socketio


server_url = 'http://localhost:5000/'

# Socket.IO istemcisi oluşturdu 
sio = socketio.Client(logger=True, engineio_logger = True)

#Bağlandığında tetiklenecek olay işleyicisi
@sio.on('connect',namespace="/test")
def on_connect():
    try:
        print('Bağlandı Test!')
    except:
        pass
#mesage olayına yanıt


@sio.on("veri",namespace="/test")
def on_data(lastemp):
    try:
         print('Alınan veri:',lastemp)
    #    print("Device ID:", data["deviceid"])
    #    print("Temperature:", data["temperaturevalue"])
    #    print("Humidity:", data["humudityvalue"])
    except:
     pass
# Socket.IO sunucusuna bağlandım
sio.connect(server_url,namespaces="/test")



#sio.disconnect()
