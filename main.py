from importlib import reload
from pickle import NONE
from sqlite3 import Time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import telebot
import time
import bd

# Por informações do seu bot.########
api_key = 'ID PRIVADO'  # TOKEN DO BOT
chat_id = '1103938119'  # ID DO CHAT PV
#####################################
bot = telebot.TeleBot(token=api_key)

bot.send_message(chat_id=chat_id, text=''' Bora Clã! O bot está on!! ''')

options = webdriver.ChromeOptions()
options.add_argument('--headless')
nav = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), chrome_options=options)

nav.get('https://blaze.com/pt/games/double')


def qualnum(x):
    if x == '0':
        return 0

    if x == '1':
        return 1

    if x == '2':
        return 2

    if x == '3':
        return 3

    if x == '4':
        return 4

    if x == '5':
        return 5

    if x == '6':
        return 6

    if x == '7':
        return 7

    if x == '8':
        return 8

    if x == '9':
        return 9

    if x == '10':
        return 10

    if x == '11':
        return 11

    if x == '12':
        return 12

    if x == '13':
        return 13

    if x == '14':
        return 14


def qualcor(x):
    if x == '0':
        return 'B'

    if x == '1':
        return 'V'

    if x == '2':
        return 'V'

    if x == '3':
        return 'V'

    if x == '4':
        return 'V'

    if x == '5':
        return 'V'

    if x == '6':
        return 'V'

    if x == '7':
        return 'V'

    if x == '8':
        return 'P'

    if x == '9':
        return 'P'

    if x == '10':
        return 'P'

    if x == '11':
        return 'P'

    if x == '12':
        return 'P'

    if x == '13':
        return 'P'

    if x == '14':
        return 'P'


def reset():
    bd.estrategy_name = 'TRUE'
    bd.direction_color = 'NULL'
    bd.analisar = 0
    bd.gale_atual = 0


def martingales():
    def very_gale(num):
        if num[0:1] == [0]:
            if bd.gale_atual == 0:
                bot.send_message(chat_id=chat_id, text='''
                ⚪ BRANCO SEM GALE ⚪
                            ''')
                bd.brancos += 1
                bd.total_win += 1
                if bd.loss == 0:
                    bd.porcentagem = 100 
                bd.b = bd.win_Sg + bd.brancos + bd.win_g1 + bd.win_g2
                if (bd.win_Sg + bd.brancos + bd.win_g1 + bd.win_g2 + bd.loss) !=0:
                    bd.a = 100/(bd.win_Sg + bd.brancos + bd.win_g1 + bd.win_g2 + bd.loss) * bd.b
                else:
                    bd.a = 0
                bd.porcentagem = (f'{bd.a:,.2f}%')
                bot.send_message(chat_id=chat_id, text=f'''
📌 Estátisticas: 

✅ Win S/Gale:  {bd.win_Sg}   
✅ Win Gale 1:  {bd.win_g1}
✅ Win Gale 2:  {bd.win_g2}
⬜ Brancos:  {bd.brancos}   

✅ Wins Total:  {bd.total_win}
❌ Loss:  {bd.loss}   

✔ Assertividade: {bd.porcentagem}

                ''')
                reset()
                return

            if bd.gale_atual == 1:
                bot.send_message(chat_id=chat_id, text='''
                ⚪BRANCO 1ª GALE ⚪
                            ''')
                bd.brancos += 1
                bd.total_win += 1
                bd.b = bd.win_Sg + bd.brancos + bd.win_g1 + bd.win_g2
                if (bd.win_Sg + bd.brancos + bd.win_g1 + bd.win_g2 + bd.loss) !=0:
                    bd.a = 100/(bd.win_Sg + bd.brancos + bd.win_g1 + bd.win_g2 + bd.loss) * bd.b
                else:
                    bd.a = 0
                bd.porcentagem = (f'{bd.a:,.2f}%')
                bot.send_message(chat_id=chat_id, text=f'''
📌 Estátisticas: 

✅ Win S/Gale:  {bd.win_Sg}   
✅ Win Gale 1:  {bd.win_g1}
✅ Win Gale 2:  {bd.win_g2}
⬜ Brancos:  {bd.brancos}   

✅ Wins Total:  {bd.total_win}
❌ Loss:  {bd.loss}   

✔ Assertividade: {bd.porcentagem}

                ''')
                reset()
                return

            if bd.gale_atual == 2:
                bot.send_message(chat_id=chat_id, text='''
                ⚪ BRANCO 2ªGALE ⚪
                            ''')
                bd.brancos += 1
                bd.total_win += 1
                bd.b = bd.win_Sg + bd.brancos + bd.win_g1 + bd.win_g2
                if (bd.win_Sg + bd.brancos + bd.win_g1 + bd.win_g2 + bd.loss) !=0:
                    bd.a = 100/(bd.win_Sg + bd.brancos + bd.win_g1 + bd.win_g2 + bd.loss) * bd.b
                else:
                    bd.a = 0
                bd.porcentagem = (f'{bd.a:,.2f}%')
                bot.send_message(chat_id=chat_id, text=f'''
📌 Estátisticas: 

✅ Win S/Gale:  {bd.win_Sg}   
✅ Win Gale 1:  {bd.win_g1}
✅ Win Gale 2:  {bd.win_g2}
⬜ Brancos:  {bd.brancos}   

✅ Wins Total:  {bd.total_win}
❌ Loss:  {bd.loss}   

✔ Assertividade: {bd.porcentagem}

                ''')
                reset()
                return

        if num[0:1] > [0] and num[0:1] <= [7] and bd.direction_color == '🟥':
            if bd.gale_atual == 0:
                bot.send_message(chat_id=chat_id, text='''
                🟢 WIN SEM GALE 🟢
                 
                            ''')
                bd.win_Sg += 1
                bd.total_win += 1
                bd.b = bd.win_Sg + bd.brancos + bd.win_g1 + bd.win_g2
                if (bd.win_Sg + bd.brancos + bd.win_g1 + bd.win_g2 + bd.loss) !=0:
                    bd.a = 100/(bd.win_Sg + bd.brancos + bd.win_g1 + bd.win_g2 + bd.loss) * bd.b
                else:
                    bd.a = 0
                bd.porcentagem = (f'{bd.a:,.2f}%')
                bot.send_message(chat_id=chat_id, text=f'''
📌 Estátisticas: 

✅ Win S/Gale:  {bd.win_Sg}   
✅ Win Gale 1:  {bd.win_g1}
✅ Win Gale 2:  {bd.win_g2}
⬜ Brancos:  {bd.brancos}   

✅ Wins Total:  {bd.total_win}
❌ Loss:  {bd.loss}   

✔ Assertividade: {bd.porcentagem}

                ''')
                reset()
                return

            if bd.gale_atual == 1:
                bot.send_message(chat_id=chat_id, text='''
                🟢 WIN 1ª GALE  🟢
                 
                            ''')
                bd.win_g1 += 1
                bd.total_win += 1
                bd.b = bd.win_Sg + bd.brancos + bd.win_g1 + bd.win_g2
                if (bd.win_Sg + bd.brancos + bd.win_g1 + bd.win_g2 + bd.loss) !=0:
                    bd.a = 100/(bd.win_Sg + bd.brancos + bd.win_g1 + bd.win_g2 + bd.loss) * bd.b
                else:
                    bd.a = 0
                bd.porcentagem = (f'{bd.a:,.2f}%')
                bot.send_message(chat_id=chat_id, text=f'''
📌 Estátisticas: 

✅ Win S/Gale:  {bd.win_Sg}   
✅ Win Gale 1:  {bd.win_g1}
✅ Win Gale 2:  {bd.win_g2}
⬜ Brancos:  {bd.brancos}   

✅ Wins Total:  {bd.total_win}
❌ Loss:  {bd.loss}   

✔ Assertividade: {bd.porcentagem}

                ''')
                reset()
                return

            if bd.gale_atual == 2:
                bot.send_message(chat_id=chat_id, text='''
                🟢 WIN 2ªGALE 🟢
                 
                            ''')
                bd.win_g2 += 1
                bd.total_win += 1
                bd.b = bd.win_Sg + bd.brancos + bd.win_g1 + bd.win_g2
                if (bd.win_Sg + bd.brancos + bd.win_g1 + bd.win_g2 + bd.loss) !=0:
                    bd.a = 100/(bd.win_Sg + bd.brancos + bd.win_g1 + bd.win_g2 + bd.loss) * bd.b
                else:
                    bd.a = 0
                bd.porcentagem = (f'{bd.a:,.2f}%')
                bot.send_message(chat_id=chat_id, text=f'''
📌 Estátisticas: 

✅ Win S/Gale:  {bd.win_Sg}   
✅ Win Gale 1:  {bd.win_g1}
✅ Win Gale 2:  {bd.win_g2}
⬜ Brancos:  {bd.brancos}   

✅ Wins Total:  {bd.total_win}
❌ Loss:  {bd.loss}   

✔ Assertividade: {bd.porcentagem}

                ''')
                reset()
                return

        if num[0:1] >= [8] and num[0:1] <= [14] and bd.direction_color == '⬛️':
            if bd.gale_atual == 0:
                bot.send_message(chat_id=chat_id, text='''
                🟢 WIN SEM GALE 🟢
                 
                            ''')
                bd.win_Sg += 1
                bd.total_win += 1
                bd.b = bd.win_Sg + bd.brancos + bd.win_g1 + bd.win_g2
                if (bd.win_Sg + bd.brancos + bd.win_g1 + bd.win_g2 + bd.loss) !=0:
                    bd.a = 100/(bd.win_Sg + bd.brancos + bd.win_g1 + bd.win_g2 + bd.loss) * bd.b
                else:
                    bd.a = 0
                bd.porcentagem = (f'{bd.a:,.2f}%')
                bot.send_message(chat_id=chat_id, text=f'''
📌 Estátisticas: 

✅ Win S/Gale:  {bd.win_Sg}   
✅ Win Gale 1:  {bd.win_g1}
✅ Win Gale 2:  {bd.win_g2}
⬜ Brancos:  {bd.brancos}   

✅ Wins Total:  {bd.total_win}
❌ Loss:  {bd.loss}   

✔ Assertividade: {bd.porcentagem}

                ''')
                reset()
                return

            if bd.gale_atual == 1:
                bot.send_message(chat_id=chat_id, text='''
                🟢 WIN 1ª GALE 🟢
                 
                            ''')
                bd.win_g1 += 1
                bd.total_win += 1
                bd.b = bd.win_Sg + bd.brancos + bd.win_g1 + bd.win_g2
                if (bd.win_Sg + bd.brancos + bd.win_g1 + bd.win_g2 + bd.loss) !=0:
                    bd.a = 100/(bd.win_Sg + bd.brancos + bd.win_g1 + bd.win_g2 + bd.loss) * bd.b
                else:
                    bd.a = 0
                bd.porcentagem = (f'{bd.a:,.2f}%')
                bot.send_message(chat_id=chat_id, text=f'''
📌 Estátisticas: 

✅ Win S/Gale:  {bd.win_Sg}   
✅ Win Gale 1:  {bd.win_g1}
✅ Win Gale 2:  {bd.win_g2}
⬜ Brancos:  {bd.brancos}   

✅ Wins Total:  {bd.total_win}
❌ Loss:  {bd.loss}   

✔ Assertividade: {bd.porcentagem}

                ''')
                reset()
                return

            if bd.gale_atual == 2:
                bot.send_message(chat_id=chat_id, text='''
                🟢 WIN 2ªGALE 🟢
                            ''')
               

                bd.win_g2 += 1
                bd.total_win += 1
                bd.b = bd.win_Sg + bd.brancos + bd.win_g1 + bd.win_g2
                if (bd.win_Sg + bd.brancos + bd.win_g1 + bd.win_g2 + bd.loss) !=0:
                    bd.a = 100/(bd.win_Sg + bd.brancos + bd.win_g1 + bd.win_g2 + bd.loss) * bd.b
                else:
                    bd.a = 0
                bd.porcentagem = (f'{bd.a:,.2f}%')
                bot.send_message(chat_id=chat_id, text=f'''
📌 Estátisticas: 

✅ Win S/Gale:  {bd.win_Sg}   
✅ Win Gale 1:  {bd.win_g1}
✅ Win Gale 2:  {bd.win_g2}
⬜ Brancos:  {bd.brancos}   

✅ Wins Total:  {bd.total_win}
❌ Loss:  {bd.loss}   

✔ Assertividade: {bd.porcentagem}

                ''')
                reset()
                return

        if num[0:1] >= [8] and num[0:1] <= [14] and bd.direction_color == '🟥':
            if bd.gale_atual == 0:
                bd.gale_atual += 1
                print('Vamos pro gale 1')
                return

            if bd.gale_atual == 1:
                bd.gale_atual += 1
                print('Vamos pro gale 2')
                return

            if bd.gale_atual == 2:
                bot.send_message(chat_id=chat_id, text='''
                LOSS ❌❌❌
                            ''')
                bd.loss += 1
                bd.total_win += 1
                bd.b = bd.win_Sg + bd.brancos + bd.win_g1 + bd.win_g2
                if (bd.win_Sg + bd.brancos + bd.win_g1 + bd.win_g2 + bd.loss) !=0:
                    bd.a = 100/(bd.win_Sg + bd.brancos + bd.win_g1 + bd.win_g2 + bd.loss) * bd.b
                else:
                    bd.a = 0
                bd.porcentagem = (f'{bd.a:,.2f}%')
                bot.send_message(chat_id=chat_id, text=f'''
📌 Estátisticas: 

✅ Win S/Gale:  {bd.win_Sg}   
✅ Win Gale 1:  {bd.win_g1}
✅ Win Gale 2:  {bd.win_g2}
⬜ Brancos:  {bd.brancos}   

✅ Wins Total:  {bd.total_win}
❌ Loss:  {bd.loss}   

✔ Assertividade: {bd.porcentagem}

                ''')
                reset()
                return

        if num[0:1] > [0] and num[0:1] <= [7] and bd.direction_color == '⬛️':
            if bd.gale_atual == 0:
                bd.gale_atual += 1
                print('Vamos pro gale 1')
                return

            if bd.gale_atual == 1:
                bd.gale_atual += 1
                print('Vamos pro gale 2')
                return

            if bd.gale_atual == 2:
                bot.send_message(chat_id=chat_id, text='''
                LOSS ❌❌❌
                            ''')
                bd.loss += 1
                bd.total_win += 1
                bd.b = bd.win_Sg + bd.brancos + bd.win_g1 + bd.win_g2
                if (bd.win_Sg + bd.brancos + bd.win_g1 + bd.win_g2 + bd.loss) !=0:
                    bd.a = 100/(bd.win_Sg + bd.brancos + bd.win_g1 + bd.win_g2 + bd.loss) * bd.b
                else:
                    bd.a = 0
                bd.porcentagem = (f'{bd.a:,.2f}%')
                bot.send_message(chat_id=chat_id, text=f'''
📌 Estátisticas: 

✅ Win S/Gale:  {bd.win_Sg}   
✅ Win Gale 1:  {bd.win_g1}
✅ Win Gale 2:  {bd.win_g2}
⬜ Brancos:  {bd.brancos}   

✅ Wins Total:  {bd.total_win}
❌ Loss:  {bd.loss}   

✔ Assertividade: {bd.porcentagem}

                ''')
                reset()
                return
    very_gale(bd.finalnum)
    return


while True:
    try:
        resulROOL = nav.find_element(
            By.XPATH, '//*[@id="roulette-timer"]/div[1]').text
    except NameError as erro:
        continue
    except Exception as erro:
        continue

    if resulROOL == 'Girando...':
        bd.analisar_open = 1

        print('Analisando')
        time.sleep(13)
        c = nav.page_source
        bd.resultsDouble.clear()

        soup = BeautifulSoup(c, 'html.parser')
        go = soup.find('div', class_="entries main")
        for i in go:
            if i.getText():
                bd.resultsDouble.append(i.getText())
            else:
                bd.resultsDouble.append('0')

        bd.resultsDouble = bd.resultsDouble[:-1]

        if bd.analisar_open == 1:

            default = bd.resultsDouble[0:14]

            mapeando = map(qualnum, default)
            mapeando2 = map(qualcor, default)
            bd.finalnum = list(mapeando)
            bd.finalcor = list(mapeando2)

        if bd.estrategy_name == 'TRUE' or bd.estrategy_name == 'MOD01':
            def CHECK_VERSION(num):

                if bd.analisar == 0:
                    if num[0:3] == ['V', 'V', 'P']:
                        bd.estrategy_name = 'MOD01'
                        bd.direction_color = '⬛️'
                        bd.analisar = 1
                        bot.send_message(chat_id=chat_id, text='''
            PADRÃO %s
‼️ Atenção ‼️
Entrada confirmada

Entra no ⚫⚫⚫
Defesa   ⚪⚪⚪                       
                        ''' % (bd.estrategy_name))
                        return
                    if num[0:3] == ['P', 'P', 'V']:
                        bd.estrategy_name = 'MOD01'
                        bd.direction_color = '🟥'
                        bd.analisar = 1
                        bot.send_message(chat_id=chat_id, text='''
            PADRÃO %s 
‼️ Atenção ‼️
Entrada confirmada

Entra no 🔴🔴🔴
Defesa   ⚪⚪⚪
                        ''' % (bd.estrategy_name))
                        return

                elif bd.analisar == 1:
                    martingales()
                    return

            CHECK_VERSION(bd.finalcor)

        if bd.estrategy_name == 'TRUE' or bd.estrategy_name == 'MOD02':

            def CHECK_VERSION(num):

                if bd.analisar == 0:
                    if num[0:3] == ['P', 'V', 'P']:
                        bd.estrategy_name = 'MOD02'
                        bd.direction_color = '⬛️'
                        bd.analisar = 1
                        bot.send_message(chat_id=chat_id, text='''
            PADRÃO %s 
‼️ Atenção ‼️
Entrada confirmada

Entra no ⚫⚫⚫
Defesa   ⚪⚪⚪                       
                        ''' % (bd.estrategy_name))
                        return
                    if num[0:3] == ['V', 'P', 'V']:
                        bd.estrategy_name = 'MOD02'
                        bd.direction_color = '🟥'
                        bd.analisar = 1
                        bot.send_message(chat_id=chat_id, text='''
            PADRÃO %s
‼️ Atenção ‼️
Entrada confirmada

Entra no 🔴🔴🔴
Defesa   ⚪⚪⚪
                        ''' % (bd.estrategy_name))
                        return

                elif bd.analisar == 1:
                    martingales()
                    return

            CHECK_VERSION(bd.finalcor)

        if bd.estrategy_name == 'TRUE' or bd.estrategy_name == 'MOD03':

            def CHECK_VERSION(num):

                if bd.analisar == 0:
                    if num[0:6] == ['V', 'V', 'V', 'V', 'V', 'P']:
                        bd.estrategy_name = 'MOD03'
                        bd.direction_color = '⬛️'
                        bd.analisar = 1
                        bot.send_message(chat_id=chat_id, text='''
            PADRÃO %s 
‼️ Atenção ‼️
Entrada confirmada

Entra no ⚫⚫⚫
Defesa   ⚪⚪⚪                        
                        ''' % (bd.estrategy_name))
                        return
                    if num[0:6] == ['P', 'P', 'P', 'P', 'P', 'V']:
                        bd.estrategy_name = 'MOD03'
                        bd.direction_color = '🟥'
                        bd.analisar = 1
                        bot.send_message(chat_id=chat_id, text='''
            PADRÃO %s
‼️ Atenção ‼️
Entrada confirmada

Entra no 🔴🔴🔴
Defesa   ⚪⚪⚪
                        ''' % (bd.estrategy_name))
                        return

                elif bd.analisar == 1:
                    martingales()
                    return

            CHECK_VERSION(bd.finalcor)

        if bd.estrategy_name == 'ALSE' or bd.estrategy_name == 'MOD04':

            def CHECK_VERSION(num):

                if bd.analisar == 0:
                    if num[0:6] == ['V', 'V', 'V', 'V', 'V', 'P']:
                        bd.estrategy_name = 'MOD04'
                        bd.direction_color = '⬛️'
                        bd.analisar = 1
                        bot.send_message(chat_id=chat_id, text='''
            PADRÃO %s 
‼️ Atenção ‼️
Entrada confirmada

Entra no ⚫⚫⚫
Defesa   ⚪⚪⚪                        
                        ''' % (bd.estrategy_name))
                        return
                    if num[0:6] == ['P', 'P', 'P', 'P', 'P', 'V']:
                        bd.estrategy_name = 'MOD04'
                        bd.direction_color = '🟥'
                        bd.analisar = 1
                        bot.send_message(chat_id=chat_id, text='''
            PADRÃO %s
‼️ Atenção ‼️
Entrada confirmada

Entra no 🔴🔴🔴
Defesa   ⚪⚪⚪
                        ''' % (bd.estrategy_name))
                        return

                elif bd.analisar == 1:
                    martingales()
                    return

            checkVersion = CHECK_VERSION(bd.finalcor)
            print(checkVersion)
