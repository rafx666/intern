time = "2022-06-01 12:00:00 - 2022-06-01 12:59:59"
time_1 = time[0:19]
time_2 = time[22:41]
print(time_1)
print(time_2)
time_dif_1 = "2022-06-01 00:00:00"
time_dif_2 = "2022-06-01 00:30:00"
from datetime import datetime


datetime_object_1 = datetime.strptime(time_1, '%Y-%m-%d %H:%M:%S')
datetime_object_2 = datetime.strptime(time_2, '%Y-%m-%d %H:%M:%S')
datetime_object_3 = datetime.strptime(time_dif_1, '%Y-%m-%d %H:%M:%S')
datetime_object_4 = datetime.strptime(time_dif_2, '%Y-%m-%d %H:%M:%S')

print(datetime_object_1, datetime_object_2)
time_difference = datetime_object_4 - datetime_object_3
time_meet = datetime_object_2 - datetime_object_1

print(datetime_object_2-datetime_object_1)
print(time_difference)

print(time_difference < time_meet)

print(datetime_object_1 + time_difference)
#da się to dodawać i odejmować

#jakiś if że jeśli data jest większa od time1 i mniejsza od time2 to pomiń bo sie nie nadaje do ustalenia meetingu


