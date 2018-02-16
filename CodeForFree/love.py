
print('
'.join([''.join([('+'[(x-y)%len('+')]if(x*0.05)**2*7+(-y*0.1)**2*5+(abs(x)*0.05)*(-y*0.1)*9<=5 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))
