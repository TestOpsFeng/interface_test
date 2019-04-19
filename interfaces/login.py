import requests
from utils.yaml_utils import get_api

login_url = get_api("login_url")
print(login_url)
data = {"usrAccount": "qvzn0123@163.com", "usrPassword": "Aa123456"}
response = requests.post(login_url, json=data)
token = response.json()['data']['token']

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Content-Type": "application/json;charset=UTF-8",
    "Authorization": token
}
