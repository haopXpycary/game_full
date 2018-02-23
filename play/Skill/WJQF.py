if True:
    if per.decMp(20):
        for i in range(6):
            if per.headfor == Left:
                a,b = i,i
                c,d = i,-i
            if per.headfor == Right:
                a,b = -i,i
                c,d = -i,-i
            if per.headfor == Up:
                a,b = i,-i
                c,d = -i,-i
            if per.headfor == Down:
                a,b = i,i
                c,d = -i,i
                
            fireL.append(AFire(per.playerX+a,per.playerY+b,per.headfor,per.hitHealth))
            fireL[-1].start()
            fireL.append(AFire(per.playerX+c,per.playerY+d,per.headfor,per.hitHealth))
            fireL[-1].start()
    