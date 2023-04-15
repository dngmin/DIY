import pandas as pd
import random

class siritori():
    def __init__(self,lang_code,do_first,gameover=False):
        self.lang_code = lang_code
        self.do_first = do_first
        self.gameover = gameover
    
    def player(self):
        if self.lang_code == 'en':
            run.play_in_en()
        elif self.lang_code == 'ja':
            run.play_in_ja()
        elif self.lang_code == 'ko':
            run.play_in_ko()

    def play_in_en(self):
        word_list = pd.read_csv(f'word_list\word_{self.lang_code}.csv',index_col='index')
        com = ''
        me = ''

        while self.gameover == False:
            answer_list = []
            me = input()
            
            for index in range(0,len(word_list)):
                if word_list['word'][index][0] == me[-1]:
                    answer_list.append(index)
            
            if len(answer_list) == 0:
                raise YouWontheRobot
            else:
                com = random.choice(answer_list)
                print(f"↓\n{word_list['word'][com]}\n↓")
                me = input()
                if me[0] != word_list['word'][com][-1]:
                    print('cheater')
                    raise Youlose
                word_list.drop(com,inplace=True)
                word_list.sort_values('word',inplace=True)
                word_list.reset_index(drop=True,inplace=True)



    def play_in_ja(self):
        # word_list = pd.read_csv(f'word_list\word_{self.lang_code}.csv',index_col='index')
        # com = ''
        # me = ''

        # while self.gameover == False:
        #     answer_list = []
        #     me = input()
            
        #     for index in range(0,len(word_list)):
        #         if word_list['word'][index][0] == me[-1]:
        #             answer_list.append(index)
            
        #     if len(answer_list) == 0:
        #         raise YouWontheRobot
        #     else:
        #         com = random.choice(answer_list)
        #         print(f"↓\n{word_list['word'][com]}\n↓")
        #         word_list.drop(com,inplace=True)
        #         word_list.sort_values('word',inplace=True)
        #         word_list.reset_index(drop=True,inplace=True)
        print('*** 構造中 ***')
    
    def play_in_ko(self):
        word_list = pd.read_csv(f'word_list\word_{self.lang_code}.csv',index_col='index')
        com = ''
        me = input()

        while self.gameover == False:
            answer_list = []
            
            for index in range(0,len(word_list)):
                if word_list['단어'][index][0] == me[-1]:
                    answer_list.append(index)
            
            if len(answer_list) == 0:
                raise YouWontheRobot
            else:
                com = random.choice(answer_list)
                print(f"↓\n{word_list['단어'][com]}\n↓")
                me = input()
                if me[0] != word_list['단어'][com][-1]:
                    print('cheater')
                    raise Youlose
                word_list.drop(com,inplace=True)
                word_list.sort_values('단어',inplace=True)
                word_list.reset_index(drop=True,inplace=True)


class LanguageCodeError(Exception):
    pass
class FoLError(Exception):
    pass
class YouWontheRobot(Exception):
    pass
class Youlose(Exception):
    pass
class Timeoverlosing(Exception):
    pass

try:
    print('\n ♪ しりとりゲームをしましょう ♪\n')
    print(' ♪ enter language code ♪\n')
    lang_code = input('[ English : en ]\n[ 日本語 : ja ]\n[ 한국어 : ko ]\n\nlanguage code : ')

    # if lang_code == 'en':
    #     first_or_later = input('\n[go first : 1]\n[let go first: 2]\n')
    # elif lang_code == 'ja':
    #     first_or_later = input('\n[自分からスタート :1]\n[コンピュータからスタート : 2]\n')
    # elif lang_code =='ko':
    #     first_or_later = input('\n[나부터 시작 : 1]\n[컴퓨터부터 시작 : 2]\n')
    # else:
    #     raise LanguageCodeError
    
    # if first_or_later == '1':
    #     do_first = True
    # elif first_or_later == '2':
    #     do_first = False
    # else:
    #     raise FoLError

    do_first = 0

    run = siritori(lang_code,do_first)
    play = run.player()

except LanguageCodeError:
    print('LanguageCodeError : LanguageCode is invalid')
except FoLError:
    print('ValueError : input 1 or 2')
except YouWontheRobot:
    print('\nGG\nYou won the siritori robot!!')
except Youlose:
    print('\nYou Lose　(´；ω；`)')