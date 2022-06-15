import requests

def test_submit_date_api():
    url = "https://qa-api.trado.co.il/api/reports/fields"
    myobj = {"store_id": "1010101011rh", "start_date": "2022-06-05T20:49:46.752Z", }
    x = requests.post(url, data=myobj)
    value = x.status_code
    assert value == 200

def test_serch_systems_users():
    url = "https://qa-api.trado.co.il/api/admin-user/filter"
    myobj = {"uid": "pslikkckpo2006r", "sid": "1010101011rh", "lng": "hebrew", "getTypes": "true", "platform": "admin",}
    x = requests.post(url, data=myobj)
    value = x.status_code
    assert value == 200

