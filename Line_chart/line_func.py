import pandas as pd
import datetime as dt

dff_kar = pd.read_csv("data_folder/processed_occ_df.csv")

dff_kar['date'] = pd.to_datetime(dff_kar['date'], format='%Y-%m-%d')
dff_kar['T_time'] = pd.to_datetime(dff_kar['T_time'], format='%H:%M:%S')
dff_kar['T_time'] = dff_kar['T_time'].dt.time
dff_kar['Camera3'] = dff_kar["Camera3"].astype(int)

def trend_line_func(date):
    def add_time(time ,hrs=0, mins=0, secs=0):
        return(dt.datetime.combine(dt.date(1,1,1),time) + dt.timedelta(hours=hrs, minutes=mins, seconds=secs)).time()
    data = dff_kar[dff_kar['date'] == pd.to_datetime(str(date))]
    data['Minutess'] = data["T_time"].apply(lambda x: x.minute)
    data_m1 = data[data['Room No']=='M1 Separation Room']
    data_m2 = data[data['Room No']=='M2 Purification Room']
    

    try:
        last_hr_r1 = data_m1.iloc[-1]['Hour']
    except:
        last_hr_r1 = 0
    try:
        last_hr_r2 = data_m2.iloc[-1]['Hour']
    except:
        last_hr_r2 = 0
    last_hr = max(last_hr_r1, last_hr_r2)

    # print(last_hr)
    trend_line_df = pd.DataFrame(columns=['Time', 'M1 Separation Room Occupancy', 'M2 Purification Room Occupancy'])
    
    m1_thresh_val = []
    m2_thresh_val = []
    hour_index = []
    for hour in range(0,last_hr+1):
        hour_index.append(hour)
        data_m1_hour = data_m1[data_m1['Hour'] == hour]
        data_m2_hour = data_m2[data_m2['Hour'] == hour]
        # threshold_value_m1.append(int(saved_result))
        # threshold_value_m2.append(int(saved_result1))
        for minns in range(0, 59, 2):
            try:
                data_m1_min = data_m1_hour[(data_m1_hour['Minutess'] == minns) | (data_m1_hour['Minutess'] == minns+1)]
                m1_minutes_max = data_m1_min['T_Occupancy'].max() # select max occupancy for this time interval of 2 mins
            except:
                m1_minutes_max = 0
            try:
                data_m2_min = data_m2_hour[(data_m2_hour['Minutess'] == minns) | (data_m2_hour['Minutess'] == minns+1)]
                m2_minutes_max = data_m2_min['T_Occupancy'].max() # select max occupancy for this time interval of 2 mins
            except:
                m2_minutes_max = 0
            
            trend_line_df.loc[len(trend_line_df.index)] = [dt.datetime.combine(pd.to_datetime(str(date)),dt.time(hour = hour, minute = minns)), m1_minutes_max, m2_minutes_max] 
    return trend_line_df.fillna(0)
# for i, row in trend_line_func('2022-03-24').iterrows():
#     print(row)
# trend_line_func('2022-03-24')
#trend_line_func('2022-03-23')