import yaml
import os

file_name = 'test_api.yaml'
fileNamePath = os.path.split(os.path.realpath(__file__))[0]
dir = os.path.join(fileNamePath,'../conf')

def get(file_name,*keys,file_path=dir):
    yamlPath = os.path.join(file_path, file_name)
    file = open(yamlPath, 'r', encoding='utf-8')
    config = yaml.safe_load(file)
    for key in keys:
        config = config[key]
    file.close()
    return config

def get_api(api,file_path=dir,file_name=file_name):
    yamlPath = os.path.join(file_path, file_name)
    file = open(yamlPath, 'r', encoding='utf-8')
    config = yaml.safe_load(file)
    config = config["host"] + config[api]
    file.close()
    return config

if __name__ == '__main__':
    driver2 = get_api("login_url")
    print(driver2)