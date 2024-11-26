// Indicateurs
EMA21 = ExponentialAverage[21](Close);
EMA30 = ExponentialAverage[30](Close);

// ATR
TR = Max(High - Low, Max(Abs(High - Close[1]), Abs(Low - Close[1])));
ATR20 = Average[20](TR);

// Tendance
Trend = EMA21 > EMA30 ? 1 : -1;

// Signaux d'achat et de vente
BuySignal = (Close == Lowest[5](Low)) AND (Trend == 1) AND (Hour(Time) >= 6 AND Hour(Time) < 22);
SellSignal = (Close == Highest[5](High)) AND (Trend == -1) AND (Hour(Time) >= 6 AND Hour(Time) < 22);

// Stops
StopLossLong = Close - 3 * ATR20;
StopLossShort = Close + 3 * ATR20;

// Sortie
ExitLong = Close == Highest[5](High);
ExitShort = Close == Lowest[5](Low);
