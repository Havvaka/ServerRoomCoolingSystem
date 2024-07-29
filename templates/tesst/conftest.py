
# import pytest
# from design.connection  import create_app
# from design.connection import db
# from api.device import apiDevice

# @pytest.fixture()
# def app():
#     app = create_app()
#     app.register_blueprint(apiDevice)

#     with app.app_context():
#         db.create_all()
#         print("Veritabanı oluşturuldu")  # Veritabanını oluşturun
#     yield app

# @pytest.fixture()
# def client(app):
#     return app.test_client()

# def test_request_example(client):
#     print(client)
#     response = client.get("/api/device/allDevice")
#     print(response)


#     assert response.status_code == 200
#     assert response.content_type == "application/json"

#     # Yanıtın içeriğini JSON olarak ayrıştırır
#     data = response.get_json()

#     # Yanıtın "success" özelliğinin True olduğunu doğrular
#     assert data["success"] is True

#     # İlk cihazın "deviceId", "deviceName" ve "devthreshtemp" özelliklerine sahip olduğunu doğrular
#     first_device = data["data"][0]
#     assert "deviceId" in first_device
#     assert "deviceName" in first_device
#     assert "dedvID" in first_device
