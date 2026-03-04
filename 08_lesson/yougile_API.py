import requests

base_url = 'https://yougile.com/api-v2'
token = ''


class YouGileAPI:

    def __init__(self):
        self.base_url = base_url
        self.token = token
        self.headers = {'Authorization': f'Bearer {self.token}'}

    def create_project(self, title):
        body = {'title': title}
        resp = requests.post(self.base_url + '/projects',
                             headers=self.headers, json=body)
        return resp

    def update_project(self, project_id, title):
        body = {'title': title}
        resp = requests.put(self.base_url + '/projects/' + (str(project_id)),
                            headers=self.headers, json=body)
        return resp

    def get_project(self, project_id):
        resp = requests.get(self.base_url + '/projects/' + (str(project_id)),
                            headers=self.headers)
        return resp
