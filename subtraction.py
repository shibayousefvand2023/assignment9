name = ('Welcome to Shiba Calculator')
print(name)
def subtraction(x, y): 
    result = {}
    result['s'] = (f1['s'] * f2['m'] - f2['s']*f1['m'])
    result['m'] = f1['m'] * f2['m']
    return result

def show(r):
    print(f"{r['s']} - {r['m']}")
f1 = {'s': 4, 'm':6}
f2 = {'s': 3, 'm':7}

result = subtraction(f1 , f2)
print(result)
show(result)