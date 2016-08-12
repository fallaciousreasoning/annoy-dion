import requests
import random
import time

min_sleep = 0.1
max_sleep = 5

url = 'http://harest.makereti.co.nz:9834/api/'
body = {'complete':True}

def annoy():
    move_down = True

    while True:
        down() if move_down else up()

        t = random.random() * (max_sleep - min_sleep) + min_sleep
        time.sleep(t)

        stop()

        move_down = not move_down

def up():
    u = url + 'up'

    r = requests.post(u, json=body)

    print('going up')

def down():
    u = url + 'down' 

    r = requests.post(u, json=body)

    print('going down')

def stop():
    u = url + 'abort'

    r = requests.get(u)

    print('stopping')

if __name__ == '__main__':
    annoy()