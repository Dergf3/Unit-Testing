import datetime

def check_symbol(symbol):
    symbol.upper()
    if(symbol.isalpha() == True):
        print ("The symbol ", symbol, " is valid.")
    else:
        print ("The symbol ", symbol, " is not valid.")

def check_chart(chart):
    if(chart == '1' or chart == '2'):
        print ("The chart is valid.")
    else:
        print ("The chart is not valid.")

def check_time(time):
    if(time == '1' or time == '2' or time == '3' or time == '4'):
        print ("The time is valid.")
    else:
        print ("The time is not valid.")

def check_date(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        print ("The date is valid.")
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")

symbol_1 = '158A'
symbol_2 = 'ABCD'

check_symbol(symbol_1)
check_symbol(symbol_2)

chart_1 = '1'
chart_2 = '3'

check_chart(chart_1)
check_chart(chart_2)

time_1 = '3'
time_2 = '8'

check_time(time_1)
check_time(time_2)

start_1 = '1567984'
start_2 = '2015-05-25'
end_1 = '2016-07-4'
end_2 = '5164984l'

check_date(start_2)
check_date(end_1)
check_date(end_2)
check_date(start_1)
