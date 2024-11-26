//@version=5
indicator("Turtle Soup", overlay=true)

// Inputs
ema21 = ta.ema(close, 21)
ema30 = ta.ema(close, 30)
atr = ta.atr(20)

// Tendance
trend = ema21 > ema30 ? 1 : -1

// Signaux
buy_signal = (close == ta.lowest(low, 5)) and (trend == 1) and (hour >= 6 and hour < 22)
sell_signal = (close == ta.highest(high, 5)) and (trend == -1) and (hour >= 6 and hour < 22)

// Stops
stop_loss_long = close - 3 * atr
stop_loss_short = close + 3 * atr

// Sortie
exit_long = close == ta.highest(high, 5)
exit_short = close == ta.lowest(low, 5)

// Plot
plotshape(buy_signal, style=shape.labelup, color=color.new(color.green, 0), location=location.belowbar, text="Buy")
plotshape(sell_signal, style=shape.labeldown, color=color.new(color.red, 0), location=location.abovebar, text="Sell")
plot(stop_loss_long, color=color.red, title="Stop Loss Long")
plot(stop_loss_short, color=color.blue, title="Stop Loss Short")
