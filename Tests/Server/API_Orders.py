import requests



class TestSearch:
    url = "https://qa-api.trado.co.il/api/order/filter"
    # Bug
    def test_search_first_name_correct(self):
        body = {"search": "עדי"}
        res = requests.post(self.url,json=body)
        response = res.json()
        assert res.elapsed.total_seconds() < 10
        assert response['payload']['count'] == 0
        assert res.status_code == 200



    # Bug
    def test_search_last_name_correct(self):
        body = {"search": "אמזלג"}
        res = requests.post(self.url,json=body)
        response = res.json()
        assert res.elapsed.total_seconds() < 10
        assert res.status_code == 200
        print(res.status_code)
        print(response)


    # Bug
    def test_search_order_correct_by_partly_first_name(self):
        body = {"search": "עד"}
        res = requests.post(self.url, json=body)
        response = res.json()
        assert response['payload']['count'] == 0
        assert res.status_code == 200
        print(res.status_code)
        print(response['payload']['count'])



    def test_search_order_incorrect_by_first_name(self):
        body = {"search": "גגג"}
        res = requests.post(self.url, data=body)
        response = res.json()
        assert response['payload']['count'] == 0
        assert res.elapsed.total_seconds() < 10





    def test_search_order_incorrect_with_special_characters(self):
        body = {"search": "!#$&*"}
        res = requests.post(self.url, json=body)
        response = res.json()
        assert response['payload']['count'] == 0
        print(response['payload']['count'])



    # Bug
    def test_search_order_correct_with_order_numbers(self):
        body = {"search": "418"}
        res = requests.post(self.url, json=body)
        response = res.json()
        assert response['payload']['count'] == 0
        assert res.status_code == 200
        print(res.status_code)
        print(response)



    def test_search_order_correct_with_invalid_order_numbers(self):
        body = {"search": "1335"}
        res = requests.post(self.url, json=body)
        response = res.json()
        assert response['payload']['count'] == 0
        print(res.status_code)
        print(response)




    #Bug
    def test_search_order_correct_with_bankTransfer_payment(self):
        body = {"search": "bankTransfer"}
        res = requests.post(self.url, json=body)
        response = res.json()
        assert response['payload']['count'] == 0
        assert res.status_code == 200
        print(res.status_code)
        print(response)




    # Bug
    def test_search_order_correct_with_b2b_payment(self):
        body = {"search": "bankTransfer"}
        res = requests.post(self.url, json=body)
        response = res.json()
        assert response['payload']['count'] == 0
        assert res.status_code == 200
        print(res.status_code)
        print(response)



    # Bug
    def test_search_order_correct_with_etrado_payment(self):
        body = {"search": "etrado"}
        res = requests.post(self.url, json=body)
        response = res.json()
        assert res.status_code == 200
        print(res.status_code)
        print(response)




    def test_search_order_correct_with_invalid_payment(self):
        body = {"search": "לאומי"}
        res = requests.post(self.url, json=body)
        response = res.json()
        assert response['payload']['count'] == 0
        assert res.status_code == 200
        print(res.status_code)
        print(response)






