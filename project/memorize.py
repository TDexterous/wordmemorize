def match_word_list(system_list, user_list):
    if system_list == user_list:
        return 1
    else:
        return 0


def word_memorize_game(repeat):
    while repeat:
        a = input("Press [Enter] key to start 'Word Memorize Game':")
        if a == '':
            WORDS = ("python", "jumble", "easy", "difficult", "answer", "phone", "success", "food", "cricket",
                        "correct", 'house', "building", "mixer", "foot", "ground", "hall", "school", "teacher", "fish")
            word_count = int(input("How many word you want to memorize ? :"))
            word_list = []
            while word_count:
                print(f"Memorize below {word_count} words ")
                time.sleep(1)
                for sr, word_sr in enumerate(range(word_count), start=1):
                    if word_count:
                        word = random.choice(WORDS)
                        display_word(word, sr, last_word=0)
                        word_list.append(word)
                        word_count = -1
                display_word('Now its your turn !!!\n', sr, last_word=1)

                word_input = input('Enter words in correct sequence with comma ( , ) :')
                entered_list = word_input.split(',')
                if match_word_list(word_list, entered_list):
                    print("################ *** Kudos to You ! *** ######################")
                    print("########## All Memorized Words Are Correct ! #################")
                    print("##############################################################")
                    print("---------------------------------------------------------------\n")
                    res = input("Want to try it again (y/n)? :")
                    if res == 'y':
                        word_memorize_game(True)
                    else:
                        sys.exit("Thank You ! Visit Again ...")
                else:
                    print("##### Better Luck Next Time ! #####")
                    print(f"Correct Word Sequence is {word_list}")
                    print("-------------------------------------------------------------------------\n")

                    res = input("Want to try it again (y/n)? :")
                    if res == 'y':
                        word_memorize_game(True)
                    else:
                        sys.exit("Thank You ! Visit Again ...")

word_memorize_game(True)





