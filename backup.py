import re
import pandas as pd
file_path = r"C:\Users\ismail amouma\Downloads\admin_bot.sql"

instruments=['AUDCAD', 'AUDCHF', 'AUDCNH', 'AUDCZK', 'AUDDKK', 'AUDHKD', 'AUDHUF', 'AUDJPY', 'AUDMXN', 'AUDNOK', 'AUDNZD', 'AUDPLN', 'AUDSEK', 'AUDSGD', 'AUDUSD', 'AUDZAR', 'CADCHF', 'CADCNH', 'CADCZK', 'CADDKK', 'CADHKD', 'CADHUF', 'CADJPY', 'CADMXN', 'CADNOK', 'CADPLN', 'CADSEK', 'CADSGD', 'CADZAR', 'CHFCNH', 'CHFCZK', 'CHFDKK', 'CHFHKD', 'CHFHUF', 'CHFJPY', 'CHFMXN', 'CHFNOK', 'CHFPLN', 'CHFSEK', 'CHFSGD', 'CHFTRY', 'CHFZAR', 'DKKCZK', 'DKKHKD', 'DKKHUF', 'DKKMXN', 'DKKNOK', 'DKKPLN', 'DKKSEK', 'DKKSGD', 'DKKZAR', 'EURAUD', 'EURCAD', 'EURCHF', 'EURCNH', 'EURCZK', 'EURDKK', 'EURGBP', 'EURHKD', 'EURHUF', 'EURILS', 'EURJPY', 'EURMXN', 'EURNOK', 'EURNZD', 'EURPLN', 'EURSEK', 'EURSGD', 'EURTRY', 'EURUSD', 'EURZAR', 'GBPAUD', 'GBPCAD', 'GBPCHF', 'GBPCNH', 'GBPCZK', 'GBPDKK', 'GBPHKD', 'GBPHUF', 'GBPJPY', 'GBPMXN', 'GBPNOK', 'GBPNZD', 'GBPPLN', 'GBPSEK', 'GBPSGD', 'GBPUSD', 'GBPZAR', 'JPYCZK', 'JPYDKK', 'JPYHKD', 'JPYHUF', 'JPYMXN', 'JPYNOK', 'JPYPLN', 'JPYSEK', 'JPYSGD', 'JPYZAR', 'NOKCZK', 'NOKHKD', 'NOKHUF', 'NOKMXN', 'NOKPLN', 'NOKSEK', 'NOKSGD', 'NOKZAR', 'NZDCAD', 'NZDCHF', 'NZDCZK', 'NZDDKK', 'NZDHKD', 'NZDHUF', 'NZDJPY', 'NZDMXN', 'NZDNOK', 'NZDPLN', 'NZDSEK', 'NZDSGD', 'NZDUSD', 'NZDZAR', 'USDCAD', 'USDCHF', 'USDCNH', 'USDCZK', 'USDDKK', 'USDHKD', 'USDHUF', 'USDILS', 'USDJPY', 'USDMXN', 'USDNOK', 'USDPLN', 'USDSEK', 'USDSGD', 'USDTRY', 'USDZAR', 'XAUUSD', 'XAUEUR', 'XAGUSD', 'XAGEUR', 'DOW', 'DOW30', 'DOWJONES', 'US30', 'NAS', 'NASDAQ', 'NASDAQ100', 'NAS100', 'US100', 'SP500', 'S&P500', 'US500', 'BRENT', 'CRUDEOIL', 'UKOIL', 'USOIL', 'WTI', 'USCRUDE', 'UKCRUDE', 'GERMAN30', 'GER30', 'UK100', 'GOLD', 'SILVER','AUD/CAD', 'AUD/CHF', 'AUD/CNH', 'AUD/CZK', 'AUD/DKK', 'AUD/HKD', 'AUD/HUF', 'AUD/JPY', 'AUD/MXN', 'AUD/NOK', 'AUD/NZD', 'AUD/PLN', 'AUD/SEK', 'AUD/SGD', 'AUD/USD', 'AUD/ZAR', 'CAD/CHF', 'CAD/CNH', 'CAD/CZK', 'CAD/DKK', 'CAD/HKD', 'CAD/HUF', 'CAD/JPY', 'CAD/MXN', 'CAD/NOK', 'CAD/PLN', 'CAD/SEK', 'CAD/SGD', 'CAD/ZAR', 'CHF/CNH', 'CHF/CZK', 'CHF/DKK', 'CHF/HKD', 'CHF/HUF', 'CHF/JPY', 'CHF/MXN', 'CHF/NOK', 'CHF/PLN', 'CHF/SEK', 'CHF/SGD', 'CHF/TRY', 'CHF/ZAR', 'DKK/CZK', 'DKK/HKD', 'DKK/HUF', 'DKK/MXN', 'DKK/NOK', 'DKK/PLN', 'DKK/SEK', 'DKK/SGD', 'DKK/ZAR', 'EUR/AUD', 'EUR/CAD', 'EUR/CHF', 'EUR/CNH', 'EUR/CZK', 'EUR/DKK', 'EUR/GBP', 'EUR/HKD', 'EUR/HUF', 'EUR/ILS', 'EUR/JPY', 'EUR/MXN', 'EUR/NOK', 'EUR/NZD', 'EUR/PLN', 'EUR/SEK', 'EUR/SGD', 'EUR/TRY', 'EUR/USD', 'EUR/ZAR', 'GBP/AUD', 'GBP/CAD', 'GBP/CHF', 'GBP/CNH', 'GBP/CZK', 'GBP/DKK', 'GBP/HKD', 'GBP/HUF', 'GBP/JPY', 'GBP/MXN', 'GBP/NOK', 'GBP/NZD', 'GBP/PLN', 'GBP/SEK', 'GBP/SGD', 'GBP/USD', 'GBP/ZAR', 'JPY/CZK', 'JPY/DKK', 'JPY/HKD', 'JPY/HUF', 'JPY/MXN', 'JPY/NOK', 'JPY/PLN', 'JPY/SEK', 'JPY/SGD', 'JPY/ZAR', 'NOK/CZK', 'NOK/HKD', 'NOK/HUF', 'NOK/MXN', 'NOK/PLN', 'NOK/SEK', 'NOK/SGD', 'NOK/ZAR', 'NZD/CAD', 'NZD/CHF', 'NZD/CZK', 'NZD/DKK', 'NZD/HKD', 'NZD/HUF', 'NZD/JPY', 'NZD/MXN', 'NZD/NOK', 'NZD/PLN', 'NZD/SEK', 'NZD/SGD', 'NZD/USD', 'NZD/ZAR', 'USD/CAD', 'USD/CHF', 'USD/CNH', 'USD/CZK', 'USD/DKK', 'USD/HKD', 'USD/HUF', 'USD/ILS', 'USD/JPY', 'USD/MXN', 'USD/NOK', 'USD/PLN', 'USD/SEK', 'USD/SGD', 'USD/TRY', 'USD/ZAR', 'v25', 'volatility 25 index']
Orders=['buy','sell','buy now','sell now','buy limit','sell limit','buy stop','sell stop']
with open(file_path, 'r',encoding='utf-8') as file:
    sql_content = file.read()
insert_statements = re.findall(r"INSERT INTO `messages` VALUES \((.*?)\);", sql_content, re.DOTALL)

text_list=insert_statements[0].split('),')
final_list=[]
def is_number(string):
    return re.match(r'^\d+(\.\d+)?$', string) is not None
def simplify_message(message):
    message = message.lower().replace('tp 1', 'tp').replace('tp 2', 'tp').replace('tp 3', 'tp').replace('(','').replace(')','').replace('[','').replace(']','').replace('tp1','tp').replace('tp2','tp').replace('tp3','tp').strip().replace(':','').replace('@','').replace('-','')
    words = message.split()
    print(words)
    simplified_message = []
    add_tp_next = False
    for i, word in enumerate(words):
                if len(word)!=1:
                    if word == 'tp':
                        add_tp_next = True
                        continue
                    elif word in 'sl':
                            if add_tp_next:
                                simplified_message.append('tp')
                                add_tp_next = False
                            simplified_message.append(word)
                    elif word in ['open','open hold']:
                            if add_tp_next:
                                simplified_message.append('tp')
                                add_tp_next = False
                            simplified_message.append(word)
                    elif is_number(word):
                        if ('pip' or 'pips') in  message:
                            if  (i==len(words)-1 and words[i] not in ['pips', 'pip']) or (i + 1 < len(words) and words[i + 1] not in ['pips', 'pip']) or (i + 2 < len(words) and words[i + 2] not in ['pips', 'pip']) or (i + 3 < len(words) and words[i + 3] not in ['pips', 'pip']) or (0<=i-1<len(words) and words[i-1]=='sl'):

                                if add_tp_next:
                                    simplified_message.append('tp')
                                    add_tp_next = False
                                simplified_message.append(word)
                        else:
                                if add_tp_next:
                                    simplified_message.append('tp')
                                    add_tp_next = False
                                simplified_message.append(word)
                         
                
    final_text=' '.join(simplified_message)
    return final_text

def extract_colomus(text):
     words=text.split()
     entry_prices =[]
     take_profit_prices =[]
     stop_loss =[]
     for i,word in enumerate(words):
          if word=='tp':
               try:
                    take_profit_prices.append(words[i+1])
               except:
                    pass
          elif word=='sl':
               try:
                    stop_loss.append(words[i+1])
               except:
                    pass
     index=0
     while  index<len(words) and words[index]!='tp' and words[index]!='sl' :
          entry_prices.append(words[index])
          index+=1
     return entry_prices,take_profit_prices,stop_loss
for elm in text_list:
    dic={'source_message_id':'',
         'source_message_id':'',
         'chatid':'',
         'target_message_id':'',
         'text':'',
         'Instrument name':'',
         'Entry price 1':'',
         'Entry price 2':'',
         'Entry price 3':'',
         'Entry price 4':'',
         'Entry price 5':'',
         'Take profit price 1':'',
         'Take profit price 2':'',
         'Take profit price 3':'',
         'Take profit price 4':'',
         'Take profit price 5':'',
         'Stop loss price':'',
         'Order Type' : ''
         }
    elm=elm.replace('(','').replace('\\n',' ').strip()
    elm=elm.split(',')

    dic['source_message_id']=elm[0]
    dic['target_message_id']=elm[1]
    dic['chatid']=elm[2]
    dic['text']=elm[3]
    text=simplify_message(dic['text'].replace("'","") )
    print(dic['text'].replace("'",""))
    entry_prices,take_profit_prices,stop_loss=extract_colomus(text)

    try:
        dic['Entry price 1']=entry_prices[0]
    except:
        pass
    try:
        dic['Entry price 2']=entry_prices[1]
    except:
        pass
    try:
        dic['Entry price 3']=entry_prices[2]
    except:
        pass
    try:
        dic['Entry price 4']=entry_prices[3]
    except:
        pass
    try:
        dic['Entry price 5']=entry_prices[4]
    except:
        pass
    try:
        dic['Take profit price 1']=take_profit_prices[0]
    except:
        pass
    try:
        dic['Take profit price 2']=take_profit_prices[1]
    except:
        pass
    try:
        dic['Take profit price 3']=take_profit_prices[2]
    except:
        pass
    try:
        dic['Take profit price 4']=take_profit_prices[3]
    except:
        pass
    try:
        dic['Take profit price 5']=take_profit_prices[4]
    except:
        pass
    try:
        dic['Stop loss price']=stop_loss[0]
    except:
        pass
    Orders=['buy','sell','buy now','sell now','buy limit','sell limit','buy stop','sell stop']
    
    for order in Orders:
        if order in dic['text'].lower():
            dic['Order Type']=order.capitalize()
    for instrument in instruments:
        if instrument.lower() in dic['text'].lower():
            dic['Instrument name']=instrument

    final_list.append(dic)

df=pd.DataFrame(final_list)
df.to_csv(r'c:\Users\ismail amouma\Desktop\final_2.csv',index=False)

