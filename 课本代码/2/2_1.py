
#coding=utf-8
months = ['January','February','March','April','May','June','July','August','September','October','November','December']
# 以1-31作为天数的结尾
endings=['st','nd','rd'] + ['st']*17 + ['st','nd','rd'] +['st']*7 + ['st']

year = raw_input("Year:")
month = raw_input('month:')
day =  raw_input('day:')
month_number = int(month)
day_number = int(day)

# 记得天数和月数减一，以获得正确的索引
month_number = months[month_number-1]
ordinal = day + endings[day_number-1]

print month_number + " " + ordinal + '.' + year