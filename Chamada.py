import json
import time

import requests
from Conexao_DB import insert_candle
import schedule
from datetime import datetime

#moeda que serão avaliadas
Moedas_candles = ['BTC_BTS']




def Retorno_candles(Periodicidade):

    api_url = 'https://poloniex.com/public?command=returnTicker'

    response = requests.get(api_url)
    # se é 200, uma resposta bem sucedida, então usamos a função loads do módulo json para carregar uma string como
    # JSON.
    if response.status_code == 200:
        Retorno = json.loads(response.content)
        for buscar_dados_Moedas in Moedas_candles:
            Moeda = buscar_dados_Moedas
            horario = datetime.now()
            print(Retorno[buscar_dados_Moedas])
            Open = Retorno[buscar_dados_Moedas]['last']
            High = Retorno[buscar_dados_Moedas]['highestBid']
            Low = Retorno[buscar_dados_Moedas]['lowestAsk']
            Close = Retorno[buscar_dados_Moedas]['last']

            print(Moeda, Periodicidade,horario, Open, Low, High, Close)
            insert_candle(Moeda, Periodicidade,horario, Open, Low, High, Close)

    else:
        print(response)

# o aplicativo rodararam de 1 em 1 minunto 5 em 5 e 10 em 10.
schedule.every(1).minutes.do(Retorno_candles,1)

schedule.every(5).minutes.do(Retorno_candles,5)

schedule.every(10).minutes.do(Retorno_candles,10)


while True:
    schedule.run_pending()
    time.sleep(1)
