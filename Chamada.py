import json
import time

import requests
from Conexao_DB import insert_candle
import schedule
from datetime import datetime

# moeda que serão avaliadas. poderá ser adicionado mais uma moeda  ex Moedas_candles = ['BTC_BTS','nova_moeda']
Moedas_candles = ['BTC_BTS']


# funcao que receber como parametro a periodicidade sendo 1 para um 1 minuto, 5 para 5 minuto 3 10 para 10 minuto.
def Retorno_candles(Periodicidade):
    #url da API
    api_url = 'https://poloniex.com/public?command=returnTicker'

    response = requests.get(api_url)
    # se é 200, uma resposta bem sucedida, então usamos a função loads do módulo json para carregar uma string como
    # JSON.
    if response.status_code == 200:
        #retorno dos resutlado da API
        Retorno = json.loads(response.content)
        # loop para buscar os dados para cada moeda na lista moeda_candles
        for buscar_dados_Moedas in Moedas_candles:
            Moeda = buscar_dados_Moedas
            horario = datetime.now()
            print(Retorno[buscar_dados_Moedas])
            Open = Retorno[buscar_dados_Moedas]['last']
            High = Retorno[buscar_dados_Moedas]['highestBid']
            Low = Retorno[buscar_dados_Moedas]['lowestAsk']
            Close = Retorno[buscar_dados_Moedas]['last']

            print(Moeda, Periodicidade, horario, Open, Low, High, Close)
            insert_candle(Moeda, Periodicidade, horario, Open, Low, High, Close)

    else:
        print(response)


# o app será executado a cada 1,5,10 minuto.
schedule.every(1).minutes.do(Retorno_candles, 1)

schedule.every(5).minutes.do(Retorno_candles, 5)

schedule.every(10).minutes.do(Retorno_candles, 10)

while True:
    schedule.run_pending()
    time.sleep(1)
