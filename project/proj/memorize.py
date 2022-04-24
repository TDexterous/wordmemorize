from clearprint import display_word, word_to_sound
from datetime import datetime
import random, sys, time, os, shutil

speech_text = {"start": "Welcome to Avengers word memorize game, press enter key to start.",
                   "howmany": "Specify, how many words you want to memorize?",
                   "try_again": "want to try it again?",
                   "press_key": "press y to restart game or press n to exit",
                   "your_turn": "Now its your turn, Enter those words in correct sequence with comma.",
                   "success": "CONGRATULATIONS! Kudos to You ! All Memorized Words Are Correct !",
                   "give_words": "Memorize below words with correct sequence which are being displayed",
                   "show_accuracy": "Your Accuracy is",
                   "correct_seq": "And correct sequence is",
                   "better_luck": "Sorry, Wrong Answer. Better Luck Next Time !",
                   "thanks": "Thank You ! Visit Again ..."}

color_dict = {
        # Foreground
        'F_Default' : "\x1b[39m", 'F_Black' : "\x1b[30m", 'F_Red' : "\x1b[31m",
        'F_Green ': "\x1b[32m", 'F_Yellow' : "\x1b[33m", 'F_Blue' : "\x1b[34m",
        'F_Magenta' : "\x1b[35m", 'F_Cyan' : "\x1b[36m", 'F_LightGray' : "\x1b[37m",
        'F_DarkGray' : "\x1b[90m", 'F_LightRed' : "\x1b[91m", 'F_LightGreen' : "\x1b[92m",
        'F_LightYellow' : "\x1b[93m", 'F_LightBlue' : "\x1b[94m", 'F_LightMagenta' : "\x1b[95m",
        'F_LightCyan' : "\x1b[96m", 'F_White' : "\x1b[97m",
        # Background
        'B_Default' : "\x1b[49m", 'B_Black' : "\x1b[40m", 'B_Red' : "\x1b[41m",
        'B_LightRed' : "\x1b[101m", 'B_Green' : "\x1b[42m", 'B_LightGreen' : "\x1b[102m", 
        'B_DarkGray' : "\x1b[100m", 'B_LightGray' : "\x1b[47m", 'B_Yellow' : "\x1b[43m",
        'B_LightYellow' : "\x1b[103m", 'B_Blue' : "\x1b[44m", 'B_LightBlue' : "\x1b[104m",
        'B_Magenta' : "\x1b[45m", 'B_LightMagenta' : "\x1b[105m", 'B_Cyan' : "\x1b[46m",
        'B_LightCyan' : "\x1b[106m", 'B_White' : "\x1b[107m" }


def match_word_list(system_list, user_list):
    if system_list == user_list:
        return 1, 0
    else:
        correct_words = []
        if len(system_list) == len(user_list):
            for i in range(len(system_list)):
                if system_list[i] == user_list[i]:
                    correct_words.append(system_list[i])
                else:
                    pass
            c = len(correct_words)
            return 0, c
        else:
            return 0, 0


def word_memorize_game():
    repeat = 1

    tday = datetime.now().strftime("%Y-%m-%d")
    try:
        shutil.rmtree(f"{tday}")
    except:
        pass 

    print("Welcome to 'Avengers Word Memorize Game'")
    word_to_sound(speech_text, 'start')
    a = input("Press Enter to start :")

    while repeat:
        
        try:
            shutil.rmtree(f"{tday}")
        except:
            pass   
        
        if a == '':
            WORDS = ('Loki', 'Captain', 'Ironman', 'Hulk', 'Thor', 'Tony', 'Vision', 'Panther', 'Spiderman' )
            word_count = 0
            word_to_sound(speech_text, 'howmany')  
            word_count = int(input("How many word you want to memorize ? :"))                      
            word_list = []
            word_to_sound(speech_text, 'give_words')
            print(f"Memorize below {word_count} words ")
            
            time.sleep(1)
            for sr in range(word_count):                
                word = random.choice(WORDS)
                display_word(word, int(sr)+1, last_word=0)
                word_list.append(word)
        

            display_word('Now its your turn !!!\n', sr, last_word=1)
            word_to_sound(speech_text, 'your_turn')

            word_input = input('Enter words in correct sequence with comma ( , ) :')
            entered_list = word_input.split(',')
            match, correct_words = match_word_list(word_list, entered_list)
            if match:
                print("---------------------------------------------------------------\n")
                print("################ *** Kudos to You ! *** ######################")
                print("########## All Memorized Words Are Correct ! #################")
                print("##############################################################")
                print("---------------------------------------------------------------\n")
                word_to_sound(speech_text, 'success')
                word_to_sound(speech_text, 'try_again')
                word_to_sound(speech_text, 'press_key')
                res = input("Want to try it again (y/n)? :")
                if res == 'y':
                    repeat=1
                else:
                    word_to_sound(speech_text, 'thanks')
                    print("Thank You ! Visit Again ...")
                    break
            else:
                word_to_sound(speech_text, 'better_luck')
                print("##### Better Luck Next Time ! #####\n")
                word_to_sound(speech_text, 'correct_seq')
                print(f"Correct Answer: ")
                for sr, word in enumerate(word_list, start=1):
                    print(f"\t{sr}]{word}")
                print("=================================\n")
                word_to_sound(speech_text, 'try_again')
                word_to_sound(speech_text, 'press_key')
                res = input("Want to try it again (y/n)? :")

                if res == 'y':
                    repeat=1
                else:
                    break
        

word_memorize_game()
word_to_sound(speech_text, 'thanks')
print("Thank You ! Visit Again ...")