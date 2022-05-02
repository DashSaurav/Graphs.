import pandas as pd

dff_kar = pd.read_csv("data_folder/processed_occ_df.csv")

dff_kar['date'] = pd.to_datetime(dff_kar['date'], format='%Y-%m-%d')
dff_kar['T_time'] = pd.to_datetime(dff_kar['T_time'], format='%H:%M:%S')
dff_kar['T_time'] = dff_kar['T_time'].dt.time
dff_kar['Camera3'] = dff_kar["Camera3"].astype(int)


def heat_map_func(date, thresh_1, thresh_2):
    """
    Takes in the dataframe created by AI engine with additional type and column changes and returns a dataframe containing records for given input date
    with 0-24 hour bucket where each row shows how many times the occupancy count went above the given threshold in that particular hour range.
    
    Args:
        df: Input dataframe
        date: date in string form (ex:-"2022-03-28")for which records have to be retrieved
        thresh: Threshold for occupancy
    Returns:
        op_df: Output Dataframe
    """
    data = dff_kar[dff_kar['date'] == pd.to_datetime(str(date))]
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
    m1_thresh_val = []
    m2_thresh_val = []
    hour_index = []
    for hour in range(0,last_hr+1):
        hour_index.append(hour)
        data_m1_hour = data_m1[data_m1['Hour'] == hour]
        m1_thresh_count = 0
        for m1_occ in data_m1_hour['T_Occupancy']:
            if m1_occ > int(thresh_1):
                m1_thresh_count += 1
        m1_thresh_val.append(m1_thresh_count)
        data_m2_hour = data_m2[data_m2['Hour'] == hour]
        m2_thresh_count = 0
        for m2_occ in data_m2_hour['T_Occupancy']:
            if m2_occ > int(thresh_2):
                m2_thresh_count += 1
        m2_thresh_val.append(m2_thresh_count)
    dff = {'Hour':hour_index,'M1 Separation Room': m1_thresh_val,'M2 Purification Room': m2_thresh_val}
    op_df = pd.DataFrame(dff)
    m1 = op_df['M1 Separation Room'].to_list()
    m2 = op_df['M2 Purification Room'].to_list()
    return dict({'M1':m1, 'M2':m2})
#kar_df[(kar_df['date'] == pd.to_datetime(str('2022-03-23'))) & (kar_df['Room No'] == 'M1 Separation Room')]
#heat_map_func('2022-03-23',1, 0)