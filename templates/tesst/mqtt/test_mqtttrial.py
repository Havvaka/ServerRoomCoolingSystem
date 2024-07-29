import unittest
import json
from design.connection import create_app,db
from mqtt.mqtttrial2 import on_message
from unittest.mock import ANY
from design.model.devicemodel import Device
from unittest.mock import patch, MagicMock
class Test_Mqtt(unittest.TestCase):

    @patch('design.connection.create_app')
    def test_mqtt_message(self,mock_create_app):
        mock_app=MagicMock()
        mock_create_app.return_value=mock_app


        mqtt_message=MagicMock()

        mqtt_message.payload=json.dumps({
            'devID': 'deviced',
            'temperaturevalue': 25.5,
            'humudityvalue': 1.0

        })
        on_message(None, None, mqtt_message)
        mock_addtemp = mock_app.addtemp
        mock_addtemp.assert_called_with('deviced', 25.5, ANY) 
        mock_add_hum = mock_app.add_hum
        mock_add_hum.assert_called_with('deviced', 1.0, ANY) 
        mock_add_alarms = mock_app.add_alarms
        mock_add_alarms.assert_called_with('deviced', 25.5, 1.0, ANY, '')
