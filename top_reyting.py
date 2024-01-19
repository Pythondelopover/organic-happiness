def reyting(max_level,username):
    top = [
        [100,'Dilshod'],
        [85,'admin'],
        [65,'Rustam_user']
    ]
    top.append([max_level, username])
    top = sorted(top)[::-1]
    s = ''
    for i in range(3):
        s += str(top[i][0])+' '+str(top[i][1])+'\n'
    return s
#top_reting(101,'Farhodjon')