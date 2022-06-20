import requests
import pytest

class Test_api_orsers():
    url = 'https://qa-api.trado.co.il/api/order/filter'

    def test_valid_search_type_pyment_b2b(self):
        body = {"search": "b2b"}
        res = requests.post(self.url,json=body)
        response = res.json()
        assert res.elapsed.total_seconds() < 10
        assert (response['status']) == 200
        assert (response['payload']['count']) == 45
        assert (response['payload']['data'][0]['PaymentType']) == ' b2b'
        print(res.status_code)
        print(response)

    def test_valid_search_type_pyment_bankTransfer(self):
        body = {"search": "bankTransfer"}
        res = requests.post(self.url, json=body)
        response = res.json()
        assert res.elapsed.total_seconds() < 10
        assert (response['status']) == 200
        assert (response['payload']['count']) == 169
        assert (response['payload']['data'][0]['PaymentType']) == 'bankTransfer'
        print(res.status_code)
        print(response)

    def test_valid_search_type_pyment_etrado(self):
        body = {"search": "etrado"}
        res = requests.post(self.url, json=body)
        response = res.json()
        assert res.elapsed.total_seconds() < 10
        assert (response['status']) == 200
        assert (response['payload']['count']) == 48
        assert (response['payload']['data'][0]['PaymentType']) == 'etrado'
        print(res.status_code)
        print(response)

    def test_valid_search_order_numbers(self):
        body = {"search": "470"}
        res = requests.post(self.url, json=body)
        response = res.json()
        assert res.elapsed.total_seconds() < 10
        assert (response['status']) == 200
        assert (response['payload']['count']) == 1
        assert (response['payload']['data'][0]['PaymentType']) == '470'
        print(res.status_code)
        print(response)
