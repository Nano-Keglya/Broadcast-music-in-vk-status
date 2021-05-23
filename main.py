import json, requests, time

print("Запуск")

with open("config.json", "r") as config:
    config = json.loads(config.read())

session = requests.Session()

def main(audio=config['audio'], access_token=config['access_token'], v='5.131'):
    session.get(f"https://api.vk.com/method/audio.setBroadcast?audio={audio}&access_token={access_token}&v={v}")
    time.sleep(60) # Обновление статуса каждую минуту (желательно выставить время музыки)

while True:
    main()
