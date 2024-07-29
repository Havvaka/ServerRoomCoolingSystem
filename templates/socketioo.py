# from design.connection import socketio

# from design.model.tempmodel import Temperature
# from flask import current_app
# from design.connection import create_app
# import threading
# import time
# #from mqtt.mqtttrial2 import global_temp


# # def verial(data):
# #     return handle_veri(data)
#    #socketio.emit('veri',data,namespace="/test")
 
# @socketio.on('connect',namespace="/test")
# def handle_connect():
#     print('Bir istemci bağlandı!')
    
  
#     sende_thread=threading.Thread(target=send_temp)
    
#     sende_thread.start()
#     sende_thread.join()



# def send_temp():
#     last_temp=Temperature.last_temp_value()
   
#     while True:
#             last_temp=Temperature.last_temp_value()
#             socketio.emit("veri",last_temp,namespace="/test")
#             time.sleep(5)



# @socket.on('disconnect', namespace="/test")
# def handle_disconnect():
#     #İstemciden ayrılmak ,bağlantı kesilmesi sağlanır ve bildirim gelir.
    
#     print('Bir istemci bağlantısı kesildi')


#
#