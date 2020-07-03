import json
import requests
import time

print("Запуск")

with open("config.json", "r") as config:
    config = json.loads(config.read())

session = requests.Session()

def main(audio, access_token=config['access_token'], v='5.120'):
    session.get(f"https://api.vk.com/method/audio.setBroadcast?audio={audio}&access_token={access_token}&v={v}")
    time.sleep(60) # Обновление статуса каждую минуту

while True:
    main(config['audio'])
