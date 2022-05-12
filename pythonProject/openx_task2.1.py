from datetime import datetime

brian = open("brian.txt", "r")
alex = open("alex.txt", "r")

brian_time = brian.read()
alex_time = alex.read()

brian_1 = brian_time[0:10]
brian_2 = brian_time[11:30]
brian_3 = brian_time[33:52]

alex_1 = alex_time[0:19]
alex_2 = alex_time[22:41]

time_now = "2022-07-01 09:00:00"

datetime_brian_1 = datetime.strptime(brian_1, '%Y-%m-%d')
datetime_brian_2 = datetime.strptime(brian_2, '%Y-%m-%d %H:%M:%S')
datetime_brian_3 = datetime.strptime(brian_3, '%Y-%m-%d %H:%M:%S')
datetime_alex_1 = datetime.strptime(alex_1, '%Y-%m-%d %H:%M:%S')
datetime_alex_2 = datetime.strptime(alex_2, '%Y-%m-%d %H:%M:%S')
datetime_now = datetime.strptime(time_now, '%Y-%m-%d %H:%M:%S')

print(datetime_now)
print(type(datetime_now))

def calendars(duration_in_minutes, minimum_people):
    pass

