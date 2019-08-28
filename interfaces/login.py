import requests
from utils.yaml_utils import get_config
#
# login_url = get_api("login_url")
# print("login_url: " + login_url)
# data = {"usrAccount": "qvzn0123@163.com", "usrPassword": "123321"}
# response = requests.post(login_url, json=data)
# token = response.json()['data']['token']
# print('token:',token)
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
#     "Accept-Encoding": "gzip, deflate",
#     "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
#     "Content-Type": "application/json;charset=UTF-8",
#     "Authorization": token
# }

proxies = { "http": "http://"+get_config("proxy")+"", "https": "http://"+get_config("proxy")+"", }

host = get_config('host')
login_url= host + "/supersell/rest/login/auth"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "Referer":""+host+"/en/login/"
}
body = "username=" +get_config("username")+ "&password="+get_config("password")+""

response = requests.post(login_url, data=body,verify=False,proxies=proxies,headers=headers)
print(response.text)
if response.status_code==200:
    bs_token = response.json()['data']['bsInfo']['token']
    print('bs_token:',bs_token)