import json
import requests
import datetime

now = datetime.datetime.now()
w = datetime.timedelta(days=7)
m = datetime.timedelta(weeks=4)
weekly_time = (now-w).strftime('%Y-%m-%d')
now_time = datetime.datetime.now().strftime('%Y-%m-%d')
monthly_time = (now-m).strftime('%Y-%m-%d')


def get_eur_mid():

    data=requests.get("http://api.nbp.pl/api/exchangerates/rates/a/eur/").json()
    value = data['rates'][0]['mid']
    return(value)


def get_usd_mid():

    data=requests.get("http://api.nbp.pl/api/exchangerates/rates/a/usd/").json()
    value = data['rates'][0]['mid']
    return(value)


def get_chf_mid():

    data=requests.get("http://api.nbp.pl/api/exchangerates/rates/a/chf/").json()
    value = data['rates'][0]['mid']
    return(value)


def get_gbp_mid():
    data=requests.get("http://api.nbp.pl/api/exchangerates/rates/a/gbp/").json()
    value = data['rates'][0]['mid']
    return(value)


def get_eur_ask_bid():

    data=requests.get("http://api.nbp.pl/api/exchangerates/rates/c/eur/").json()
    value = data['rates'][0]
    ask = value['ask']
    bid = value['bid']
    return(ask,bid)


def get_usd_ask_bid():

    data=requests.get("http://api.nbp.pl/api/exchangerates/rates/c/usd/").json()
    value = data['rates'][0]
    ask = value['ask']
    bid = value['bid']
    return (ask, bid)


def get_chf_ask_bid():

    data=requests.get("http://api.nbp.pl/api/exchangerates/rates/c/chf/").json()
    value = data['rates'][0]
    ask = value['ask']
    bid = value['bid']
    return(ask,bid)


def get_gbp_ask_bid():

    data=requests.get("http://api.nbp.pl/api/exchangerates/rates/c/gbp/").json()
    value = data['rates'][0]
    ask = value['ask']
    bid = value['bid']
    return (ask, bid)


def get_eur_ask_bid_weekly():

    data = requests.get(("http://api.nbp.pl/api/exchangerates/rates/c/eur/{}/{}/").format(weekly_time,now_time)).json()
    data = data['rates']
    ask_values = [data[_]['ask'] for _ in range(len(data))]
    bid_values = [data[_]['bid'] for _ in range(len(data))]
    ask_max = max(ask_values)
    ask_min = min(ask_values)
    bid_max = max(bid_values)
    bid_min = min(bid_values)
    ask_mid =round(sum(ask_values)/len(data),4)
    bid_mid = round(sum(bid_values) / len(data),4)
    ask_trend = round(ask_values[len(data)-1] - ask_values[len(data)-2],4)
    bid_trend = round(bid_values[len(data)-1] - bid_values[len(data)-2],4)
    ask_trend = str(ask_trend) if ask_trend <= 0 else '+' + str(ask_trend)
    bid_trend = str(bid_trend) if bid_trend <= 0 else '+' + str(bid_trend)
    return([ask_max,ask_min,ask_mid,ask_trend],[bid_max,bid_min,bid_mid,bid_trend])


def get_usd_ask_bid_weekly():

    data = requests.get(("http://api.nbp.pl/api/exchangerates/rates/c/usd/{}/{}/").format(weekly_time,now_time)).json()
    data = data['rates']
    ask_values = [data[_]['ask'] for _ in range(len(data))]
    bid_values = [data[_]['bid'] for _ in range(len(data))]
    ask_max = max(ask_values)
    ask_min = min(ask_values)
    bid_max = max(bid_values)
    bid_min = min(bid_values)
    ask_mid = round(sum(ask_values)/len(data),4)
    bid_mid = round(sum(bid_values) / len(data),4)
    ask_trend = round(ask_values[len(data)-1] - ask_values[len(data)-2],4)
    bid_trend = round(bid_values[len(data)-1] - bid_values[len(data)-2],4)
    ask_trend = str(ask_trend) if ask_trend <= 0 else '+' + str(ask_trend)
    bid_trend = str(bid_trend) if bid_trend <= 0 else '+' + str(bid_trend)
    return([ask_max,ask_min,ask_mid,ask_trend],[bid_max,bid_min,bid_mid,bid_trend])


def get_chf_ask_bid_weekly():

    data = requests.get(("http://api.nbp.pl/api/exchangerates/rates/c/chf/{}/{}/").format(weekly_time,now_time)).json()
    data = data['rates']
    ask_values = [data[_]['ask'] for _ in range(len(data))]
    bid_values = [data[_]['bid'] for _ in range(len(data))]
    ask_max = max(ask_values)
    ask_min = min(ask_values)
    bid_max = max(bid_values)
    bid_min = min(bid_values)
    ask_mid = round(sum(ask_values)/len(data),4)
    bid_mid = round(sum(bid_values) / len(data),4)
    ask_trend = round(ask_values[len(data)-1] - ask_values[len(data)-2],4)
    bid_trend = round(bid_values[len(data)-1] - bid_values[len(data)-2],4)
    ask_trend = str(ask_trend) if ask_trend <= 0 else '+' + str(ask_trend)
    bid_trend = str(bid_trend) if bid_trend <= 0 else '+' + str(bid_trend)
    return([ask_max,ask_min,ask_mid,ask_trend],[bid_max,bid_min,bid_mid,bid_trend])


def get_gbp_ask_bid_weekly():

    data = requests.get(("http://api.nbp.pl/api/exchangerates/rates/c/gbp/{}/{}/").format(weekly_time,now_time)).json()
    data = data['rates']
    ask_values = [data[_]['ask'] for _ in range(len(data))]
    bid_values = [data[_]['bid'] for _ in range(len(data))]
    ask_max = max(ask_values)
    ask_min = min(ask_values)
    bid_max = max(bid_values)
    bid_min = min(bid_values)
    ask_mid = round(sum(ask_values)/len(data),4)
    bid_mid = round(sum(bid_values) / len(data),4)
    ask_trend = round(ask_values[len(data)-1] - ask_values[len(data)-2],4)
    bid_trend = round(bid_values[len(data)-1] - bid_values[len(data)-2],4)
    ask_trend = str(ask_trend) if ask_trend <= 0 else '+' + str(ask_trend)
    bid_trend = str(bid_trend) if bid_trend <= 0 else '+' + str(bid_trend)
    return([ask_max,ask_min,ask_mid,ask_trend],[bid_max,bid_min,bid_mid,bid_trend])


euro_mid = get_eur_mid()
dollar_mid = get_usd_mid()
chf_mid = get_chf_mid()
gbp_mid = get_gbp_mid()
euro_ask, euro_bid = get_eur_ask_bid()
dollar_ask, dollar_bid = get_usd_ask_bid()
chf_ask, chf_bid = get_chf_ask_bid()
gbp_ask, gbp_bid = get_gbp_ask_bid()
eur_ask_weekly, eur_bid_weekly = get_eur_ask_bid_weekly()
usd_ask_weekly, usd_bid_weekly = get_usd_ask_bid_weekly()
chf_ask_weekly, chf_bid_weekly = get_chf_ask_bid_weekly()
gbp_ask_weekly, gbp_bid_weekly = get_gbp_ask_bid_weekly()

print('{} Avg: {} Ask: {} Bid: {}'.format('EUR:', euro_mid, euro_ask, euro_bid))
print('\n'
      'from {} to  {} (Today)\n'
      'Max ask:    {}\n'
      'Min aks:    {}\n'
      'Avg ask:    {}\n'
      'Ask trend: {}\n'
      'Max bid:    {}\n'
      'Min bid:    {}\n'
      'Avg bid:    {}\n'
      'Bid trend: {}\n'.format(weekly_time,now_time,*eur_ask_weekly,*eur_bid_weekly)
      )

print('{} Avg: {} Ask: {} Bid: {}'.format('USD:', dollar_mid, dollar_ask, dollar_bid))
print('\n'
      'from {} to  {} (Today)\n'
      'Max ask:    {}\n'
      'Min aks:    {}\n'
      'Avg ask:    {}\n'
      'Ask trend: {}\n'
      'Max bid:    {}\n'
      'Min bid:    {}\n'
      'Avg bid:    {}\n'
      'Bid trend: {}\n'.format(weekly_time,now_time,*usd_ask_weekly,*usd_bid_weekly)
      )

print('{} Avg: {} Ask: {} Bid: {}'.format('CHF:', chf_mid, chf_ask, chf_bid))
print('\n'
      'from {} to  {} (Today)\n'
      'Max ask:    {}\n'
      'Min aks:    {}\n'
      'Avg ask:    {}\n'
      'Ask trend: {}\n'
      'Max bid:    {}\n'
      'Min bid:    {}\n'
      'Avg bid:    {}\n'
      'Bid trend: {}\n'.format(weekly_time,now_time,*chf_ask_weekly,*chf_bid_weekly)
      )

print('{} Avg: {} Ask: {} Bid: {}'.format('GBP:', gbp_mid, gbp_ask, gbp_bid))
print('\n'
      'from {} to  {} (Today)\n'
      'Max ask:    {}\n'
      'Min aks:    {}\n'
      'Avg ask:    {}\n'
      'Ask trend: {}\n'
      'Max bid:    {}\n'
      'Min bid:    {}\n'
      'Avg bid:    {}\n'
      'Bid trend: {}\n'.format(weekly_time,now_time,*gbp_ask_weekly,*gbp_bid_weekly)
      )