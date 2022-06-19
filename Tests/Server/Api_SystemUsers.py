import requests


class TestSearch():
    url = "https://qa-api.trado.co.il/api/admin-user/filter"

    def test_valid_search_first_name(self):
        body = {"search": "ייהלם"}
        res = requests.post(self.url, json=body)
        response = res.json()
        assert res.elapsed.total_seconds() < 10
        assert (response['status']) == 200
        assert (response['payload']['count']) == 1
        assert (response['payload']['data'][0]['firstName']) == 'ייהלם'
        print(res.status_code)
        print(response)

    def test_valid_search_last_name(self):
        body = {"search": "בדיקות"}
        res = requests.post(self.url, json=body)
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
        res = requests.post(self.url, json=body)
        response = res.json()
        assert res.elapsed.total_seconds() < 10
        assert (response['status']) == 200
        assert (response['payload']['count']) == 0
        assert (response['payload']['data']['count']) == "0"

        print(res.status_code)
        print(response)

    def test_valid_search_email_name(self):
        body = {"search": "test@gmail.com"}
        res = requests.post(self.url, json=body)
        response = res.json()
        assert res.elapsed.total_seconds() < 10
        assert (response['status']) == 200
        assert (response['payload']['count']) == 1
        assert (response['payload']['data'][0]['email']) == 'test@gmail.com'
        print(res.status_code)
        print(response)

    def test_valid_editing_firstName(self):
        url = "https://qa-api.trado.co.il/api/admin-user/update"
        body = {"firstName":"salmonsalmon","lastName":"סלמון",
                "email":"dfgdfg@dsd.fs","phone":"9513247812",
                "role":"delivery","permission":"read",
                "id":"4jp555dl4b2tieg"}
        res = requests.post(url, json=body)
        response = res.json()
        assert res.elapsed.total_seconds() < 10
        assert (response['status']) == 200
        # assert (response['payload']['count']) == 1
        # assert (response['payload']['data'][0]['firstName']) == 'dan'
        print(res.status_code)
        print(response)

    def test_valid_editing_lastName(self):
        url = "https://qa-api.trado.co.il/api/admin-user/update"
        body = {"firstName":"elieli","lastName":"tasama",
                "email":"dfgdfg@dsd.fs","phone":"9513247812",
                "role":"delivery","permission":"read",
                "id":"4jp555dl4b2tieg"}
        res = requests.post(url, json=body)
        response = res.json()
        assert res.elapsed.total_seconds() < 10
        assert (response['status']) == 200
        # assert (response['payload']['count']) == 1
        # assert (response['payload']['data'][0]['firstName']) == 'dan'

    def test_valid_editing_email(self):
        url = "https://qa-api.trado.co.il/api/admin-user/update"
        body = {"firstName":"salmonsalmon","lastName":"סלמון",
                "email":"salmon@dsd.fs","phone":"9513247812",
                "role":"delivery","permission":"read",
                "id":"4jp555dl4b2tieg"}
        res = requests.post(url, json=body)
        response = res.json()
        assert res.elapsed.total_seconds() < 10
        assert (response['status']) == 200
        # assert (response['payload']['count']) == 1
        # assert (response['payload']['data'][0]['firstName']) == 'dan'

    def test_valid_editing_phone(self):
        url = "https://qa-api.trado.co.il/api/admin-user/update"
        body = {"firstName":"salmonsalmon","lastName":"סלמון",
                "email":"dfgdfg@dsd.fs","phone":"0547877475",
                "role":"delivery","permission":"read",
                "id":"4jp555dl4b2tieg"}
        res = requests.post(url, json=body)
        response = res.json()
        assert res.elapsed.total_seconds() < 10
        assert (response['status']) == 200
        # assert (response['payload']['count']) == 1
        # assert (response['payload']['data'][0]['firstName']) == 'dan'

    def test_valid_editing_role(self):
        url = "https://qa-api.trado.co.il/api/admin-user/update"
        body = {"firstName":"salmonsalmon","lastName":"סלמון",
                "email":"dfgdfg@dsd.fs","phone":"9513247812",
                "role":"חנות","permission":"הרשאה",
                "id":"4jp555dl4b2tieg"}
        res = requests.post(url, json=body)
        response = res.json()
        assert res.elapsed.total_seconds() < 10
        assert (response['status']) == 200


    def test_valid_editing_authorization(self):
        url = "https://qa-api.trado.co.il/api/admin-user/update"
        body = {"firstName":"salmonsalmon","lastName":"סלמון",
                "email":"dfgdfg@dsd.fs","phone":"9513247812",
                "role":"delivery","permission":"read",
                "id":"4jp555dl4b2tieg"}
        res = requests.post(url, json=body)
        response = res.json()
        assert res.elapsed.total_seconds() < 10
        assert (response['status']) == 200
        # assert (response['payload']['count']) == 1
        # assert (response['payload']['data'][0]['firstName']) == 'dan'

    def test_invalid_editing_firstName_is_null(self):
        url = "https://qa-api.trado.co.il/api/admin-user/update"
        body = {"firstName":"","lastName":"סלמון",
                "email":"dfgdfg@dsd.fs","phone":"9513247812",
                "role":"delivery","permission":"read",
                "id":"4jp555dl4b2tieg"}
        res = requests.post(url, json=body)
        response = res.json()
        assert res.elapsed.total_seconds() < 10
        assert (response['status']) == 400
        # assert (response['payload']['count']) == 1
        # assert (response['payload']['data'][0]['firstName']) == 'dan'
        print(res.status_code)
        print(response)

    def test_invalid_editing_lastName_is_null(self):
        url = "https://qa-api.trado.co.il/api/admin-user/update"
        body = {"firstName":"salmonsalmon","lastName":"",
                "email":"dfgdfg@dsd.fs","phone":"9513247812",
                "role":"delivery","permission":"read",
                "id":"4jp555dl4b2tieg"}
        res = requests.post(url, json=body)
        response = res.json()
        assert res.elapsed.total_seconds() < 10
        assert (response['status']) == 400


    def test_invalid_editing_email_is_null(self):
        url = "https://qa-api.trado.co.il/api/admin-user/update"
        body = {"firstName":"salmonsalmon","lastName":"סלמון",
                "email":"","phone":"9513247812",
                "role":"delivery","permission":"read",
                "id":"4jp555dl4b2tieg"}
        res = requests.post(url, json=body)
        response = res.json()
        assert res.elapsed.total_seconds() < 10
        assert (response['status']) == 400


    def test_invalid_editing_email_is_invalid(self):
        url = "https://qa-api.trado.co.il/api/admin-user/update"
        body = {"firstName":"salmonsalmon","lastName":"סלמון",
                "email":"sasddsa","phone":"9513247812",
                "role":"delivery","permission":"read",
                "id":"4jp555dl4b2tieg"}
        res = requests.post(url, json=body)
        response = res.json()
        assert res.elapsed.total_seconds() < 10
        assert (response['status']) == 400

    def test_invalid_editing_phone_is_null(self):
        url = "https://qa-api.trado.co.il/api/admin-user/update"
        body = {"firstName":"salmonsalmon","lastName":"סלמון",
                "email":"dfgdfg@dsd.fs","phone":"",
                "role":"delivery","permission":"read",
                "id":"4jp555dl4b2tieg"}
        res = requests.post(url, json=body)
        response = res.json()
        assert res.elapsed.total_seconds() < 10
        assert (response['status']) == 400


    def test_invalid_editing_phone_is_invalid(self):
        url = "https://qa-api.trado.co.il/api/admin-user/update"
        body = {"firstName":"salmonsalmon","lastName":"סלמון",
                "email":"dfgdfg@dsd.fs","phone":"dfsdf",
                "role":"delivery","permission":"read",
                "id":"4jp555dl4b2tieg"}
        res = requests.post(url, json=body)
        response = res.json()
        assert res.elapsed.total_seconds() < 10
        assert (response['status']) == 400

    def test_invalid_editing_role_is_null(self):
        url = "https://qa-api.trado.co.il/api/admin-user/update"
        body = {"firstName":"salmonsalmon","lastName":"סלמון",
                "email":"dfgdfg@dsd.fs","phone":"9513247812",
                "role":"","permission":"הרשאה",
                "id":"4jp555dl4b2tieg"}
        res = requests.post(url, json=body)
        response = res.json()
        assert res.elapsed.total_seconds() < 10
        assert (response['status']) == 400


    def test_invalid_editing_authorization_is_null(self):
        url = "https://qa-api.trado.co.il/api/admin-user/update"
        body = {"firstName":"salmonsalmon","lastName":"סלמון",
                "email":"dfgdfg@dsd.fs","phone":"9513247812",
                "role":"delivery","permission":"",
                "id":"4jp555dl4b2tieg"}
        res = requests.post(url, json=body)
        response = res.json()
        assert res.elapsed.total_seconds() < 10
        assert (response['status']) == 400

