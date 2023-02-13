# Create a map with the following key-value pairs:

names = ['William A. Lathan','John K. Miller',
         'Hortensia E. Foster','Amanda D. Newland',
         'Brooke P. Askew']

numbers=['405-709-1865','402-247-8568','606-481-6467',
         '319-243-5613','307-687-2982']

tuples = zip(names,numbers)
map_1 = {}
for k,v in tuples:
    map_1[k] = v

# What is John K. Miller's phone number?
print(map_1['John K. Miller'])

# Whose phone number is 307-687-2982?
for k, v in map_1.items():
    if v == '307-687-2982':
        print(k)

# Do we know Chris E. Myers' phone number? (Yes/No)
if 'Chris E. Myers' in map_1:
    print('Yes')
else:
    print('No')