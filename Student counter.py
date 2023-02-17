# create a function called listOfNames() that takes a list of students and returns:
# - The name of students who have more than 4 candies

# create a function called sumOfAge() that takes a list of students and returns:
# - The sum of the age of people who have less than 5 candies

# create a function that takes a list of students and prints:
#  - how many candies they have on average

students = [
    {'name': 'Theodor', 'age': 3, 'candies': 2},
    {'name': 'Paul', 'age': 9, 'candies': 2},
    {'name': 'Mark', 'age': 12, 'candies': 5},
    {'name': 'Peter', 'age': 7, 'candies': 3},
    {'name': 'Olaf', 'age': 12, 'candies': 7},
    {'name': 'George', 'age': 10, 'candies': 1}
]


def list_of_names(my_list):
    for i in my_list:
        for k, v in i.items():
            if k == 'candies' and i[k] > 4:
                print(i['name'])


def sum_of_ages(my_list):
    sum = 0
    for i in my_list:
        for k, v in i.items():
            if k == 'candies' and i[k] < 5:
                sum += i['age']
    print(sum)


def average(my_list):
    my_sum = 0
    for i in my_list:
        for k, v in i.items():
            my_sum += i['candies']
            break

    print('{:.3}'.format(my_sum / len(my_list)))


list_of_names(students)
sum_of_ages(students)
average(students)
