# Most snowy city
#
# Write a method that can read and parse a file containing information about the weather in various cities
# (the file content follows the pattern of the example below). The method should take the name of the file as an
# input and return the name of the most snowy city (where the most SNOWY days measured). If there are more cities
# with the same amount of snowy days, you can decide which one to return. The function should handle possible
# exceptions by printing messages to the standard output.
#
# Example
#
# An example .txt file content can be found here:
#
# 2021-01-30;Budapest;SNOWY
# 2021-01-30;Moscow;SNOWY
# 2021-01-30;Barcelona;RAINY
# 2021-01-31;Budapest;SUNNY
# 2021-01-31;Moscow;SNOWY
# 2021-01-31;Barcelona;CLOUDY
# 2021-02-01;Budapest;SNOWY
# 2021-02-01;Moscow;SNOWY
# 2021-02-01;Barcelona;SNOWY
# 2021-02-02;Budapest;SUNNY
# 2021-02-02;Moscow;SNOWY
# 2021-02-02;Barcelona;SNOWY
# 2021-02-03;Budapest;CLOUDY
# 2021-02-03;Moscow;SNOWY
# 2021-02-03;Barcelona;SUNNY
# 2021-02-04;Budapest;RAINY
# 2021-02-04;Moscow;CLOUDY
# 2021-02-04;Barcelona;CLOUDY
# 2021-02-05;Budapest;SNOWY
# 2021-02-05;Moscow;SUNNY
# 2021-02-05;Barcelona;RAINY
# 2021-02-06;Budapest;CLOUDY
# 2021-02-06;Moscow;CLOUDY
# 2021-02-06;Barcelona;SUNNY
# 2021-02-07;Budapest;SNOWY
# 2021-02-07;Moscow;RAINY
# 2021-02-07;Barcelona;CLOUDY
# 2021-02-08;Budapest;SUNNY
# 2021-02-08;Moscow;CLOUDY
# 2021-02-08;Barcelona;CLOUDY

def most_pop_weather(filename):
    with open(filename, "r") as f:

        sentences = f.read().splitlines()
        new_list = []
        new_dic = {}

        for i in sentences:
            new_list.append(i[11:].replace(";", "-"))

        for i in new_list:
            if "SNOWY" in i:
                if i not in new_dic:
                    new_dic[i] = 0
                new_dic[i] += 1
        return max(new_dic.keys(), key=(lambda x: new_dic[x]))


print(most_pop_weather('1.txt'))
