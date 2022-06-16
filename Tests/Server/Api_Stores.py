import requests
import json
from requests.auth import HTTPBasicAuth
from Base.base import Base
from Pages.PStores import StoresPage
import pytest

class Test_storeSearch:
        url= "https://qa-api.trado.co.il/api/store/filter"

#31
        def test_Valid_response_when_search_ByStore_name(self):
                body = {"search":"סופר כל רונן בעמ"}
                res = requests.post(self.url,data=body)
                response = res.json()
                assert res.elapsed.total_seconds() < 10
                assert res.status_code == 200

#32
        def test_Valid_response_when_search_ByStore_phone(self):
                body = {"search":"0547795920"}
                res = requests.post(self.url,data=body)
                response = res.json()
                assert res.elapsed.total_seconds() < 5
                assert res.status_code == 200

#33
        def test_Valid_response_when_search_ByPartial_store_phone(self):
                body = {"search": "05477"}
                res = requests.post(self.url, data=body)
                response = res.json()
                assert res.elapsed.total_seconds() < 5
                assert res.status_code == 200
                # assert response['active']== True
                # print(response)

#34
        def test_Valid_response_when_search_Bystore_email(self):
                body = {"search": "netz@walla.com"}
                res = requests.post(self.url, data=body)
                response = res.json()
                assert res.elapsed.total_seconds() < 5
                assert res.status_code == 200


#35
        def test_Valid_response_when_search_Bypartial_store_email(self):
                body = {"search": "netz@"}
                res = requests.post(self.url, data=body)
                response = res.json()
                assert res.elapsed.total_seconds() < 5
                assert res.status_code == 200

#36
        def test_Valid_response_when_search_Bypartial_store_name(self):
                body = {"search": "tomi"}
                res = requests.post(self.url, data=body)
                response = res.json()
                assert res.elapsed.total_seconds() < 5
                assert res.status_code == 200

#37
        def test_Invalid_response_when_search_Bystore_address(self):
                body = {"search": "dor 13/45"}
                res = requests.post(self.url, data=body)
                response = res.json()
                assert res.elapsed.total_seconds() < 5
                assert res.status_code == 200

#38
        def test_Invalid_response_when_search_Bystore_bnNum(self):
                body = {"search": "1122333"}
                res = requests.post(self.url, data=body)
                response = res.json()
                assert res.elapsed.total_seconds() < 5
                assert res.status_code == 200

#39
        def test_Invalid_response_when_search_Bystore_Departments(self):
                body = {"search": "שוקולדים"}
                res = requests.post(self.url, data=body)
                response = res.json()
                assert res.elapsed.total_seconds() < 5
                assert res.status_code == 200

#40
        def test_Invalid_response_when_search_Bystore_CreatedDate(self):
                body = {"search":"09/11/21"}
                res = requests.post(self.url, data=body)
                response = res.json()
                assert res.elapsed.total_seconds() < 5
                assert res.status_code == 200

#41
        def test_Invalid_response_when_search_Bystore_CreatedHour(self):
                body = {"search":"21:00"}
                res = requests.post(self.url, data=body)
                response = res.json()
                assert res.elapsed.total_seconds() < 5
                assert res.status_code == 200

















