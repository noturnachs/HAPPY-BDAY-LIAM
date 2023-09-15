import os


def init():
    global script, delay, iterations
    script = os.getcwd() + "\script.txt"
    delay = 1.00
    iterations = 10


init()
