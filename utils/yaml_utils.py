import yaml
import os

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

def get_config(*keys,file_path=dir):
    yamlPath = os.path.join(file_path,  'config.yaml')
    file = open(yamlPath, 'r', encoding='utf-8')
    config = yaml.safe_load(file)
    for key in keys:
        config = config[key]
    file.close()
    return config

if __name__ == '__main__':
    driver2 = get_config("host")
    print(driver2)