from playsound import playsound
from gtts import gTTS
from datetime import datetime
import time, os, shutil


def list_compare(a, b):
    correct_words=[]
    for i in range(len(a)):
        if a[i] == b[i]:
            print(a[i])
            correct_words.append(a[i])
            print(correct_words)
        else:
            pass

# list_compare(['aa','bb','ee','ff', 'gg'], ['aa','bb','cc','dd','ee'])

def word_to_sound(text_dict, mp3_key):
    tday = datetime.now().strftime("%Y-%m-%d")
    os.mkdir(f'{tday}')
    os.chdir(f'{tday}')
    text_str2 = gTTS(text_dict[mp3_key])
    text_str2.save(f"{mp3_key}.mp3")
    playsound(f"{mp3_key}.mp3")

def display_word(word, sr, last_word):
    if last_word:
        print('\r', word, end='')
    else:
        print('\r', f"{sr}# word:" + word, end='')
    time.sleep(2)

def display_word2(word, sr, last_word):
    if last_word:
        print('\r', word, end='')
    else:
        print('\r', f"{sr}# word:" + word, end='')
    time.sleep(2)