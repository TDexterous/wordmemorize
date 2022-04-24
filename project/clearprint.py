from datetime import datetime
import time


def clock():
    while True:
        print('\r', datetime.now().strftime("%H:%M:%S"), end='')
        time.sleep(1)

# clock()


def display_word(word, sr, last_word):
    if last_word:
        print('\r', word, end='')
    else:
        print('\r', f"{sr}# word:" + word, end='')
    time.sleep(2)