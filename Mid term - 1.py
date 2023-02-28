# Write a function(get_hottest_day) that takes one parameter:
# measured temperatures on different weekdays(a list of dictionaries)
# and returns the day with the highest average temperature of the given weekdays based on the given
# measured temperature data. It is possible that different weekly measurements contain different days.


temperatures = [{'monday': 12, 'wednesday': 13, 'friday': 14},
                {'monday': 15, 'friday': 12},
                {'tuesday': 10, 'thursday': 11, 'saturday': 12}]


def get_hottest_day(temp):
    new_data = {}
    for i in range(len(temp)):

        new_dic = {**new_data, **temp[i]}
        for k, v in new_dic.items():
            if k in temp[i] and k in new_data:
                new_data[k] = new_data[k] + [v]
            elif k in temp[i]:
                new_data[k] = [v]

    average = {}
    for k, v in new_data.items():
        average[k] = sum(v) / len(v)

    return max(average.keys(), key=(lambda x: average[x]))


# print(get_hottest_day(temperatures))  # should return "monday"
print(get_hottest_day(temperatures))
