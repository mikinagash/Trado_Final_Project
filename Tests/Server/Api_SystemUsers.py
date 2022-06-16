import requests




class TestSearch:
    url = "https://qa-api.trado.co.il/api/admin-user/filter"

    def test_valid_search_first_name(self):
        body = {"search": "ולדימיר"}
        res = requests.post(self.url,json=body)
        response = res.json()
        assert res.elapsed.total_seconds() < 10
        assert (response['status']) == 200
        assert (response['payload']['count']) == 1
        assert (response['payload']['data'][0]['firstName']) == ' ולדימיר'
        print(res.status_code)
        print(response)

    def test_valid_search_last_name(self):
        body = {"search": "בדיקות"}
        res = requests.post(self.url,json=body)
        response = res.json()
        assert res.elapsed.total_seconds() < 10
        assert (response['status']) == 200
        assert (response['payload']['count']) == 2
        assert (response['payload']['data'][0]['lastName']) == 'בדיקות'
        # assert (response['payload']['data'][1]['lastName']) == 'בדיקות'

        print(res.status_code)
        print(response)

    def test_invalid_search_first_name(self):
        body = {"search": "jhgk"}
        res = requests.post(self.url,json=body)
        response = res.json()
        assert res.elapsed.total_seconds() < 10
        assert (response['status']) == 200
        assert (response['payload']['count']) == 0
        print(res.status_code)
        print(response)

    def test_valid_search_email_name(self):
        body = {"search": "test@gmail.com"}
        res = requests.post(self.url,json=body)
        response = res.json()
        assert res.elapsed.total_seconds() < 10
        assert (response['status']) == 200
        assert (response['payload']['count']) == 1
        assert (response['payload']['data'][0]['email']) == 'test@gmail.com'
        print(res.status_code)
        print(response)

