import pandas as pd
import numpy as np

def turtle_soup_strategy(data):
    """
    Implémente la stratégie Turtle Soup.
    data: DataFrame avec colonnes 'Open', 'High', 'Low', 'Close', 'Time'.
    """

    # Calcul des EMA
    data['EMA_21'] = data['Close'].ewm(span=21, adjust=False).mean()
    data['EMA_30'] = data['Close'].ewm(span=30, adjust=False).mean()

    # Calcul de l'ATR
    data['TR'] = np.maximum(data['High'] - data['Low'],
                            np.maximum(abs(data['High'] - data['Close'].shift(1)),
                                       abs(data['Low'] - data['Close'].shift(1))))
    data['ATR'] = data['TR'].rolling(window=20).mean()

    # Définir la tendance
    data['Trend'] = np.where(data['EMA_21'] > data['EMA_30'], "Bullish", "Bearish")

    # Signaux
    data['Buy_Signal'] = ((data['Close'] == data['Low'].rolling(window=5).min()) &
                          (data['Trend'] == "Bullish") &
                          (data['Time'].dt.hour >= 6) & (data['Time'].dt.hour < 22))
    
    data['Sell_Signal'] = ((data['Close'] == data['High'].rolling(window=5).max()) &
                           (data['Trend'] == "Bearish") &
                           (data['Time'].dt.hour >= 6) & (data['Time'].dt.hour < 22))
    
    # Stop Loss
    data['Stop_Loss_Long'] = data['Close'] - 3 * data['ATR']
    data['Stop_Loss_Short'] = data['Close'] + 3 * data['ATR']
    
    # Sortie
    data['Exit_Long'] = data['Close'] == data['High'].rolling(window=5).max()
    data['Exit_Short'] = data['Close'] == data['Low'].rolling(window=5).min()

    return data
