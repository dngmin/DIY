import pandas as pd
import numpy as np

class management():

    def __init__(self,lang_code):
        self.lang_code = lang_code

    def add_txt(self):
        try:
            word_list = pd.read_csv(f'word_list\word_{self.lang_code}.csv')
            new_word_list = pd.read_csv(f'word_list\word_{self.lang_code}.txt',sep='\t')
            word_list.set_index('index',inplace=True)
            word_list = word_list.append(new_word_list)

            if self.lang_code == 'en':
                word_list = word_list.sort_values('word')
            elif self.lang_code == 'ja':
                word_list = word_list.sort_values('ふりがな')
            elif self.lang_code == 'ko':
                word_list = word_list.sort_values('단어')

            word_list = word_list.replace(np.NaN,0)
            
            if self.lang_code == 'en':
                word_list.drop_duplicates('word',keep='first',inplace=True)
            elif self.lang_code == 'ja':
                word_list.drop_duplicates('単語',keep='first',inplace=True)
            elif self.lang_code == 'ko':
                word_list.drop_duplicates('단어',keep='first',inplace=True)

            word_list.reset_index(drop=True,inplace=True)
            
            word_list.to_csv(f'word_list\word_{self.lang_code}.csv',encoding='utf-8-sig',index_label='index')
        except FileNotFoundError:
            if self.lang_code == 'en':
                print('FileNotFoundError : No such file or directory : word_en.txt')
            elif self.lang_code == 'ja':
                print('FileNotFoundError : 次のファイルが見つかりませんでした : word_ja.txt')
            elif self.lang_code == 'ko':
                print('FileNotFoundError : 다음 파일을 발견하지 못했습니다 : word_ko.txt')
    
    def add_fillout(self):
        try:
            word_list = pd.read_csv(f'word_list\word_{self.lang_code}.csv',index_col='index')
            if self.lang_code == 'en':
                new_word_list = run.new_word_list_en()
            elif self.lang_code == 'ja':
                new_word_list = run.new_word_list_ja()
            elif self.lang_code == 'ko':
                new_word_list = run.new_word_list_ko()
            else:
                raise ValueError
            stop = False

            if self.lang_code == 'en':
                while stop == False:
                    word = input('\nword : ')
                    new_word_list['word'].append(word)
                    new_word_list['pt'].append(0)
                    ask = input('input more word?\ny or n : ')
                    if ask == 'n':
                        stop = True
                    elif ask != 'y' and ask != 'n':
                        raise ValueError
            elif self.lang_code == 'ja':
                while stop == False:
                    word = input('\n単語 : ')
                    hurigana = input('\nふりがな [ひらがな] : ')
                    new_word_list['単語'].append(word)
                    new_word_list['ふりがな'].append(hurigana)
                    new_word_list['pt'].append(0)
                    ask = input('もっと追加しましか？\n y or n : ')
                    if ask == 'n':
                        stop = True
                    elif ask != 'y' and ask != 'n':
                        raise ValueError
            elif self.lang_code == 'ko':
                while stop == False:
                    word = input('\n단어 : ')
                    new_word_list['단어'].append(word)
                    new_word_list['pt'].append(0)
                    ask = input('계속해서 추가하시겠습니까？\n y or n : ')
                    if ask == 'n':
                        stop = True
                    elif ask != 'y' and ask != 'n':
                        raise ValueError
            
            new_word_list_Frame = pd.DataFrame(new_word_list)
            word_list = word_list.append(new_word_list_Frame,ignore_index=True)
            
            if self.lang_code == 'en':
                word_list = word_list.sort_values('word')
            elif self.lang_code == 'ja':
                word_list = word_list.sort_values('ふりがな')
            elif self.lang_code == 'ko':
                word_list = word_list.sort_values('단어')
            
            word_list.reset_index(drop=True,inplace=True)
            word_list.to_csv(f'word_list\word_{self.lang_code}.csv',encoding='utf-8-sig',index_label='index')

        except:
            print('\nError : Check your language code or word_xx.csv file is exist\n')

    def new_word_list_en(self):
        return {
            'word' : [],
            'pt' : []
        }

    def new_word_list_ja(self):
        return {
            '単語' : [],
            'ふりがな' : [],
            'pt' : []
        }

    def new_word_list_ko(self):
        return {
            '단어' : [],
            'pt' : []
        }

class LanguageCodeError(Exception):
    pass
class TorFError(Exception):
    # txt or fill out invalid error
    pass

try:
    print(' ♪ enter language code ♪\n')
    lang_code = input('[ English : en ]\n[ 日本語 : ja ]\n[ 한국어 : ko ]\n\nlanguage code : ')

    if lang_code == 'en':
        txt_or_fill = input('\n[txt file : 1]\n[fill out: 2]\n')
    elif lang_code == 'ja':
        txt_or_fill = input('\n[txtファイル :1]\n[自分で入力 : 2]\n')
    elif lang_code =='ko':
        txt_or_fill = input('\n[txt파일 : 1]\n[직접입력 : 2]\n')
    else:
        raise LanguageCodeError
    run = management(lang_code)
    
    if txt_or_fill == '1':
        add = run.add_txt()
    elif txt_or_fill == '2':
        add = run.add_fillout()
    else:
        raise TorFError
except LanguageCodeError:
    print('LanguageCodeError : LanguageCode is invalid')
except TorFError:
    print('ValueError : input 1 or 2')