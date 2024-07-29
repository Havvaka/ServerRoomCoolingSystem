
from flask import Flask,current_app
from flask_sqlalchemy import SQLAlchemy
from flask_mqtt import Mqtt
from flask_socketio import SocketIO 

db=SQLAlchemy()
mqtt= Mqtt()
def create_app():
    """    
    app Nesnesi oluşturulur.Veritabanı path i eklenerek bağlantı oluşturulur ve
    init methoduyla app nesnesiyle bağlanır.Mqtt bağantısı da sağlanır broker url'si 
    config edilir.
    Mqtt sınıfı init methoduyla app nesnesine bağlanma işlemi yapılır ve app nesnesini geri döndürür.
    return:App nesnesini gerekli bağlamlar oluşturduktan sonra gönderir.

    """
    app=Flask(__name__)
    with app.app_context():
        #current_app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///.../database/db.db'
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Havva/Desktop/cihazların sıcaklık ölçüm projesi/templates/api/database.db'
        
        #app.config['MQTT_BROKER_URL'] = '172.16.20.85'
        app.config['MQTT_BROKER_URL']="172.20.10.14"

        app.config['MQTT_BROKER_PORT'] = 1883             # Broker bağlağlantı noktası
        app.config['MQTT_KEEPALIVE'] = 60
        app.config['MQTT_TLS_ENABLED'] = False        
        app.config['TEMPLATES_AUTO_RELOAD'] = True
        app.config['SECRET_KEY']='secret!'
        
        db.init_app(app)
        mqtt.init_app(app)
       
        print(db.session) 
        
        return app