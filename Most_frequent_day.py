def most_frequent_days(year):
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    result = []
    res=[]
    if int(str(year)[:2]) in range(16,40,4): num_3 = 6
    elif int(str(year)[:2]) in range(17,40,4): num_3 = 4
    elif int(str(year)[:2]) in range(18,40,4): num_3 = 2
    elif int(str(year)[:2]) in range(19,40,4): num_3 = 0
    year_code = (num_3+year%100+year%100//4)%7
    if year%4 != 0: result.append((2+year_code)%7-2)
    elif year%100 == 0:
        if year%400==0:
            result.append((1+year_code)%7-2)
            result.append((1+year_code)%7-1)
        else:
            result.append((2+year_code)%7-2)
    else:
        result.append((1+year_code)%7-2)
        result.append((1+year_code)%7-1)
    for i in result:
        if i<0: res.append(i+7)
        else: res.append(i)
    finall = []
    for i in sorted(res): finall.append(week[i])
    return finall