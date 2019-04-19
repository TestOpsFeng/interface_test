import os
import logging.config
import yaml


log_path = os.path.split(os.path.realpath(__file__))[0] + '/../conf/logger_config.yaml'

def setup_logging(default_path = log_path,default_level = logging.INFO):
    print(log_path)
    path = default_path
    if os.path.exists(path):
        with open(path, "r") as f:
            config = yaml.safe_load(f)
            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


logger = logging.getLogger('info')
logger.error('Faild to get result', exc_info=True)
setup_logging()