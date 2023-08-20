name = ('Welcome to shiba Clock')
print(name)
def substraction(t1, t2):
    result = {}
    result['h']= t1['h'] - t2['h']
    result['m']=t1['m'] - t2['m']
    result['s']=t1['s'] - t2['s']
    if result['s']<=60:
        result['s']+=60
        result['m']-=1

    if result['m']<=60:
        result['m']+=60
        result['h']-=1

    if result['s']>=60:
        result['s']-=60
        result['m']+=1

    if result['m']>=60:
        result['m']-=60
        result['h']+=1
    return result


def show(result):
    print(f"{result['h']} :{result['m']}:{result['s']}")

time1 = {'h':9, 'm':32, 's':15}
time2 = {'h':7, 'm':25, 's':10}

result_s = substraction(time1, time2)
print(result_s)
show(result_s)
