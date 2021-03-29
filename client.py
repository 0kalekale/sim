import threading
import requests
import time


channel = "master" # example channel name
username = "0kalekale" # example username

print(chr(27) + "[2J")
def get_msg():
    while True:
        print(chr(27)+ "[2j")
        url = "http://127.0.0.1:5000/channel/" + channel

        get = requests.get(url)
        print(get.text)
        time.sleep(10)
        print(chr(27) + "[2J")

def __raw_get_msg():
    url = "http://127.0.0.1:5000/channel/" + channel

    get = requests.get(url)
    print(chr(27) + "[2j")
    print(get.text)
    
def send_msg():
    while True:
        msg = input("")
        url = "http://127.0.1:5000/msg?uname=" + username + "&msg=" + msg + "&channel=" + channel
        get = requests.get(url)
        print(chr(27) + "[2j")
        __raw_get_msg()

msg_t = threading.Thread(target=send_msg)
def main():

    msg_t.start()

    get_msg()

try:
    main()
except KeyboardInterrupt:
    exit()

