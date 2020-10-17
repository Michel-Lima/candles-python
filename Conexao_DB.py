import time

import mysql.connector




def insert_candle(Moeda, Periodicidade, Datetime, Open, Low, High, close):
    connection = mysql.connector.connect(host='db',
                                         database='Smarttbot',
                                         user='root',
                                         password='password',
                                         port=3307)

    cursor = connection.cursor()
    query = "insert into candles (Moeda,Periodicidade,Datetime,Open,Low,High,close) values(%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(query, (Moeda, Periodicidade, Datetime, Open, Low, High, close))
    connection.commit()
    cursor.close()

