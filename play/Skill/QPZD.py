if True:
    if per.decMp(50):
        for i in range(MaxScrX):
            if i % 2 == 0:
                fireL.append(AFire(i,0,Down,per.hitHealth))
                fireL[-1].start()
                fireL.append(AFire(i,2,Down,per.hitHealth))
                fireL[-1].start()
            fireL.append(AFire(i,1,Down,per.hitHealth))
            fireL[-1].start()
