import requests
import random
import time, datetime

def log(text):
    timestamp = datetime.datetime.utcfromtimestamp(time.time()).strftime("%H:%M:%S")
    print(f"[{timestamp}] {text}")

def check_name(session, name):
    if len(name) >= 5:
        response = session.get(f"https://tise.com/{name}")
        if '"@context":"http://schema.org"' not in str(response.content): log(f"`{name}` is available")
        elif response.status_code == 429:
            log("Ratelimited, waiting 60s")
            time.sleep(60)
    else: pass

with open("useragents.txt", "r") as file:
    useragents = file.read().splitlines()

with open("words.txt", "r") as file:
    word_list = file.read().splitlines()

with requests.Session() as session:
    for word in word_list:
        useragent = random.choice(useragents)
        session.headers.update({"User-Agent": useragent})
        check_name(session, word)
