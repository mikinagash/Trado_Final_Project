import requests
import json
from requests.auth import HTTPBasicAuth
from Base.base import Base
from Pages.PStores import StoresPage
import pytest

class test_storesApi:

        def test_search(self):
                response = requests.get(url="https://qa-admin.trado.co.il/#/stores",auth=HTTPBasicAuth(username="1950000000", password="1234"))
                url="https://qa-api.trado.co.il/api/store/filter"
                body={"from":0,"limit":50,"sort":{"createdAt":-1},"filter":{},"search":"ניצי פיצי"}
                res= requests.post(url, data= body)
                assert res.status_code == 200
                print(res.status_code)




