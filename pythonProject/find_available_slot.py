from datetime import datetime
import pandas as pd #importing modules

brian = open("brian.txt", "r")  #opening both text files
alex = open("alex.txt", "r")

brian_time = brian.readlines()  #reading the files line by line
alex_time = alex.readlines()

datetime_brian = [] #creating empty lists to store datetime data
datetime_alex = []

time_1 = datetime.strptime("2022-06-01 00:00:00", '%Y-%m-%d %H:%M:%S')  #creating datetime data
time_2 = datetime.strptime("2022-06-02 00:00:00", '%Y-%m-%d %H:%M:%S')
time_3 = datetime.strptime("2022-06-01 00:00:01", '%Y-%m-%d %H:%M:%S')
datetime_end = datetime.strptime("2022-07-03 00:00:00", '%Y-%m-%d %H:%M:%S')
time_4 = datetime.strptime("2022-06-01 00:01:00", '%Y-%m-%d %H:%M:%S')

sec = time_3 - time_1   #substracting datetime variables to recieve specified periods of time without year, month and day
day = time_2 - time_1
one_min = time_4 - time_1

i = 0
while i < len(brian_time):  #while loop: when i is smaller than lenght of brian_time list
    if len(brian_time[i]) == 11:
        datetime_brian.append(datetime.strptime(brian_time[i][0:10], '%Y-%m-%d'))   #if lenght of the element equals 11 that means that it contains only year, month and day without hours, minutes and seconds
    elif len(brian_time[i]) > 11:
        brian_time_list = brian_time[i].split(" - ") #if lenght of element is greater than 11 that means it contains 2 elements separated with " - "
        d = 0
        while d < 2:
            datetime_brian.append(datetime.strptime(brian_time_list[d], '%Y-%m-%d %H:%M:%S'))   #creatting datetime variables from txt file and adding them to a list
            d += 1
    i += 1

i = 0                           #repeating the actions for second txt file
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

def calendars(duration_in_minutes, minimum_people):     #defining the calendars function

    if minimum_people == 0:     #first condition for minimum_people argument
        print("There's no meeting.")

    elif minimum_people == 1:   #second condition
        i = 0
        while i < (len(datetime_brian) - 1):
            date_b = datetime_brian[i + 1] - datetime_brian[i]  #substracting the dates to obtain time difference between them
            if date_b < day:    #if the time difference is smaller than the value of one day, that means that a person is not available in this time period and we can plan a meeting only after the later date of the two
                range_brian_set = set(pd.date_range(start=datetime_brian[i + 1], end=datetime_end, freq='s'))
            else:   #if time difference equals one day, that means that the person is busy for all day on first date and we cant plan a meeting in that time
                if datetime_brian[i + 1] == (datetime_brian[i] + day):
                    pass
                else: #if time difference is greater than one day we can plan a meeting between first and second datetime value, but only if theres a free time greater than duration of meeting value
                    range_brian_set = set(pd.date_range((datetime_brian[i] + day), datetime_brian[i + 1], freq='s'))
                    if date_b - day > duration_in_minutes*one_min:
                        continue
                    else:
                        range_brian_set.clear()     #else the set is cleared, meeting cant be planned

            i += 1

                    #repeating the actions for second txt file
        i = 0
        while i < (len(datetime_alex) - 1):
            date_a = datetime_alex[i + 1] - datetime_alex[i]
            if date_a < day:
                range_alex_set = set(pd.date_range(start=datetime_alex[i + 1], end=datetime_end, freq='s'))
            else:
                if datetime_alex[i + 1] == (datetime_alex[i] + day):
                    pass
                else:
                    range_alex_set = set(pd.date_range((datetime_alex[i] + day), datetime_alex[i + 1], freq='s'))
                    if date_a - day > duration_in_minutes*one_min:
                        continue
                    else:
                        range_alex_set.clear()
            i += 1
        if min(range_alex_set) < min(range_brian_set):  #comparing the minimum values of both sets, finding the earliest time a meeting can be planned for 1 person
            meeting_time = min(range_alex_set) + sec
            print(meeting_time)         #meeting time is the earliest date from the set with added 1 second
        else:
            meeting_time = min(range_brian_set) + sec
            print(meeting_time)

    elif minimum_people == 2:       #third condition
        i = 0
        while i < (len(datetime_brian) - 1):        #the same methods as in previous condition
            date_b = datetime_brian[i + 1] - datetime_brian[i]
            if date_b < day:
                range_brian_set = set(pd.date_range(start=datetime_brian[i + 1], end=datetime_end, freq='s'))
            else:
                if datetime_brian[i + 1] == (datetime_brian[i] + day):
                    pass
                else:
                    range_brian_set = set(pd.date_range((datetime_brian[i] + day), datetime_brian[i + 1], freq='s'))
                    if date_b - day > duration_in_minutes*one_min:
                        continue
                    else:
                        range_brian_set.clear()
            i += 1

        i = 0
        while i < (len(datetime_alex) - 1):
            date_a = datetime_alex[i + 1] - datetime_alex[i]
            if date_a < day:
                range_alex_set = set(pd.date_range(start=datetime_alex[i + 1], end=datetime_end, freq='s'))
            else:
                if datetime_alex[i + 1] == (datetime_alex[i] + day):
                    pass
                else:
                    range_alex_set = set(pd.date_range((datetime_alex[i] + day), datetime_alex[i + 1], freq='s'))
                    if date_a - day > duration_in_minutes*one_min:
                        continue
                    else:
                        range_alex_set.clear()
            i += 1

        common_part = range_brian_set.intersection(range_alex_set)  #finding the common part in both sets - times when both workers are available for a meeting
        meeting_time = min(common_part) + sec   #meeting time is the earliest date from the common part with added one second
        print(meeting_time)

    else:
        print("Not enough people available.")   #last condition

calendars(30, 2)    #calling out the function with arguments: duration_in_minutes = 30, minimum_people = 2
