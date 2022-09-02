def timeConversion(s):
    # Write your code here
    hour_code = s[-2:]
    min_sec = s[2:8]
    hour = int(s[:2])
# HORAS DA TARDE
    if(hour_code == 'PM'):
        if(hour==12):
            s_hour = str(hour)
            print(f'{s_hour}{min_sec}')    
            return f'{s_hour}{min_sec}'    
        else:
            hour+=12
            s_hour = str(hour)
            print(f'{s_hour}{min_sec}')
            return f'{s_hour}{min_sec}'
    else:
        if(hour==12):
            hour-=12
            s_hour = str(hour)
            print(f'0{s_hour}{min_sec}')
            return f'{s_hour}{min_sec}'
        else:
            hour+=12
            s_hour = str(hour)
            print(f'{s_hour}{min_sec}')
            return f'{s_hour}{min_sec}'
timeConversion('12:01:00AM')