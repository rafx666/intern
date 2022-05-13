from datetime import datetime
import pandas as pd

brian = open("brian.txt", "r")
alex = open("alex.txt", "r")

brian_time = brian.readlines()
alex_time = alex.readlines()

datetime_brian = []
datetime_alex = []

time_1 = datetime.strptime("2022-06-01 00:00:00", '%Y-%m-%d %H:%M:%S')
time_3 = datetime.strptime("2022-06-02 00:00:00", '%Y-%m-%d %H:%M:%S')
time_4 = datetime.strptime("2022-06-01 00:00:01", '%Y-%m-%d %H:%M:%S')
datetime_end = datetime.strptime("2022-07-03 00:00:00", '%Y-%m-%d %H:%M:%S')
time_5 = datetime.strptime("2022-06-01 00:01:00", '%Y-%m-%d %H:%M:%S')

sec = time_4 - time_1
day = time_3 - time_1
one_min = time_5 - time_1

i = 0
while i < len(brian_time):
    if len(brian_time[i]) == 11:
        datetime_brian.append(datetime.strptime(brian_time[i][0:10], '%Y-%m-%d'))
    elif len(brian_time[i]) > 11:
        brian_time_list = brian_time[i].split(" - ")
        d = 0
        while d < 2:
            datetime_brian.append(datetime.strptime(brian_time_list[d], '%Y-%m-%d %H:%M:%S'))
            d += 1
    i += 1

i = 0
while i < len(alex_time):
    if len(alex_time[i]) == 11:
        datetime_alex.append(datetime.strptime(alex_time[i][0:10], '%Y-%m-%d'))
    elif len(alex_time[i]) > 11:
        alex_time_list = alex_time[i].split(" - ")
        d = 0
        while d < 2:
            datetime_alex.append(datetime.strptime(alex_time_list[d], '%Y-%m-%d %H:%M:%S'))
            d += 1
    i += 1

def calendars(duration_in_minutes, minimum_people):

    if minimum_people == 0:
        print("There's no meeting.")

    elif minimum_people == 1:
        i = 0
        while i < (len(datetime_brian) - 1):
            date_b = datetime_brian[i + 1] - datetime_brian[i]
            if date_b < day:
                range_brian_set = set(pd.date_range(start=datetime_brian[i + 1], end=datetime_end, freq='s'))
            else:
                if datetime_brian[i + 1] == (datetime_brian[i] + day):  # to znaczy ze druga data jest rowno 24h po
                    # pierwszej, nie ma mozliwosci zaplanowac spotkania miedzy 1 i 2 datą
                    pass
                else:
                    range_brian_set = set(pd.date_range((datetime_brian[i] + day), datetime_brian[i + 1], freq='s'))
                    #dodaj że roznica musi byc wieksza niz spotkanie
            i += 1

        # range_brian_set - zbior elementow gdzie brian moze spotkanie
        i = 0
        while i < (len(datetime_alex) - 1):
            date_a = datetime_alex[i + 1] - datetime_alex[i]
            if date_a < day:
                range_alex_set = set(pd.date_range(start=datetime_alex[i + 1], end=datetime_end, freq='s'))
            else:
                if datetime_alex[i + 1] == (datetime_alex[i] + day):  # to znaczy ze druga data jest rowno 24h po pierwszej, nie ma mozliwosci zaplanowac spotkania miedzy 1 i 2 datą
                    pass
                else:
                    range_alex_set = set(pd.date_range((datetime_alex[i] + day), datetime_alex[i + 1], freq='s'))
            i += 1
        if min(range_alex_set) < min(range_brian_set):
            meeting_time = min(range_alex_set) + sec
            print(meeting_time)
        else:
            meeting_time = min(range_brian_set) + sec
            print(meeting_time)

    elif minimum_people == 2:
        i = 0
        while i < (len(datetime_brian) - 1):
            date_b = datetime_brian[i + 1] - datetime_brian[i]
            if date_b < day:
                range_brian_set = set(pd.date_range(start=datetime_brian[i + 1], end=datetime_end, freq='s'))
            else:
                if datetime_brian[i + 1] == (datetime_brian[i] + day):  # to znaczy ze druga data jest rowno 24h po pierwszej, nie ma mozliwosci zaplanowac spotkania miedzy 1 i 2 datą
                    pass
                else:
                    range_brian_set = set(pd.date_range((datetime_brian[i] + day), datetime_brian[i + 1], freq='s'))
            i += 1

        # range_brian_set - zbior elementow gdzie brian moze spotkanie
        i = 0
        while i < (len(datetime_alex) - 1):
            date_a = datetime_alex[i + 1] - datetime_alex[i]
            if date_a < day:
                range_alex_set = set(pd.date_range(start=datetime_alex[i + 1], end=datetime_end, freq='s'))
            else:
                if datetime_alex[i + 1] == (datetime_alex[i] + day):  # to znaczy ze druga data jest rowno 24h po pierwszej, nie ma mozliwosci zaplanowac spotkania miedzy 1 i 2 datą
                    pass
                else:
                    range_alex_set = set(pd.date_range((datetime_alex[i] + day), datetime_alex[i + 1], freq='s'))
            i += 1

        common_part = range_brian_set.intersection(range_alex_set)
        meeting_time = min(common_part) + sec
        print(meeting_time)

    else:
        print("Not enough people available.")

calendars(30, 2)
