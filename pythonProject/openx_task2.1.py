from datetime import datetime

brian = open("brian.txt", "r")
alex = open("alex.txt", "r")

brian_time = brian.readlines()
alex_time = alex.readlines()

datetime_brian = []
datetime_alex = []

time_1 = datetime.strptime("2022-06-01 00:00:00", '%Y-%m-%d %H:%M:%S')
time_2 = datetime.strptime("2022-06-01 00:30:00", '%Y-%m-%d %H:%M:%S')
time_3 = datetime.strptime("2022-06-02 00:00:00", '%Y-%m-%d %H:%M:%S')

half_hour = time_2 - time_1
day = time_3 - time_1

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

i = 0

while i < len(datetime_brian):
    date = datetime_brian[i + 1] - datetime_brian[i]
    if date >= day:
        print("szukamy czasu między 2 i 3 elementem listy")
    else:
        print("szukamy czasu między 1 i 2 elementem listy")
    i += 1
  
"""
def calendars(duration_in_minutes, minimum_people):
    pass

"""
