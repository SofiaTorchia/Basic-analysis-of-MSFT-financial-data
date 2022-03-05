def simple_moving_average(series,period):
    n = series.shape[0]
    avr = []
    for i in range(n-period):
        s = 0.0
        for j in range(period):
            s = s + series[j+i]
        s = s/period
        avr.append(s)
    s_m_avr = [None for i in range(period)]
    return s_m_avr + avr

def ema(series,period,smoothing):
    n = series.shape[0]
    ema = [series[0]]
    for j in range(n-1):
        e = series[j+1] * (smoothing/(1+period)) + ema[j]*(1-(smoothing/(1+period)))
        ema.append(e)
    return ema

def average_true_range(high,low,close,period):
    n = high.shape[0]
    s = 0
    atr = []
    for j in range(n-period-1):
        for i in range(period):
            tr = max([high[i+j+1]-low[i+j+1],abs(high[i+j+1]-close[i+j]),abs(low[i+j+1]-close[i+j])])
            s = s + tr
        s = s/period
        atr.append(tr)
    return [None for i in range(period+1)] + atr


def typical_price(high,low,close):
    n = high.shape[0]
    tp = []
    for i in range(n):
        tp.append((high[i] + low[i] + close[i])/3)
    return tp


def average_typical_price(tp,period):
    atp = simple_moving_average(tp,period)
    return atp


def mean_deviation(tp,ma,period):
    n = ma.shape[0]
    md = []
    for i in range(0,n-period):
        s = 0
        for j in range(period):
            s = s + abs(tp[i+j]-ma[i+j])
        s = s/period
        md.append(s)
    return [None for j in range(period)] + md


def commodity_channel_index(tp,ma,md,period):
    n = ma.shape[0]
    cci = []
    for i in range(n-period):
        s = (tp[i] - ma[i])/(0.015 * md[i])
        cci.append(s)
    return [None for j in range(period)] + cci

