import requests
import time
import shutil
import os

class Wombo:
    def __init__(self):
        self.secret = "AIzaSyDCvp5MTJLUdtBYEKYWXJrlLzu1zuKM6Xw"
        self.wombo_api = 'https://paint.api.wombo.ai/api/tasks/'
        self.token = None
        self.id = None
        self.url = None

    def get_auth_token(self):
        print('getting auth token')
        # POST to /v1/accounts:signUp?key=AIzaSyDCvp5MTJLUdtBYEKYWXJrlLzu1zuKM6Xw
        # payload {returnSecureToken: true}
        # self.token = response.idToken
        token_server = 'https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=AIzaSyDCvp5MTJLUdtBYEKYWXJrlLzu1zuKM6Xw'
        r = requests.post(token_server, data={"returnSecureToken":True})
        res = r.json()
        print('received response', res)
        print('id token acquired', res['idToken'])
        self.token = res['idToken']

    def get_task_id(self):
        print('generating task id')
        # POST request to api
        token_string = "Bearer " + self.token
        headers = {"Authorization": token_string}
        r = requests.post(self.wombo_api, data='{"premium":false}', headers=headers)
        res = r.json()
        print('received response', res)
        self.id = res['id']

    def enqueue_job(self, prompt, style):
        print('enqueueing task')
        # PUT to task ID URL with prompt
        data_template = '{"input_spec":{"prompt":"' + prompt + '","style":' + str(style) + ',"display_freq":10}}'
        token_string = "Bearer " + self.token
        headers = {"Authorization": token_string}
        r = requests.put(self.wombo_api + self.id, data=data_template, headers=headers)
        res = r.json()
        print('received response', res)

    def get_result(self):
        print('attempting to get result')
        # GET request to task ID URL
        token_string = "Bearer " + self.token
        headers = {"Authorization": token_string}
        r = requests.get(self.wombo_api + self.id, headers=headers)
        res = r.json()
        print('received response', res)

        if res['state'] == 'completed':
            self.url = res['result']['final']
        else:
            print('not completed - waiting 3s')
            time.sleep(3)
            self.get_result()

    def generate(self, prompt, style):
        self.get_auth_token()
        self.get_task_id()
        self.enqueue_job(prompt, style)

        time.sleep(5)
        self.get_result()

        return self.url

    def download_image(self):
        # hit url, store in file system
        filename = 'raw.jpg'
        r = requests.get(self.url, stream = True)
        if r.status_code == 200:
            r.raw.decode_content = True
            with open(filename, 'wb') as f:
                shutil.copyfileobj(r.raw, f)

            print('Image downloaded and stored')
        else:
            print('something bad happened')
            print(r.raw)
