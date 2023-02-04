import os.path
from pushbullet import Pushbullet
import json
import time
import sys


def importar_profile():
    with open('profile.json') as profile_json:
        profile = json.load(profile_json)
        profile_json.close()
    return profile


def timestamp():
    return time.strftime('%H:%M:%S')


def snap_timestamp():
    return time.strftime('%d-%m-%y__%H-%M-%S')

##################


perfil = importar_profile()
limite = 'ativado: $%d' % perfil['price_limit'] if perfil['price_limit'] > 0.0 else 'desativado (express)'
##################


def printin(text):
    print(f"\r|{timestamp()}| Limite de valor {limite} | {text}", end='\r')


def printc(text):
    print("|{0}| {1}".format(timestamp(), text))


def inputc(text):
    input("|{0}| {1}".format(timestamp(), text))


def print_flush(content):
    sys.stdout.write(content)
    sys.stdout.flush()


def log_print(content):
    if not os.path.isdir("logs"):
        os.mkdir("logs")
    with open(f'logs\\{time.strftime("%d-%m-%y")}.log', 'a', encoding="utf-8") as logging:
        print(content)
        logging.write(content)
        logging.close()


def empty_method():
    pass


def save_source(page):
    with open(f'page_source/{snap_timestamp()}_page.html', 'w') as f:
        f.write(page.page_source)
        f.close()


def send_push(msg):
    api_key = ""
    pb = Pushbullet(api_key)
    pb.push_note('NEW JOB!',
                 f'{msg}.')
